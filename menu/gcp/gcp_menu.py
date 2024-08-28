from helpers.menu.load_main_menu import load_main_menu
from helpers.menu.if_x_is_y_run_func import if_x_is_y_run_func
from menu.gcp.cloud_compute.cloud_compute_menu import cloud_compute_menu
from helpers.print.yellow import print_in_yellow
from helpers.menu.read_json_menu import read_json_menu
from menu.gcp.vpc.vpc_menu import vpc_menu
from menu.gcp.subnet.subnet_menu import gcp_subnet_menu

def gcp_menu():
    from menu.home_menu import home_menu
    
    where = "GCP"
    main_menu_items = [
      {
        "desc": "VPC"
      },
      {
        "desc": "Subnet"
      },
      {
        "desc": "Cloud Compute"
      }
    ]
    user_selection = load_main_menu(main_menu_items,where)


    if user_selection == -1:
      # previous menu to this is = home
      home_menu()
    else:
      if_x_is_y_run_func(user_selection,1,vpc_menu)
      if_x_is_y_run_func(user_selection,2,gcp_subnet_menu)
      if_x_is_y_run_func(user_selection,3,cloud_compute_menu)
    
    gcp_menu()