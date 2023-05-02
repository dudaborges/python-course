from functools import reduce
num = int(input("Enter the number to calculate factorial: "))
mainNum = num
factorial = [num]

while 1 not in factorial:
    num = num - 1
    factorial.append(num)

result = reduce(lambda x, y: x*y, factorial)
listFactorial = ' x '.join(str(numFactorial) for numFactorial in factorial)
print(f"Result: {mainNum}!: {listFactorial} = {result}")

