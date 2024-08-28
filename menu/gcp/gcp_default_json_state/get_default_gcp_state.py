from helpers.menu.read_json_menu import read_json_menu

def get_gcp_projectID():
  gcp_state = read_json_menu("./state/gcp.json")

  projectID = ""
  if gcp_state['projectID']:
    projectID = input(f"Enter the project ID(default: {gcp_state['projectID']}): ") or gcp_state['projectID']
    return projectID
  else:
    projectID = input(f"Enter the project ID: ")
    return projectID
  
def get_gcp_zone():
  
  input("Enter the zone (press Enter for all zones): ")