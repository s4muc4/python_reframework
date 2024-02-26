import random
import string
import os
from datetime import datetime
from Components.logs import *

def logMessage(message, logLevel):
    print(logLevel + ' - ' + message)
    saveLog(logLevel + ' - ' + message)
    

def generateHashCodeProject():
    deleteHashCodeProject('hash_code.txt')
    characters = string.digits + string.ascii_letters

    # Generate a random code using the specified length
    random_code = ''.join(random.choice(characters) for _ in range(15))

    # Save the random code to a file
    with open('hash_code.txt', 'w') as file:
        file.write(random_code+"-"+datetime.now().strftime("%H-%M-%S -- "))

def deleteHashCodeProject(file_path):
    try:
        os.remove(file_path)
    except Exception as error:
        print(f"{file_path} dont exist. OK!")

def retrieveHashCodeProject():
    with open('hash_code.txt', 'r') as file:
        text = str(file.read())

        hash = text[0:15]
        time = text[16:24]
        return hash, time

def saveLog(message):
    hash, time = retrieveHashCodeProject()
    file_path = f"Logs/log_{time}_{hash}.txt"

    if os.path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write(datetime.now().strftime("%H:%M:%S - ")+ message + '\n')
    else:
        with open(file_path, 'w') as file:
            file.write(datetime.now().strftime("%H:%M:%S - ")+ message + '\n')

    
    if 'AUTOMATION ENDED' in message:
        deleteHashCodeProject('hash_code.txt')

def clear_logs_output():
    # Determine the operating system
    operating_system = os.name

    if operating_system == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif operating_system == 'nt':  # Windows
        os.system('cls')
    else:
        print("Unsupported operating system")