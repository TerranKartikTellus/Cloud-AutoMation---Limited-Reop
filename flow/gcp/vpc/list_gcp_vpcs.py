from googleapiclient.discovery import build
from menu.gcp.gcp_default_json_state.get_default_gcp_state import get_gcp_projectID
from helpers.print.table import print_table

def list_gcp_vpcs(project_ID: str = None):
  project_id=''
  if project_ID:
    project_id = project_ID
  else:
    project_id = get_gcp_projectID()
  compute_service = build('compute', 'v1')

  vpcs_request = compute_service.networks().list(project=project_id)
  vpcs_list = vpcs_request.execute()
  l = vpcs_list.get('items', [])
  rows = []
  for index,i in enumerate(l):
    no_of_subnets = len(i["subnetworks"]) if "subnetworks" in i else 0
    rows.append([index+1,i["name"],i["id"],i["kind"],no_of_subnets])

  table = print_table(["SNO","VPC Name","ID","RESOURCE KIND","No. OF SUBNETS"],rows)
  print(table)
  return l
    
