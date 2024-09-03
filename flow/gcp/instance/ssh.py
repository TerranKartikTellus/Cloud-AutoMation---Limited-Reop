import paramiko
from flow.ssh.docker.check_docker_version import check_docker_version

def install_docker(ssh):
    print("Installing Docker...")
    stdin, stdout, stderr = ssh.exec_command('sudo apt-get update && sudo apt-get install -y docker.io')
    output = stdout.read().decode().strip()
    print("Docker installation output:")
    print(output)

    # Start Docker service
    stdin, stdout, stderr = ssh.exec_command('sudo systemctl start docker')
    output = stdout.read().decode().strip()
    print("Docker service start output:")
    print(output)

    # Enable Docker service to start at boot
    stdin, stdout, stderr = ssh.exec_command('sudo systemctl enable docker')
    output = stdout.read().decode().strip()
    print("Docker service enable output:")
    print(output)


    
def exec_commands(ssh):    
    print("Checking if Docker is installed...")
    stdin, stdout, stderr = ssh.exec_command('which docker')
    if stdout.read().decode().strip() == '':
        print("Docker is not installed. Installing...")
        install_docker(ssh)
        check_docker_version(ssh)
    else:
        print("Docker is already installed.")
        check_docker_version(ssh)
        
        
def check_ssh(instance_ip, private_key_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    key = paramiko.RSAKey.from_private_key_file(private_key_file)
    try:
        ssh.connect(instance_ip, username='kartik2', pkey=key)
        print("SSH connection successful!")
        
        exec_commands(ssh)
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
    finally:
        ssh.close()

instance_ip = '34.159.112.248'
private_key_file = '/Users/kartik2/Documents/Cloud Creds/AWS/02-sept-2024'
check_ssh(instance_ip, private_key_file)

