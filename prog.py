password = input("Input a password: ")
new_pass = ""
for char in password[:-(len(password)):-1].lower():
    if char == "a":
        new_pass += "#"
    elif char == "e":
        new_pass += "5"
    elif char == "i":
        new_pass += "b"
    elif char == "o":
        new_pass += "&"
    elif char == "u":
        new_pass += "^"
    elif char == "b":
        new_pass += "7"
    elif char == "c":
        new_pass += "("
    elif char == "d":
        new_pass += "H"
    elif char == "f":
        new_pass += "#"
    elif char == "g":
        new_pass += "%"
    elif char == "h":
        new_pass += "i"
    elif char == "j":
        new_pass += "!"
    elif char == "k":
        new_pass += "3"
    elif char == "l":
        new_pass += "2"
    elif char == "m":
        new_pass += "F"
    elif char == "n":
        new_pass += "N"
    elif char == "p":
        new_pass += "a"
    elif char == "q":
        new_pass += "q"
    elif char == "r":
        new_pass += "S"
    elif char == "s":
        new_pass += "}"
    elif char == "t":
        new_pass += "x"
    elif char == "v":
        new_pass += "U"
    elif char == "w":
        new_pass += "9"
    elif char == "x":
        new_pass += "x"
    elif char == "y":
        new_pass += "@"
    elif char == "z":
        new_pass += "t"
    elif char == "1":
        new_pass += "d"
    elif char == "2":
        new_pass += "4"
    elif char == "3":
        new_pass += ":"
    elif char == "4":
        new_pass += "'"
    elif char == "5":
        new_pass += "1"
    elif char == "6":
        new_pass += "*"
    elif char == "7":
        new_pass += ")"
    elif char == "8":
        new_pass += "["
    elif char == "9":
        new_pass += "]"
    elif char == "0":
        new_pass += "|"
new_pass += password[0].upper()
print(new_pass)
