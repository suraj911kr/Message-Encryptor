def translate(phrase):
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

print (translate(input("Enter your message to be encrypted: ")))
