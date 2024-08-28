from helpers.menu.load_main_menu import load_main_menu
from helpers.menu.if_x_is_y_run_func import if_x_is_y_run_func
from flow.gcp.instance.create_gcp_instance import create_gcp_instance
from flow.gcp.instance.list_gcp_instances import list_gcp_instances
from flow.gcp.instance.delete_gcp_instance import delete_gcp_instance

def cloud_compute_menu():
    from menu.gcp.gcp_menu import gcp_menu
    
    prev_menu = gcp_menu

    current_menu = cloud_compute_menu

    where = "Cloud Compute"
    main_menu_items = [
      {
        "desc": "Create Compute"
      },
      {
        "desc": "List All Compute"
      },
      {
        "desc": "Update Compute"
      },
      {
        "desc": "Delete Compute"
      }
    ]
    user_selection = load_main_menu(main_menu_items,where)
    
    # print(user_selection)
    if user_selection == -1:
      # previous menu to this is = home
      prev_menu()
    else:
      pass
      if_x_is_y_run_func(user_selection,1,create_gcp_instance)
      if_x_is_y_run_func(user_selection,2,list_gcp_instances)
      # if_x_is_y_run_func(user_selection,3,azure_menu)
      if_x_is_y_run_func(user_selection,4,delete_gcp_instance)
    
    
    
    cloud_compute_menu()