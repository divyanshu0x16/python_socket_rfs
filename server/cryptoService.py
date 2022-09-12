def encryptText(text):
    typeOfEncryption = int(input('enter the type of encryption you want. input: \n1 for plain \n2 for caesar \n3 for transpose\n'))

    if (typeOfEncryption == 1):
        return text, 'plain'

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

        return result, 'caesar'

    elif (typeOfEncryption == 3):
        return text[::-1], 'transpose'

    raise Exception('enter a valid type')

def decryptText(text, encryptionType):

    if(encryptionType == 'plain'):
        return text

    elif(encryptionType == 'caesar'):

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

    elif(encryptionType == 'transpose'):
        return text[::-1]