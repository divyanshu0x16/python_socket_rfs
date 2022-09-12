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