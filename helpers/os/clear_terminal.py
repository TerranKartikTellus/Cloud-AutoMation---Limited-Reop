import os

def clear_terminal():
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)