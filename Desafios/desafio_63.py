qtd = int(input('Entre com a quantidade de números que vc deseja ver da Sequência de Fibonacci: '))

n1 = 0
n2 = 1

if qtd >= 1:
    print('{} -> '.format(n1), end='')

    if qtd >= 2:
        print('{} -> '.format(n2), end='')


cont = 3
while cont <= qtd: 
    n3 = n1 + n2
    print('{} -> '.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1

print('FIM!!!')