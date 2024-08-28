from google.cloud import compute_v1
from helpers.print.yellow import print_in_yellow
from menu.gcp.gcp_default_json_state.get_default_gcp_state import get_gcp_projectID
from flow.gcp.instance.list_gcp_instances import list_gcp_instances
from helpers.input.text_input import text_input

def delete_gcp_instance():
    compute_client = compute_v1.InstancesClient()

    project_id = get_gcp_projectID()
    instances = list_gcp_instances(project_id=project_id)
    selected_instance = instances[int(text_input(f"Enter Instance you would like to delete [1,{len(instances)}]: ", 'number', 0, [1,len(instances)]))-1]
    # print(selected_instance)

    
    sure = input(f"Are you sure you want to delete instance {selected_instance['name']}? Y/N: ")
    if sure == 'y' or sure == 'Y':
      instance_name = selected_instance['name']
      zone = selected_instance['zone'].split('/')[-1]
      print_in_yellow(f"Please wait while we delete instance '{instance_name}' in zone:{zone} !")

      operation = compute_client.delete(project=project_id,zone=zone, instance=instance_name)
      operation.result()

      print(f"Instance '{instance_name}' deleted successfully!")

