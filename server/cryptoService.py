def encryptText(text, typeOfEncryption):

    if (typeOfEncryption == 1):
        return text

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

        return result

    elif (typeOfEncryption == 3):
        return text[::-1]

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