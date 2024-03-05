import subprocess


def execute_shell_command(shell_command):
    try:
        result = subprocess.run(shell_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Shell command executed successfully:")
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error executing shell command: {e}")
        print(e.stderr.decode('utf-8'))


execute_shell_command('python --version')
