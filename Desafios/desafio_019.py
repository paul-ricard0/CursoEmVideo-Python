import random

a1 = input('Entre com o número do primeiro aluno: ')
b2 = input('Entre com o número do segundo  aluno: ')
c3 = input('Entre com o número do terceiro aluno: ')
d4 = input('Entre com o número do quarto aluno: ')
lista = [a1, b2, c3, d4]
escolhido = random.choice(lista)

print('O aluno sorteado foi', escolhido)