import random
print("------Insira o nome dos alunos que irão se apresentar e eu irei gerar uma lista ordenada aleatoriamente------")
aluno1 = input("Aluno 1: ")
aluno2 = input("Aluno 2: ")
aluno3 = input("Aluno3: ")
aluno4 = input("Aluno4: ")
aluno5 = input("Aluno5: ")

alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
random.shuffle(alunos)
for aluno in alunos:
    print(aluno)