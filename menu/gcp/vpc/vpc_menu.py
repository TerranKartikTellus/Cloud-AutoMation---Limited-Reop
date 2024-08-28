from helpers.menu.load_main_menu import load_main_menu
from helpers.menu.if_x_is_y_run_func import if_x_is_y_run_func
from flow.gcp.vpc.create_gcp_vpc import create_gcp_vpc
from flow.gcp.vpc.list_gcp_vpcs import list_gcp_vpcs
from flow.gcp.vpc.delete_gcp_vpc import delete_gcp_vpc


def vpc_menu():
    from menu.gcp.gcp_menu import gcp_menu
  
    where = "VPC"
    main_menu_items = [
      {
        "desc": "Create VPC"
      },
      {
        "desc": "List all VPC"
      },
      {
        "desc": "Update all VPC"
      },
      {
        "desc": "Delete all VPC"
      },
      
    ]
    user_selection = load_main_menu(main_menu_items,where)


    print(user_selection)
    if user_selection == -1:
      # previous menu to this is = home
      gcp_menu()
    else:
      if_x_is_y_run_func(user_selection,1,create_gcp_vpc)
      if_x_is_y_run_func(user_selection,2,list_gcp_subnets)
      # if_x_is_y_run_func(user_selection,4,delete_gcp_vpc)
    