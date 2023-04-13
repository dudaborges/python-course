from random import randint
from time import sleep
print('=' * 60)
print("Vou pensar em um número entre 0 e 5. Tente Adivinhar...")
print('=' * 60)
num = int(input('Em que número eu pensei? '))
print("| PROCESSANDO... |")
sleep(2)
numMaq = randint(0, 5)
if(numMaq == num):
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número', numMaq, 'e não no', num)