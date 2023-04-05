import math

co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
hip = math.hypot(co, ca)
# calcula a hipotenusa apenas passando o cateto oposto e o adjacente
print("Hipotenusa = {:.2f}".format(hip))