from helpers.print.red import print_in_red
from helpers.print.table import print_table
from helpers.os.clear_terminal import clear_terminal
from helpers.print.print_cvo import print_cvo

def load_main_menu(main_menu_items, menu_name):
    clear_terminal()
    print_cvo()
    print_in_red(f"\n\n========={menu_name} Selection Menu===========")

    
    rows = []
    rows.append([0, "Exit"])
    for index, item in enumerate(main_menu_items):
        rows.append([index+1, item['desc']])
    rows.append([len(main_menu_items)+1, "Previous Menu"])
    menu_table = print_table(["Option", "Description"],rows)
    print(menu_table)
    

    no_of_options = len(main_menu_items) + 1
    user_input = int(input(f"Select option (0-{no_of_options}): "))

    if user_input == 0:
        inp = input("Sure you want to exit? : [Y/N]: ")
        if inp == 'Y' or inp == 'y':
            print("\n")
            exit(0)
    elif user_input == len(main_menu_items) + 1:
        return -1

    if user_input >= 1 and user_input <= no_of_options:
        return user_input
    else:
        return load_main_menu(file_path, menu_name)
