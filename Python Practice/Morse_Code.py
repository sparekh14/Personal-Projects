dot = "• "
dash = "▄▄ "

def toMorse(character):
    morse = ""
    if character == 'A':
        morse += (dot + dash + "  ")
    elif character == 'B':
        morse += (dash + dot + dot + dot + "  ")
    elif character == 'C':
        morse += (dash + dot + dash + dot + "  ")
    elif character == 'D':
        morse += (dash + dot + dot + "  ")
    elif character == 'E':
        morse += (dot + "  ")
    elif character == 'F':
        morse += (dot + dot + dash + dot + "  ")
    elif character == 'G':
        morse += (dash + dash + dot + "  ")
    elif character == 'H':
        morse += (dot + dot + dot + dot + "  ")
    elif character == 'I':
        morse += (dot + dot + "  ")
    elif character == 'J':
        morse += (dot + dash + dash + dash + "  ")
    elif character == 'K':
        morse += (dash + dot + dash + "  ")
    elif character == 'L':
        morse += (dot + dash + dot + dot + "  ")
    elif character == 'M':
        morse += (dash + dash + "  ")
    elif character == 'N':
        morse += (dash + dot + "  ")
    elif character == 'O':
        morse += (dash + dash + dash + "  ")
    elif character == 'P':
        morse += (dot + dash + dash + dot + "  ")
    elif character == 'Q':
        morse += (dash + dash + dot + dash + "  ")
    elif character == 'R':
        morse += (dot + dash + dot + "  ")
    elif character == 'S':
        morse += (dot + dot + dot + "  ")
    elif character == 'T':
        morse += (dash + "  ")
    elif character == 'U':
        morse += (dot + dot + dash + "  ")
    elif character == 'V':
        morse += (dot + dot + dot + dash + "  ")
    elif character == 'W':
        morse += (dot + dash + dash + "  ")
    elif character == 'X':
        morse += (dash + dot + dot + dash + "  ")
    elif character == 'Y':
        morse += (dash + dot + dash + dash + "  ")
    elif character == 'Z':
        morse += (dash + dash + dot + dot + "  ")
    elif character == ' ':
        morse += ("    ")
    return morse

phrase = input("Enter your word or phrase: ")
upperPhrase = phrase.upper()
print(upperPhrase)

result = ""

for i in range(len(upperPhrase)):
    result += toMorse(upperPhrase[i])

print(result)