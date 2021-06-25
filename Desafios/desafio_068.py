print('='*30)
print('     JOGO DE PAR OU ÍMPAR')
print('='*30)

import random as rd

lw = 'w'
cont=0
while lw == 'w':
    val = int(input('Entre com o valor: '))
    pi = str(input('Par ou ímpar [P/I] ? ').strip().upper())

    valpc = rd.randrange(1, 10)
    total = val + valpc
    print('\nVc jogou {} e o computador jogou {}, total = {}'.format(val, valpc, total))
    
    print('='*30)
    if pi in 'Pp':   
        if (total%2) == 0:
            print('You wiinn!!!')
            cont += 1
        else:
            print("You LOSSEEER!!")
            print('Vc venceu {} vezes'.format(cont))
            lw = 'l'
    if pi in 'Ii':
        if (total%2) == 0:
            print("You LOSSEEER!!")
            print('Vc venceu {} vezes'.format(cont))
            lw = 'l'
        else:
            print('You wiinn!!!')
            cont += 1
    print('='*30)


