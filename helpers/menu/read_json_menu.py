import json

def read_json_menu(file_path):
      with open(file_path, "r") as file:
        main_menu_items = json.load(file)
      return main_menu_items