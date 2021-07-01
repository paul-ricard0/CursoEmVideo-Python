nomeMenor = ' '
key = totGasto = totmil = 0

print('     COMPRE O PRODUTO')
print('*'*30)
while True:

    nomeProduto = str(input('Qual nome do produtor? '))
    preco = float(input('Preço: R$'))

    totGasto += preco

    if preco > 1000:
        totmil += 1
    
    if key == 0 or preco < menorPreco: 
        menorPreco = preco
        nomeMenor = nomeProduto
        key += 1


    print('x'*30)
    while fim not in 'SsNn':
        fim = input('Quer continuar [S/N]? ').strip().upper()[0]
    if fim == 'Nn':
        break

print('\n===== FIM DO PROGRAMA =====')
print(f'Total gasto: {totGasto:.2f}')
print(f'Total que custa mais de R$1000: {totmil}')
print(f'O produto mais barato foi {nomeMenor} que custa {menorPreco}')