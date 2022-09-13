import os

def takeInput():
    command = input("enter the command you want to execute on server, 'q' to quit\n")

    if (command == 'cwd' or command == 'ls' or command.startswith('cd ') or  command.startswith('dwd ') or command.startswith('upd ') or command == 'q'):
        return command
    raise Exception('enter a valid command')

def writeFile(data, name):
    file = open(name, 'w')
    file.write(data)
    file.close()
    return 0

def readFile(command):
    filePath = command[4:]

    if os.path.isfile(filePath):
        fileName = os.path.basename(filePath)
        #TODO: Check for binary file
        file = open(filePath, 'r')
        data = file.read()

        return data, fileName
    else:
        raise Exception('enter a valid file path')