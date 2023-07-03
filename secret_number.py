#Secret number game.
#Import OS for use in clearing screen.
import os

#Welcome screen.

#Create loop to run the guessing game.
while True:

    #Call OS with clear screen to clear screen each time.
    os.system('cls')

    #Welcome screen
    print("""
    +=============================+
    | Welcome to my game, muggle! |
    | Enter an integer number and |
    | guess what number I have.   |
    +=============================+
    """)
    #Use try to handle ValueError on anything other than integer.
    try:
    #Set secret number.
        secret_number = 777
    #Set guess with input.
        guess = int(input("Enter your guess: "))
    
    
    #If guess matches secret number - break, else continue loop
        if guess == secret_number:
            print("Well done muggle! You are now free.")
            break
        elif guess == 7:
            print("Getting closer...")
            input("Press enter to continue...")
        elif guess == 77:
            print("Getting closer...")
            input("Press enter to continue...")
        else:
            print("Ha ha! You're stuck in my loop!")
            input("Press enter to continue...")
    except ValueError:
        print("Value must an integer!!!")
        input("Press enter to continue...")

