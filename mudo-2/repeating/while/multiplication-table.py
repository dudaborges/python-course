count = 1
while True:
    num = int(input("Enter the numer: "))

    if num < 0:
        print("Exiting...")
        break

    while count <= 10:
        print(f'{num} x {count} = {num * count}')
        count += 1

    count = 1