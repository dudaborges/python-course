num = int(input('Enter a number to check if it is a prime number: '))
numArray = []
for n in range(1, num+1):
    if(num % n == 0):
        print('\033[1;31;40m{}\33[m'.format(n), end=' ')
        numArray.append(n)
    else:
        print('\033[1;33;40m{}\33[m'.format(n), end=' ')

print('\nO número {} foi dívisivel {} vezes'.format(num, len(numArray)))
if(len(numArray) == 2):
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é primo')
