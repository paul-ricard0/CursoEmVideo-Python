num = total = qtd = maior = menor = 0 

next = 'S'
while(next in 'Ss' ):

    num = int(input('Entre com um número : '))
    qtd += 1
    total += num

    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    next = str(input('Quer continuar? [S/N]'.upper().strip()))

md = total / qtd

print('~'*30 + 'Maior: {} \nMenor: {:.2f} \nMédia: {}'.format(maior, menor, md, qtd) + '~'*30 )