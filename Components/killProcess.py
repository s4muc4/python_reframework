from Components.logs import logMessage
import os
import subprocess

def killProcess(process_name):

    result = subprocess.run(f'taskkill /F /IM {process_name}.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        logMessage(f"No process found with name {process_name}.", "TRACE")
    else:
        logMessage(f"Process {process_name} killed.", "TRACE")

        
