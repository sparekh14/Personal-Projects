import random

print("Guess the Word Game")

words = ["computer", "programming", "desktop", "python", "keyboard"]

chosenWord = random.choice(words)

guesses = ''
tries = 15

print(chosenWord)
while tries > 0:
    failed = 0
    for char in chosenWord:
        if char in guesses:
            print(char, end = ' ')
        else:
            print('_', end = ' ')
            failed += 1

    if failed == 0:
        print("\n\nYou win")
        print("The word is: " + chosenWord)
        break

    guess = input("\nEnter a character: ")

    guesses += guess

    if guess not in chosenWord:
        tries -= 1
        print("Wrong")
        if tries == 0:
            print("You lose!")
            print("The correct word was " + chosenWord)
            break
        print("You have " + str(tries) + " tries left")