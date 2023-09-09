x = int(input("How many values will you enter: "))

vals = []
phrases = []

for i in range(x):
    y = int(input("Enter a number: "))
    vals.append(y)

for j in range(x):
    b = (input("Enter a phrase: "))
    phrases.append(b)

vals_and_phrases = dict(zip(vals, phrases))
print(vals_and_phrases)