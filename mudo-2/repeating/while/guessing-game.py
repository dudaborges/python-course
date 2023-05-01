from random import randint

print("Helo, Im your computer...")
print("I will think of a number from 1 to 10. Try to guess")
numUser = int(input("Enter the number: "))
numPC = randint(1, 10)
while numUser != numPC:
    if numUser < numPC:
        numUser = int(input("The number is bigger. Try again: "))
    else:
        numUser = int(input("The number is small. Try again: "))

print("\033[1;30;45mYOU'ARE RIGHT!\033[m")