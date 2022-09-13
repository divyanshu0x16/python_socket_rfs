import os

def takeInput():
    command = input("enter the command you want to execute on server, 'q' to quit\n")
    return command

def writeFile(data, name):
    file = open(name, 'w')
    file.write(data)
    file.close()
    return 0

def readFile(command):
    filePath = command[4:]

    if os.path.isfile(filePath):
        fileName = os.path.basename(filePath)
        file = open(filePath, 'r')
        data = file.read()

        return data, fileName
    else:
        raise Exception('enter a valid file path')