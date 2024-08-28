from collections import defaultdict
from collections.abc import Iterable

from google.cloud import compute_v1
from helpers.print.table import print_table
from helpers.menu.read_json_menu import read_json_menu
from menu.gcp.gcp_default_json_state.get_default_gcp_state import get_gcp_projectID
from helpers.LOGS.save_object_to_file import save_object_to_file


    
  
def list_gcp_instances(is_print: bool = True,project_id:str=None):
    project_id = project_id
    if not project_id:
      project_id = get_gcp_projectID()

    instances = list_all_instances(project_id)

    if is_print:
      # for instance in instances:
          # print(f"Instance name: {instance['name']}")
          # print(f"Instance ID: {instance.id}")
          # print(f"Type type: {instance['type']}")
          # print(f"Zone: {instance['zone']}")
          # print("-----")
      table = print_table(
        ["Sno","Instance name","Machine type","Zone"],
        [[index+1,instance['name'],instance['type'].split('/')[-1],instance['zone']] for index, instance in enumerate(instances)]
      )
      print(table)
      input("Press enter to continue")
      return instances
    else:
      return instances






def list_all_instances(
    project_id: str,
) -> dict[str, Iterable[compute_v1.Instance]]:

    instance_client = compute_v1.InstancesClient()
    request = compute_v1.AggregatedListInstancesRequest()
    request.project = project_id
    request.max_results = 50

    agg_list = instance_client.aggregated_list(request=request)
    instance_obj = []
    all_instances = defaultdict(list)
    # save_object_to_file(all_instances, "object.txt")

    for zone, response in agg_list:
        if response.instances:
            all_instances[zone].extend(response.instances)
            # print(f" {zone}:")
            for instance in response.instances:
                # print(f" - {instance.name} ({instance.machine_type})")
                instance_obj.append({
                  "name": instance.name,
                  "type": instance.machine_type,
                  "zone":zone
                })
                

                
    # print(all_instances)
    return instance_obj