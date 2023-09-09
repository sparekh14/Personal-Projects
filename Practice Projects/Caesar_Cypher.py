phrase = input("Enter your word or phrase: ")
key = int(input("Enter your key: "))

result = ""

for i in range(len(phrase)):
    char = phrase[i]
    if char.isupper():
        result += chr((ord(char) + key - 65) % 26 + 65)
    else:
        result += chr((ord(char) + key - 97) % 26 + 97)

print(result)