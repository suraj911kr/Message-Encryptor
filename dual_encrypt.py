def caeser(phrase):
    translation = ""
    for letter in phrase:
        if letter in "a":
            translation = translation + "d"
        elif letter in "b":
            translation = translation + "e"
        elif letter in "c":
            translation = translation + "f"
        elif letter in "d":
            translation = translation + "g"
        elif letter in "e":
            translation = translation + "h"
        elif letter in "f":
            translation = translation + "i"
        elif letter in "g":
            translation = translation + "j"
        elif letter in "h":
            translation = translation + "k"
        elif letter in "i":
            translation = translation + "l"
        elif letter in "j":
            translation = translation + "m"
        elif letter in "k":
            translation = translation + "n"
        elif letter in "l":
            translation = translation + "o"
        elif letter in "m":
            translation = translation + "p"
        elif letter in "n":
            translation = translation + "q"
        elif letter in "o":
            translation = translation + "r"
        elif letter in "p":
            translation = translation + "s"
        elif letter in "q":
            translation = translation + "t"
        elif letter in "r":
            translation = translation + "u"
        elif letter in "s":
            translation = translation + "v"
        elif letter in "t":
            translation = translation + "w"
        elif letter in "u":
            translation = translation + "x"
        elif letter in "v":
            translation = translation + "y"
        elif letter in "w":
            translation = translation + "z"
        elif letter in "x":
            translation = translation + "a"
        elif letter in "y":
            translation = translation + "b"
        elif letter in "z":
            translation = translation + "c"
        else:
            translation = translation + letter
    return translation

def caeser_decrypt(phrase):
    translation = ""
    for letter in phrase:
        if letter in "d":
            translation = translation + "a"
        elif letter in "e":
            translation = translation + "b"
        elif letter in "f":
            translation = translation + "c"
        elif letter in "g":
            translation = translation + "d"
        elif letter in "h":
            translation = translation + "e"
        elif letter in "i":
            translation = translation + "f"
        elif letter in "j":
            translation = translation + "g"
        elif letter in "k":
            translation = translation + "h"
        elif letter in "l":
            translation = translation + "i"
        elif letter in "m":
            translation = translation + "j"
        elif letter in "n":
            translation = translation + "k"
        elif letter in "o":
            translation = translation + "l"
        elif letter in "p":
            translation = translation + "m"
        elif letter in "q":
            translation = translation + "n"
        elif letter in "r":
            translation = translation + "o"
        elif letter in "s":
            translation = translation + "p"
        elif letter in "t":
            translation = translation + "q"
        elif letter in "u":
            translation = translation + "r"
        elif letter in "v":
            translation = translation + "s"
        elif letter in "w":
            translation = translation + "t"
        elif letter in "x":
            translation = translation + "u"
        elif letter in "y":
            translation = translation + "v"
        elif letter in "z":
            translation = translation + "w"
        elif letter in "a":
            translation = translation + "x"
        elif letter in "b":
            translation = translation + "y"
        elif letter in "c":
            translation = translation + "z"
        elif letter in "5":
            translation = translation + "!"
        else:
            translation = translation + letter
    return translation

def morse(phrase):
    translation = ""
    for letter in phrase:
        if letter in "a":
            translation = translation + ".-"
        elif letter in "b":
            translation = translation + "-..."
        elif letter in "c":
            translation = translation + "-.-."
        elif letter in "d":
            translation = translation + "-.."
        elif letter in "e":
            translation = translation + "."
        elif letter in "f":
            translation = translation + "..-."
        elif letter in "g":
            translation = translation + "--."
        elif letter in "h":
            translation = translation + "...."
        elif letter in "i":
            translation = translation + ".."
        elif letter in "j":
            translation = translation + ".---"
        elif letter in "k":
            translation = translation + "-.-"
        elif letter in "l":
            translation = translation + ".-.."
        elif letter in "m":
            translation = translation + "--"
        elif letter in "n":
            translation = translation + "-."
        elif letter in "o":
            translation = translation + "---"
        elif letter in "p":
            translation = translation + ".--."
        elif letter in "q":
            translation = translation + "--.-"
        elif letter in "r":
            translation = translation + ".-."
        elif letter in "s":
            translation = translation + "..."
        elif letter in "t":
            translation = translation + "-"
        elif letter in "u":
            translation = translation + "..-"
        elif letter in "v":
            translation = translation + "...-"
        elif letter in "w":
            translation = translation + ".--"
        elif letter in "x":
            translation = translation + "-..-"
        elif letter in "y":
            translation = translation + "-.--"
        elif letter in "z":
            translation = translation + "--.."
        else:
            translation = translation + letter
    return translation

x = str(input("Enter Command: "))

if x=="Encryption":
    y = str(input("Encryption Method: "))
    z = str(input("Enter message: "))
    if y=="Caeser Cipher":
        print(caeser(z))
    elif y=="Morse":
        print(morse(z))
    else:
        print("Invalid method")
elif x=="Decryption":
    w = str(input("Enter message: "))
    print(caeser_decrypt(w))

else:
    print("Invalid Command")