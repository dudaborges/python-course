from math import hypot
# importa apenas a função que vamos usar no código: hypot"
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
hip = hypot(co, ca)
# calcula a hipotenusa apenas passando o cateto oposto e o adjacente
print("Hipotenusa = {:.2f}".format(hip))