import subprocess

def run_shell(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result.strip()
    except Exception as e:
        return str(e)

def get_system_info():
    return run_shell("uname -a")
