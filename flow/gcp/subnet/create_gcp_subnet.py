from flow.gcp.vpc.create_gcp_vpc import create_gcp_vpc
from helpers.input.text_input import text_input
from menu.gcp.gcp_default_json_state.get_default_gcp_state import get_gcp_projectID
from flow.gcp.vpc.list_gcp_vpcs import list_gcp_vpcs
from googleapiclient.discovery import build
from helpers.print.red import print_in_red
from helpers.menu.read_json_menu import read_json_menu
from helpers.print.table import print_table
import time
from google.cloud.compute_v1 import NetworksClient, GlobalOperationsClient
from helpers.LOGS.log_now import log_now
from helpers.print.green import print_in_green
import uuid
from google.cloud import compute_v1
from flow.gcp.get_gcp_regions import get_gcp_regions

def create_gcp_subnet():

        project_id = get_gcp_projectID()

        subnet_name = text_input("Enter Subnet name [min length 3]: ", 'string', 3, [])
        description = text_input("Enter description [min length 3]: ", 'string', 3, [])
        vpc_name = get_gcp_vpc_list(project_id)
        ipCidrRange = text_input("Enter IPV4 range in Cider fomat eg: 10.0.0.0/23: ", 'string', 8, [])
        available_regions = get_gcp_regions(also_print=True)
        selected_region = available_regions[int(text_input(f"Enter region [1,{len(available_regions)}]: ", 'number', 0, [1,len(available_regions)]))-1]
        print(selected_region)
        
        subnet_body = {
          "allowSubnetCidrRoutesOverlap": False,
          "description": description,
          "enableFlowLogs": False,
          "ipCidrRange": ipCidrRange,
          "name": subnet_name,
          "network": f"projects/{project_id}/global/networks/{vpc_name}",
          "privateIpGoogleAccess": False,
          "region": f"projects/{project_id}/regions/{selected_region}",
          "selfLink": "",
          "stackType": "IPV4_ONLY"
        }
        compute_service = build('compute', 'v1')







        try:
          # client = SubnetworksClient()
          
          subnet_request = compute_service.subnetworks().insert(project=project_id, region= selected_region, body=subnet_body)
          subnet_response = subnet_request.execute()
          
          print_in_green(f"Subnet '{subnet_name}' created in VPC {vpc_name} successfully.")
          l_id = str(uuid.uuid4())
          log_now(
              function_name=create_gcp_subnet.__name__, 
              log_type='success', 
              message=str(f"Subnet '{subnet_name}' created in VPC {vpc_name} successfully."), 
              log_id=l_id
          )
        except Exception as e:
          l_id = str(uuid.uuid4())
          print_in_red(f"Error occured in Subnet creation | log id: {l_id}")

          log_now(
              function_name=create_gcp_subnet.__name__, 
              log_type='error', 
              message=str(e), 
              log_id=l_id
          )

        
        
        
        
        
        
        
        
        
        
def get_gcp_vpc_list(project_id):
  vpcs = list_gcp_vpcs(project_id)
  selected_vpc = int(input(f"Select a VPC: "))-1
  if selected_vpc < len(vpcs):
  # print(str(vpcs[selected_vpc]))
    return str(vpcs[selected_vpc]['name'])
  else:
    print_in_red("Please Select a valid VPC")
    get_gcp_vpc_list(project_id)

