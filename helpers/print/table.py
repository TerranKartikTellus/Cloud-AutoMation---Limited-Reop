from prettytable import PrettyTable
from prettytable import SINGLE_BORDER

def print_table(column_names, rows):
    table = PrettyTable()
    table.field_names = column_names
    table.set_style(SINGLE_BORDER)

    for index, row in enumerate(rows):
        table.add_row(row)

    return table