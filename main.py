run = True
while run:
    at = False
    dot = False
    space = False
    atPos = 0
    dotPos = 0
    email = input("enter email: ")
    for i in range(len(email)):
        if email[i] == "@":
            at = True
            atPos = i
        if email[i] == ".":
            dot = True
            dotPos = i
        if email[i] == " ":
            space = True
    if at == True and dot == True and space == False:
        if atPos < dotPos:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")




