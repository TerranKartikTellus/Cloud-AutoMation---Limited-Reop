from helpers.print.yellow import print_in_yellow

def check_docker_version(ssh):
    print_in_yellow("Checking Docker version...")
    stdin, stdout, stderr = ssh.exec_command('docker --version')
    output = stdout.read().decode().strip()
    print("Docker version:")
    print(output)