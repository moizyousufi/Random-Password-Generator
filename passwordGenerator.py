import random

# This function utilizes recursion to eventually induce a valid response from the user for whether there should be letters in the password
def lettersResend(letters):
    if letters == "Y":
        print("You selected to have letters")
        letterTruth = True
    elif letters == "N":
        print("You selected to have no letters")
        letterTruth = False
    else:
        print("Your input is invalid ")
        letters = input("Would you like to have letters in your password (Y/N)? ")
        # This is where the recursion occurs in the scenario that the user continues giving invalid responses
        lettersResend(letters)

# This function utilizes recursion to eventually induce a valid response from the user for whether there should be numbers in the password
def numbersResend(numbers):
    if numbers == "Y":
        print("You selected to have numbers")
        numberTruth = True
    elif numbers == "N":
        print("You selected to have no numbers")
        numberTruth = False
    else:
        print("Your input is invalid ")
        numbers = input("Would you like to have numbers in your password (Y/N)? ")
        # This is where the recursion occurs in the scenario that the user continues giving invalid responses
        numbersResend(numbers)
        
# This function utilizes recursion to eventually induce a valid response from the user for whether there should be symbols in the password
def symbolsResend(symbols):
    if symbols == "Y":
        print("You selected to have symbols")
        symbolTruth = True
    elif symbols == "N":
        print("You selected to have no symbols")
        symbolTruth = False
    else:
        print("Your input is invalid ")
        symbols = input("Would you like to have symbols in your password (Y/N)? ")
        # This is where the recursion occurs in the scenario that the user continues giving invalid responses
        symbolsResend(symbols)

# This function occurs whenever symbolTruth == True and numberTruth == False and letterTruth == False
# This function intends to create a random number that fits in the ASCII range that symbols occur under
# Recursion occurs until an appropriate number is created
def symbolsOnly():
    x = (round(random.random() * 31 + 33))
    if x < 48 or x > 57:
        return x
    else:            
        x = symbolsOnly()
        return x

# This function occurs whenever symbolTruth == False and numberTruth == True and letterTruth == True
# This function intends to create a random number that fits in the ASCII range that numbers and letters occur under
# Recursion occurs until an appropriate number is created
def numLettersOnly():
    x = round(random.random() * 89) + 48
    if (x > 47 and x < 58) or (x > 64 and x < 91) or (x > 96 and x < 123):
        return x
    else:
        x = numLettersOnly()
        return x

# This function occurs whenever symbolTruth == False and numberTruth == False and letterTruth == True
# This function intends to create a random number that fits in the ASCII range that letters occur under
# Recursion occurs until an appropriate number is created
def lettersOnly():
    x = round(random.random() * 57) + 65
    if (x > 64 and x < 91) or (x > 96 and x < 123):
        return x
    else:            
        x = lettersOnly()
        return x

# This function converts an array of individual characters into a single string
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

# function to begin the program
# allows for easy restart of program
def begin():
    # initializes the truths to be false
    letterTruth = False
    numberTruth = False
    symbolTruth = False
    
    # collects user input over how many characters they would desire for a password
    length = input("How long should the password be? ")
    
    # checks to confirm that user input is a positive, nonzero number and not a character nor a negative/zero number
    try:
        val = int(length)
        print("Input is an integer number. Number = ", val)
        if val > 0:
            length = val
        else:
            print("No.. input is invalid. Try again")
            begin()    
    except ValueError:
        # int() function gives ValueError when string cannot be converted to a number
        # this error allows for program to confirm numerical input while efficiently converting the input into a number
        print("No.. input is invalid. Try again")
        begin()
    
    # lengthCount is initalized as 0 because it is later used as an iterative variable
    # lengthCount will iterate until it is equal to length input variable
    lengthCount = 0

    # password customization features for user to input
    letters = input("Would you like to have letters in your password (Y/N)? ").upper()      #.upper() allows for lowercase input to be the same
    # lettersResend() function defined to confirm valid input
    lettersResend(letters)

    numbers = input("Would you like to have numbers in your password (Y/N)? ").upper()
    # numbersResend() function defined to confirm valid input
    numbersResend(numbers)

    symbols = input("Would you like to have symbols in your password (Y/N)? ").upper()
    # symbolsResend() function defined to confirm valid input
    symbolsResend(symbols)

    # sets truth variables based on user input
    # change is only made if user inputs "Y" or "y"
    if letters == "Y":
        letterTruth = True
    if numbers == "Y":
        numberTruth = True
    if symbols == "Y":
        symbolTruth = True

    # array of individual characters is made as password
    password = []

    if (not letterTruth) and (not numberTruth ) and (not symbolTruth):
        # scenario that user sets all truths to false
        # system asks user if they would like to restart program or quit
        print("You cannot have a password without letters, numbers, or symbols")
        rebegin = input("Would you like to reset this program (Y/N)? ").upper()
        if rebegin == "Y":
            begin()
        elif rebegin == "N":
            exit()
        else:
            print("Invalid input. I'll just restart the program I guess lol")
            begin()
    elif letterTruth:
        if numberTruth:
            if symbolTruth:
                # scenario that all truths are met
                while lengthCount < length:         # compares lengthCount (starting at 0) to user input
                    x = round(random.random() * 89) + 33
                    # chr() function is used to convert number --> ASCII character
                    # password array appends as a loop until user-specified length is met
                    password.append(chr(x))
                    lengthCount += 1        # lengthCount adds by one until exact amount of array appends are met
            else:
                # scenario that letterTruth and numberTruth are met
                while lengthCount < length:
                    x = round(random.random() * 74) + 48
                    if (x > 47 and x < 58) or (x > 64 and x < 91) or (x > 96 and x < 123):
                        password.append(chr(x))
                    else:
                        x = numLettersOnly()
                        password.append(chr(x))
                    lengthCount += 1
        else:
            if symbolTruth:
                # scenario that letterTruth and symbolTruth are met
                while lengthCount < length:
                    x = round(random.random() * 93) + 33
                    password.append(chr(x))
                    lengthCount += 1
            else:
                # scenario that only letterTruth is met
                while lengthCount < length:
                    x = round(random.random() * 57) + 65
                    if (x > 64 and x < 91) or (x > 96 and x < 123):
                        password.append(chr(x))
                    else:            
                        x = lettersOnly()
                        password.append(chr(x))
                    lengthCount += 1
        # listToString(x) function converts array of characters to a string
        print("Your password shall be: " + listToString(password))
    elif numberTruth:
        if symbolTruth:
            # scenario that numberTruth and symbolTruth are met
            while lengthCount < length:
                x = round(random.random() * 31) + 33
                password.append(chr(x))
                lengthCount += 1
        else:
            # scenario that only numberTruth is met
            while lengthCount < length:
                x = round(random.random() * 9) + 48
                password.append(chr(x))
                lengthCount += 1
        print("Your password shall be: " + listToString(password))
    elif symbolTruth:
        # scenario that only symbolTruth is met
        while lengthCount < length:
            x = round(random.random() * 31)  + 33
            if x < 48 or x > 57:
                password.append(chr(x))
            else:            
                x = symbolsOnly()
                password.append(chr(x))
            lengthCount += 1
        print("Your password shall be: " + listToString(password))

# starts up the program
begin()




