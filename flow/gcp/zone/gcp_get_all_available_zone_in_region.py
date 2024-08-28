from google.cloud import compute_v1
from helpers.print.table import print_table

def gcp_get_all_available_zones_in_region(is_print: bool = True, project_id: str="", region: str=""):
    client = compute_v1.ZonesClient()
    all_zones = client.list(project=project_id)
    
    available_zones = []
    i = 1
    for zone in all_zones:
        if region in zone.name:
            available_zones.append([i, zone.name])
            i+=1
    
    if is_print:
        table = print_table(["Sno", "Available Zone"], available_zones)
        print(table)
    
    input("Press enter to proceed.")
    
    return available_zones
