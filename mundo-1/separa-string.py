nome = input("Digite seu nome completo").strip()
separa = nome.split()
print(separa)
print('seu nome tem ', len(nome) - nome.count(' '), 'letras')