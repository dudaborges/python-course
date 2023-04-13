name = input("Insira o seu nome: ")
print("Seu nome está correto? \n----", name, "----\n -> Digite 1 para alterar\n", "-> Digite 2 para continuar")
number = int(input(""))
if(number == 1):
    alteredName = input("Digite: ")
    name = name.replace(name, alteredName)
    print("Seja bem-vindo(a)", name)
elif(number == 2):
    print("Seja bem-vindo(a)", name)
else:
    print("ERROR")


