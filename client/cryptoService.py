def encryptText(text, typeOfEncryption = None):

    while(typeOfEncryption == None or typeOfEncryption not in range(1, 4)):
        try:
            typeOfEncryption = int(input('enter the type of encryption you want. input: \n1 for plain \n2 for caesar \n3 for transpose\n0 to quit\n'))
        except:
            print('invalid type entered. try again')
            continue
        
        if (typeOfEncryption not in range(0, 4)):
            print('invalid type entered. try again')
        else:
            break

    if (typeOfEncryption == 1):
        return text, 1

    elif (typeOfEncryption == 2):
        #reference: https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
        result = ""

        for i in range(len(text)):
            current = text[i]

            if( current.isupper() ):
                result += chr((ord(current) + 2 - 65) % 26 + 65)
            elif( current.islower() ):
                result += chr((ord(current) + 2 - 97) % 26 + 97)
            elif( current.isnumeric() ):
                result += str((int(current) + 2)%10)
            else:
                result += current

        return result, 2

    elif (typeOfEncryption == 3):
        return text[::-1], 3
    
    elif (typeOfEncryption == 0):
        return None, 0

def decryptText(text, encryptionType):

    if(encryptionType == 1):
        return text

    elif(encryptionType == 2):

        result = ''

        for i in range(len(text)):
            current = text[i]

            if( current.isupper() ):
                result += chr((ord(current) + 24 - 65) % 26 + 65)
            elif( current.islower() ):
                result += chr((ord(current) + 24 - 97) % 26 + 97)
            elif( current.isnumeric() ):
                result += str((int(current) - 2)%10)
            else:
                result += current

        return result

    elif(encryptionType == 3):
        return text[::-1]
    