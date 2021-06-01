from random import shuffle 

aluno1 = input('Entre com o número do primeiro aluno: ')
aluno2 = input('Entre com o número do segundo  aluno: ')
aluno3 = input('Entre com o número do terceiro aluno: ')
aluno4 = input('Entre com o número do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista) #shuffle significa embaralhar algo

print('A ordem de aprgesentação sorteada foi', lista)