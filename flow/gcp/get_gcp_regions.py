from helpers.menu.read_json_menu import read_json_menu
from helpers.print.table import print_table

def get_gcp_regions(also_print: bool = False):
  regions = read_json_menu('./state/gcp.json')["available_regions"]
  if also_print:
    rows = []
    for index,i in enumerate(regions):
      rows.append([index+1, i])
    table = print_table(["Sno", "Regions"],rows)
    print(table)
  
  return regions