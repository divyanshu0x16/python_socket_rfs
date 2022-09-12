import os

def handleCommand(command):
    #TODO: Complete Functionality

    if (command == 'cwd'):
        return command
    elif (command == 'ls'):
        return ls
    elif ( command.startswith('cd ') ):
        #checking if the path is a directory
        file_path = command[3:]

        if os.path.isdir(file_path):
            return command
        else:
            raise Exception('not a valid directory: %s'%(file_path))
    elif ( command.startswith('dwd ') or command.startswith('upd ') ):
        #checking if the path is a file
        file_path = command[4:]
        
        if os.path.isfile(file_path):
            return command
        else:
            raise Exception('not a valid file: %s'%(file_path))
    raise Exception('Please enter a valid command')