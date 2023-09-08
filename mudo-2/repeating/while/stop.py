count = -1 #começa com 1 negativo para não contabilizar o 999
num = 0

while num != 999:
    num = int(input("Enter the numer 999 to stop: "))
    count += 1

print(f"You insert {count} numbers")