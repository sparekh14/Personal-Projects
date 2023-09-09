from random import *

seed(1)
gameCount = 1
compWins = 0
userWins = 0
gameReplay = True

games = int(input("How many games do you want to play (Enter an odd number): "))

if games % 2 == 0:
    print("You have entered an invalid value. Clearly you could not read the instructions. Please rerun the program to try again")
while gameReplay == True:
    while gameCount <= games:
        for i in range(games):
            print("\nGame #", gameCount)
            print("1. Rock\n2. Paper\n3. Scissors")
            userChoice = int(input("Enter your desired choice: "))
            compNum = randint(1, 3)
            if userChoice == compNum:
                print("\nDraw")
            elif userChoice == 1:
                if compNum == 2:
                    print("\nComputer wins!")
                    compWins += 1
                    gameCount += 1
                else:
                    print("\nYou win!")
                    userWins += 1
                    gameCount += 1
            elif userChoice == 2:
                if compNum == 1:
                    print("\nYou win!")
                    userWins += 1
                    gameCount += 1
                else:
                    print("\nComputer wins!")
                    compWins += 1
                    gameCount += 1
            else:
                if compNum == 1:
                    print("\nComputer wins!")
                    compWins += 1
                    gameCount += 1
                else:
                    print("\nYou win!")
                    userWins += 1
                    gameCount += 1
            print("Scoreboard")
            print("User wins: ", userWins)
            print("Computer wins: ", compWins)

        print("\n1. Yes\n2. No")
        userInput = int(input("Would you like to play again?"))
        if userInput != 1:
            gameReplay = False
            print("Thanks for playing!")