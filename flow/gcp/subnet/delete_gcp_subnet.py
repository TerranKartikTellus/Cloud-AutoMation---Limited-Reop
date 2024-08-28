from flow.gcp.subnet.list_gcp_subnets import list_gcp_subnets
from helpers.print.table import print_table
from menu.gcp.gcp_default_json_state.get_default_gcp_state import get_gcp_projectID
from helpers.input.text_input import text_input
from flow.gcp.helpers.get_region_from_subnet_url import get_region_from_subnet_url
from google.cloud import compute_v1
from helpers.print.green import print_in_green

def delete_gcp_subnet():
    project_id = get_gcp_projectID()

    subnets = list_gcp_subnets(is_print=False, project_id=project_id)

    if not subnets:
        print("No subnets found.")
        return

    # Display the list of subnets
    print("Available Subnets:")
    table = print_table(
        ["Sno", "Subnet Name", "Region"],
        [[i + 1, subnet['name'], get_region_from_subnet_url(subnet['selfLink'])] for i, subnet in enumerate(subnets)]
    )
    print(table)

    # Prompt for subnet selection
    selected_subnet = int(text_input("Enter the subnet number to delete: ", 'number', 0, [1, len(subnets)])) - 1
    subnet = subnets[selected_subnet]

    subnet_name = subnet['name']
    region = get_region_from_subnet_url(subnet['selfLink'])

    # Confirm deletion
    confirmation = text_input(f"Are you sure you want to delete subnet '{subnet_name}' in region '{region}'? (y/n): ", 'string', 1, ['y', 'n'])

    if confirmation.lower() == 'y':
        delete_gcp_subnet_main(project_id, region, subnet_name)
    else:
        print("Deletion canceled.")

def delete_gcp_subnet_main(project_id, region, subnet_name):
    compute_client = compute_v1.SubnetworksClient()

    # subnet_path = f"https://www.googleapis.com/compute/v1/projects/{project_id}/regions/{region}/subnetworks/{subnet_name}"
    # print(project_id, region, subnet_path)
    operation = compute_client.delete(project=project_id, region=region, subnetwork=subnet_name)
    operation.result()

    print_in_green(f"Subnet '{subnet_name}' in region '{region}' deleted successfully.")
    print("Press enter to Continue.")