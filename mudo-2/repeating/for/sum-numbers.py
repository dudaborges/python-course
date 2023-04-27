n1 = int(input('Enter the number one'))
n2 = int(input('Enter the number two'))
n3 = int(input('Enter the number three'))
n4 = int(input('Enter the number four'))
n5 = int(input('Enter the number five'))
n6 = int(input('Enter the number six'))
num = [n1, n2, n3, n4, n5, n6]
sumNum = 0
for n in num:
    if n % 2 == 0:
        sumNum += n
print(sumNum)
