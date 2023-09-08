count = 0

while True: 
    num = int(input("Enter the numer 999 to stop: "))
    if num == 999:
        break
    count += 1

print(f"You insert {count} numbers")