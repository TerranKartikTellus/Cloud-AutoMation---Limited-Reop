from googleapiclient.discovery import build
from menu.gcp.gcp_default_json_state.get_default_gcp_state import get_gcp_projectID
from flow.gcp.get_gcp_regions import get_gcp_regions
from helpers.input.text_input import text_input
from helpers.print.red import print_in_red
from helpers.print.table import print_table
from flow.gcp.helpers.get_region_from_subnet_url import get_region_from_subnet_url

def list_gcp_subnets(
  is_print: bool = True,
  project_id: str = None
  ):
  compute_service = build('compute', 'v1')
  project_id =project_id
  if not project_id:
    project_id = get_gcp_projectID()
  
  available_regions = get_gcp_regions(also_print=True)
  selected_region = available_regions[int(text_input(f"Enter region range between[1,{len(available_regions)}]: ", 'number', 0, [1,len(available_regions)]))-1]
        
  subnet_request = compute_service.subnetworks().list(project=project_id, region=selected_region)
  subnet_response = subnet_request.execute()
  # print(subnet_response) 
  if "items" in subnet_response:
    if is_print:
      rows = []
      
      for index,i in enumerate(subnet_response["items"]):
        region = get_region_from_subnet_url(i['selfLink'])
        rows.append(
          [
            index+1,
            i['id'],
            i['name'],
            i['creationTimestamp'],
            i['ipCidrRange'],
            i['gatewayAddress'],
            i['privateIpGoogleAccess'],
            region
          ]
        )
      table = print_table(["Sno","ID","NAME","CREATED AT","IPV4 Range","Gateway Addr.","Google Access","Region"],rows)
      print(table)
    input("Press Enter to proceed.")
    return subnet_response["items"]
      
  else:
    print_in_red("Request to server has failed! Please retry after some time!")
          

def list_gcp_subnets_using():
  pass