
alphaArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

caeserDict = {}

def caeserEncryption(message, shift):
    for i in range(len(alphaArray)):
        key = alphaArray[i]
        value_index = (i+shift) % len(alphaArray)
        value = alphaArray[value_index]
        caeserDict[key] = value

    encryptedMsg = ""
    for letter in message:
        if letter==' ':
            encryptedMsg = encryptedMsg + letter
        else:
            encryptedMsg = encryptedMsg + caeserDict[letter]
    return encryptedMsg

def caeserDecryption(message, shift):
    for i in range(len(alphaArray)):
        key = alphaArray[i]
        value_index = (i - shift) % len(alphaArray)
        value = alphaArray[value_index]
        caeserDict[key] = value

    decryptedMsg = ""
    for letter in message:
        if letter==' ':
            decryptedMsg = decryptedMsg + letter
        else:
            decryptedMsg = decryptedMsg + caeserDict[letter]
    return decryptedMsg

command = str(input("Enter Command: "))
s = int(input("Shift value: "))

if command == "Encryption":
    msg = str(input("Enter message for Encryption: "))
    print(caeserEncryption(msg, s))

elif command == "Decryption":
    msg = str(input("Enter message for Decryption: "))
    print(caeserDecryption(msg, s))

else:
    print("Invalid command.")

