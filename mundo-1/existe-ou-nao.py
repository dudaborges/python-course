print("LISTA DE APROVADOS")
nomes = " 1 - Maria Eduarda \n 2 - Jessica \n 3 - Debora \n 4 - Igor \n 5 - Stafani \n 6 - Yan \n 7 - Julia \n 8 - Pedro \n 9 - Ricardo \n 10 - Emelly \n"
print(nomes)
seuNome = input("Procure pelo seu nome e veja se esá aprovado: ")
if(seuNome in nomes):
    print("Seu nome está na lista, parabéns! APROVADO")
else:
    print("Não encontramos seu nome na lista, sinto muito... REPROVADO")



