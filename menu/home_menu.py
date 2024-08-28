from helpers.menu.load_main_menu import load_main_menu
from menu.gcp.gcp_menu import gcp_menu
from menu.aws.aws_menu import aws_menu
from menu.azure.azure_menu import azure_menu
from helpers.menu.if_x_is_y_run_func import if_x_is_y_run_func
from helpers.print.print_cvo import print_cvo

def home_menu():


    where = "Home"
    main_menu_items = [
      {
        "desc": "GCP"
      },
      {
        "desc": "AWS"
      },
      {
        "desc": "AZURE"
      }
    ]
    user_selection = load_main_menu(main_menu_items,where)
    
    if user_selection == -1:
      # previous menu to this is = exit
      exit(0)
    else:
      if_x_is_y_run_func(user_selection,1,gcp_menu)
      if_x_is_y_run_func(user_selection,2,aws_menu)
      if_x_is_y_run_func(user_selection,3,azure_menu)
      
    home_menu()