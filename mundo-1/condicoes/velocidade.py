vel = int(input("Qual a velocidade do carro? "))
multa = (vel - 80) * 7
if(vel > 80):
    print("MULTADO! Você excedeu o limite  permitido que é de 80Km/h")
    print("Você deve pegar uma multa de R$", multa)
else:
    print("Tenha um bom dia! Dirija com segurança!")
