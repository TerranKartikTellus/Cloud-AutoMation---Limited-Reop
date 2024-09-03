import time
from google.cloud import compute_v1
from flow.gcp.subnet.list_gcp_subnets import list_gcp_subnets
from helpers.print.table import print_table
from menu.gcp.gcp_default_json_state.get_default_gcp_state import get_gcp_projectID
from helpers.input.text_input import text_input
from flow.gcp.helpers.get_region_from_subnet_url import get_region_from_subnet_url
from flow.gcp.zone.gcp_get_all_available_zone_in_region import gcp_get_all_available_zones_in_region
from helpers.print.yellow import print_in_yellow
from helpers.print.green import print_in_green


def create_gcp_instance():
    compute_client = compute_v1.InstancesClient()

    instance_name = input("Enter the instance name: ")

    # zone = input("Enter the zone (default: us-central1-a): ") or "us-central1-a"
    project_id = get_gcp_projectID()

    network_interfaces,region,zone = configure_network_interface(project_id)

    instance = {
        "name": instance_name,
        "machine_type": f"projects/{project_id}/zones/{zone}/machineTypes/e2-medium",
        # "metadata": {
        # "items": [
        #     {
        #       "key": "ssh-keys",
        #       "value": "kartik2:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5VZMbhbhjbkJEEuIUuKG4260UYp+1bf2xEeXc59sF6MtDwRB5/k4uSrVmJkK0Unba+h5z6NrORxXzzwJSVKPtj9XzFm3lCnh73DD1xtK9j0CpK81ehpudn+CNPCnj9F3o9onAtTdshNdsxkCI0uhtX3p8RSLr49nvyu2YxT7sHLP/AY5+kqm2p7oeGey4LJduxBFjcx35jbj9N9QIHL4vjtfg5YLcNeM+VbKpKMQgaIPHF/Xakt/1ajPXssZ3xekol35JKs9J8PedeUSmbF4b13lLGZagwtevgeum/9dYreCXBMlHZ83kflFthYk13UQhtfb2xNjF6KrIgC7W2yAbsbJmP kartik2@kartik2-mac-0"
        #     }
        #   ]
        # },
        "zone": zone,
        "disks": [
            {
              "auto_delete": True,
              "boot": True,
              "device_name": "instance-20240826-041440",
              "disk_encryption_key": {},
              "initialize_params": {
                "disk_size_gb": "10",
                "disk_type": f"projects/{project_id}/zones/{zone}/diskTypes/pd-balanced",
                "labels": {},
                "source_image": "projects/debian-cloud/global/images/debian-12-bookworm-v20240815"
              },
              "mode": "READ_WRITE",
              "type": "PERSISTENT"
            }
          ],
          "network_interfaces": network_interfaces
    }
    response = compute_client.insert(project=project_id, zone=zone, instance_resource=instance)

    print(f"Instance '{response.name}' creation initiated successfully!")
    table = print_table(
      ["Sno", "Inctance Name"], 
      [[1, instance_name]]
      )
    print(table)
    print_in_yellow("Waiting for instance to complete initialization, this may take sometime")

# ---------

    while response.status is not 'RUNNING':
        if response.status == 'RUNNING':
          break
        print(f"> Current State: {response.status}")
        time.sleep(5)
        response = compute_client.get(project=project_id, zone=zone, instance=instance_name)

    print_in_yellow("Fetching metadata")

    metadata = response.metadata.items
    # print(response)
    ssh_keys = [item.value for item in metadata if item.key == 'ssh-keys']
    print(ssh_keys)
    if ssh_keys:
        ssh_key = ssh_keys[0]
        username, _, key_filename = ssh_key.partition(' ')

        
        print_in_green(f"Instance SSH username: {username}")
        # print(f"Key filename: {key_filename}")
    else:
        print("No SSH keys found in instance metadata.")
# ---------
    
    input("Press Enter to continue")


def configure_network_interface(project_id):
    awailavle_subnets = list_gcp_subnets(
      project_id=project_id
    )
    
    # ToDO: one VM can have multiple subnets too but for now let's have
    # ToDo: 1 subnet assigned for a VM
    selected_region = awailavle_subnets[int(text_input(f"Enter subnets you would like to use [1,{len(awailavle_subnets)}]: ", 'number', 0, [1,len(awailavle_subnets)]))-1]
    # print(selected_region['selfLink'])
    # print(selected_region['stackType'])
    region = get_region_from_subnet_url(selected_region['selfLink'])
    
    # a=a="https://www.googleapis.com/compute/v1/projects/terrankartiktellus/regions/asia-east1/subnetworks/sub1"
    # path_parts = a.split('/')
    # print('/'.join(path_parts[5::]))
    subnetworklink = '/'.join(selected_region['selfLink'].split('/')[5::])

    network_interfaces = [
              {
                "access_configs": [
                  {
                    "name": "External NAT",
                    "network_tier": "PREMIUM"
                  }
                ],
                "stack_type": selected_region['stackType'],
                "subnetwork":subnetworklink
              }
      ]
    
    available_zones = gcp_get_all_available_zones_in_region(
      is_print=True,
      project_id=project_id,
      region=region
    )
    selected_zone = available_zones[int(text_input(f"Enter a zone [1,{len(available_zones)}]: ", 'number', 0, [1,len(available_zones)]))-1][1]
    # print(network_interfaces,region,selected_zone)
    return network_interfaces,region,selected_zone