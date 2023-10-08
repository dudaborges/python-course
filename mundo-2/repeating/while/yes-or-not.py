option = ''
soma = 0
count = 0

while option != 'n':
    num = float(input("Enter the number: "))
    soma += num

    option = str(input("Do you want continue? S/N ")).lower().strip()
    if option != 's' and option != 'n':
        print("Invalid option! Try again")

    count += 1

print(count)
print(soma)
print(f"You entered {count} numbers")
print(f"The average of the numbers gives {soma / count}")