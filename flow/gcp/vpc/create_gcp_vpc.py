from menu.gcp.gcp_default_json_state.get_default_gcp_state import get_gcp_projectID
from helpers.input.text_input import text_input
from google.cloud import compute_v1
from google.cloud.compute_v1 import NetworksClient, GlobalOperationsClient
from helpers.print.red import print_in_red
from helpers.print.green import print_in_green
from helpers.LOGS.log_now import log_now
import uuid

def create_gcp_vpc():
    project_id = get_gcp_projectID()
    vpc_name = text_input("Enter VPC name [min length 3]: ", 'string', 3, [])
    description = text_input("Enter description [min length 3]: ", 'string', 3, [])
    create_gcp_vpc_using(vpc_name,description,project_id)
    # print(project_id, vpc_name, description)


def create_gcp_vpc_using(vpc_name,description,project_id):
    vpc_resource = compute_v1.Network(
        name=vpc_name,
        auto_create_subnetworks=False,
        description=description,
        mtu=1460,
        routing_config={
            "routing_mode": "REGIONAL",
        },
    )
    try:
      client = NetworksClient()
      operation = client.insert(project=project_id, network_resource=vpc_resource)
      print_in_green(f"VPC '{vpc_name}' created successfully.")
      l_id = str(uuid.uuid4())
      log_now(
          function_name=create_gcp_vpc_using.__name__, 
          log_type='success', 
          message=str(f"VPC '{vpc_name}' created successfully."), 
          log_id=l_id
      )
    except Exception as e:
      print_in_red(f"Error during VPC creation | log id: {l_id}")
      l_id = str(uuid.uuid4())
      log_now(
          function_name=create_gcp_vpc_using.__name__, 
          log_type='error', 
          message=str(e), 
          log_id=l_id
      )