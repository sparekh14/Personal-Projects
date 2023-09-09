from random import *

rolls = [1, 2, 3, 4, 5, 6]

x = input("Would you like to roll a dice: ")
x.upper()
while x != "NO":
  print("Your roll is: ", choice(rolls))
  print()
  x = input("Would you like to roll again: ")
  x = x.upper()
  if x == "NO":
    print("Thanks for rolling!!!")