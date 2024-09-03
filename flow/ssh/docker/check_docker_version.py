from helpers.print.yellow import print_in_yellow
from helpers.print.table import print_table

def check_docker_version(ssh):
    print_in_yellow("Checking Docker version...")
    command = "docker --version"
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode().strip()

    table = print_table([f"Commands:",f"{command}"],[[">",output]])
    print(table)
    input("Press enter to continue!")