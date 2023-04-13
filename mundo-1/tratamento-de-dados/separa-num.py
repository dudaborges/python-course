num = int(input('Digite um número'))
uni = num % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print('Unidade: ', uni, '\nDezena: ', dez, '\nCentena: ', cent, '\nMilhar: ', mil)