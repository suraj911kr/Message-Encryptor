import caeser_dict
import morse_dict

def caeser(phrase):
    code = ""
    for letter in phrase:
        code = code + caeser_dict.cce[letter]
    return code

def caeser_decrypt(phrase):
    code = ""
    for letter in phrase:
        code = code + caeser_dict.ccd[letter]
    return code

def morse(phrase):
    code = ""
    for letter in phrase:
        code = code + morse_dict.me[letter]
    return code

def morse_decrypt(phrase):
    code = ""
    for letter in phrase:
        code = code + morse_dict.md[letter]
    return code

x = str(input("Enter Command: "))

if x=="Encryption":
    y = str(input("Encryption Method: "))
    z = str(input("Enter message: "))
    if y=="Caeser Cipher":
        print(caeser(z))
    elif y=="Morse":
        print(morse(z))
    else:
        print("Invalid encryption method")
elif x=="Decryption":
    v = str(input("Decryption Method: "))
    w = str(input("Enter message: "))
    if v=="Caeser Cipher":
        print(caeser_decrypt(w))
    elif v=="Morse":
        print(morse_decrypt(w))
    else:
        print("Invalid decryption method")

else:
    print("Invalid Command")