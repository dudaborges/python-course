num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
option = 0
while option != 5:
    print('''    [1] Add
    [2] Multiplication
    [3] Bigger
    [4] New numbers 
    [5] Exit''')
    option = int(input("\033[1;32;40mWhat is your option?\33[m "))

    if option == 1:
        add = num1 + num2
        print(f"Result: {add}")
    elif option == 2:
        multi = num1 * num2
        print(f"Result: {multi}")
    elif option == 3:
        bigger = max(num1, num2)
        print(f"Result: {bigger}")
    elif option == 4:
        num1 = float(input("Enter the new first number: "))
        num2 = float(input("Enter the new second number: "))
    else:
        print("[ERROR] Try again")
