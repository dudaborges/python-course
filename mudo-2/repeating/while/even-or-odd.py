from random import randint
print('=-'*30)
print(f'\033[1;30;43m{'EVEN OR ODD GAME!':^60}\33[m')
print('=-'*30)

while True:
    num = int(input("Enter the number: "))
    even_or_odd = str(input("Even or odd? [E/O]")).upper().strip()

    random_num = randint(1,10)
    sum = num + random_num

    print(f'You played the number {num} and computer the {random_num}. Sum total: {sum}')
    if (sum % 2 == 0 and even_or_odd == 'E') or (sum % 2 != 0 and even_or_odd == 'O') :
        print(f"\033[1;32;42m{'You won the game!':^60}\33[m")
    else:
        print(f'\033[1;34;41mGAME OVER {'.' * 10}\33[m')
        break



