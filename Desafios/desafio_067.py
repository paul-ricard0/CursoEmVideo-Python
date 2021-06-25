
print('DIGITE UM NÚMERO [NEGATIVO] PARA FINALIZAR!')
f = 1
while f != 0:
    num = int(input('Entre com um número: '))
    x = 0

    print('=='*20)
    if num > 0:
        while x < 10:
            x += 1
            print('{} x {} = {}'.format(num, x, (num * x)))
    else:
        f = 0
        print('FIM DO PROGRAMA!!!!!!!!!')
    print('=='*20 + '\n')

