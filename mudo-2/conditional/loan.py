homeValue = float(input('house value: R$'))
salary = float(input('buyers salary: R$'))
finYears = int(input('How many years of financing? '))
instMonth = round((homeValue / finYears) / 12, 2)
print('To pay off a house worth R${} in {} years, the installment will be R${}'.format(homeValue, finYears, instMonth))
if( salary * 0.3) <= instMonth:
    print('loan DENIED!')
else:
    print('loan accepted!')
