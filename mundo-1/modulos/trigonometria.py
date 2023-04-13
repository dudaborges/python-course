import math
ang = float(input("Insira o ângulo: "))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print("Seno = ", round(seno, 2), "Cosseno = ", round(cosseno, 2), "Tangente = ", round(tangente, 2))