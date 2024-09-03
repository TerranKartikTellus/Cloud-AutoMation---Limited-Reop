import paramiko
from flow.ssh.docker.check_docker_version import check_docker_version
from helpers.input.text_input import text_input
from helpers.print.table import print_table
from helpers.menu.read_json_menu import read_json_menu
from helpers.print.red import print_in_red
from helpers.print.yellow import print_in_yellow
from helpers.print.green import print_in_green

def install_docker(ssh):
    print_in_yellow("Installing Docker...")
    command = "sudo apt-get update && sudo apt-get install -y docker.io"
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode().strip()
    print("Docker installation output:")
    print(output)
    
    table = print_table([f"Commands:",f"{command}"],[["Docker installation output",output]])
    print(table)
    input("Press enter to start docker service")

    command = "sudo systemctl start docker"
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode().strip()

    table = print_table([f"Commands:",f"{command}"],[["Docker service start output:",output]])
    print(table)
    input("Press enter to start docker service on startup")

    command = "sudo systemctl enable docker"
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode().strip()
    table = print_table([f"Commands:",f"{command}"],[["Docker service enable output:",output]])
    print(table)
    input("Press enter to continue!")



    
def exec_commands(ssh):    
    print_in_yellow("Checking if Docker is installed...")
    stdin, stdout, stderr = ssh.exec_command('which docker')
    # print(str(stdout))
    if stdout.read().decode().strip() == '':
        print_in_red("Docker is not installed. Installing...")
        install_docker(ssh)
        check_docker_version(ssh)
    else:
        print("Docker is already installed.")
        check_docker_version(ssh)
    input("-----")
        

def check_ssh():
    gcp_state = read_json_menu("./state/gcp.json")

    instance_ip = text_input("Enter instance public ip: ", 'string', 10, [])
    private_key_file = input(f"Private key location: (default: {gcp_state["private_key_file"]}) ") or gcp_state["private_key_file"]

    
    table = print_table(["Instance", "Private Key Location"],[[instance_ip, private_key_file]])
    print(table)
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    key = paramiko.RSAKey.from_private_key_file(private_key_file)
    try:
        ssh.connect(instance_ip, username='kartik2', pkey=key)
        print_in_green("SSH connection successful!")
        input("Press enter to verify presence of \n  - docker ")
        exec_commands(ssh)
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
    finally:
        ssh.close()



