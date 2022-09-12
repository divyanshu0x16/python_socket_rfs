import os
import subprocess

def handleCommand(command):
    #TODO: Complete Functionality

    if (command == 'cwd'):
        output = subprocess.run('pwd', capture_output=True).stdout.decode('utf-8')
        return output
    elif (command == 'ls'):
        output = subprocess.run(command, capture_output=True).stdout.decode('utf-8')
        return output
    elif ( command.startswith('cd ') ):
        #checking if the path is a directory
        file_path = command[3:]

        if os.path.isdir(file_path):
            return command
        else:
            return ('not a valid directory: %s'%(file_path))
    elif ( command.startswith('dwd ') or command.startswith('upd ') ):
        #checking if the path is a file
        file_path = command[4:]
        
        if os.path.isfile(file_path):
            return command
        else:
            return ('not a valid file: %s'%(file_path))