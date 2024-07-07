import subprocess

def execute_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()
    exit_code = process.returncode

    stdout_str = stdout.decode('utf-8')
    stderr_str = stderr.decode('utf-8')

    return exit_code, stdout_str, stderr_str