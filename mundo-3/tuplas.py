# tuplas são imutáveis
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

# pelo index
print('2 ', lanche[2])

# pega do elemento até o último
print('1: ', lanche[1:])

# pega do início até o elemento
print(':1', lanche[:3])

# último elemento
print('-1 ', lanche[-1])

# pega pelo fatiamento
print('0:2', lanche[0:1])

print(f'os dois últimos {lanche[-2:]}')

print(f'os dois primeitos {lanche[:2]}')

for l in lanche:
    print(l)

# ou
for i in range(0, len(lanche)):
    print(lanche[i])

# para apagar uma tupla inteira: del(nome_tupla)
