from googleapiclient.discovery import build
from menu.gcp.gcp_default_json_state.get_default_gcp_state import get_gcp_projectID
from helpers.print.green import print_in_green

def delete_gcp_vpc(project_id,vpc_name):
    project_id = get_gcp_projectID()
    compute_service = build('compute', 'v1')

    vpc_request = compute_service.networks().delete(project=project_id, network=vpc_name)
    response = vpc_request.execute()
    print_in_green(f"VPC {vpc_name} deleted successfully.")