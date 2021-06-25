num = total = qtd = 0
print('DIGITE [999] para parar')
while(num != 999 ):
    total += num

    if num != 0:
        qtd += 1
    num = int(input('Entre com um número : '))

print('~'*30 + '\nVc digitou {} números \nA soma desses números é igual a {}\n'.format(qtd, total) + '~'*30)
