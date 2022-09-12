import os
import subprocess

def handleCommand(command):
    if (command == 'cwd'):
        output = subprocess.run('pwd', capture_output=True).stdout.decode('utf-8')
        return output
    elif (command == 'ls'):
        output = subprocess.run(command, capture_output=True).stdout.decode('utf-8')
        return output
    elif ( command.startswith('cd ') ):
        #checking if the path is a directory
        filePath = command[3:]

        if os.path.isdir(filePath):
            os.chdir(filePath)
            return 'OK'
        else:
            return 'NOK'
    elif ( command.startswith('dwd ') ):
        #checking if the path is a file
        filePath = command[4:]
        
        if os.path.isfile(filePath):
            fileName = os.path.basename(filePath)
            #TODO: Check for binary file
            file = open(filePath, 'r')
            data = file.read()

            return data, fileName
        else:
            return 'NOK'