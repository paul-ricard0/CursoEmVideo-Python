c = 'S'
ttgasto = qtprodutos = menorPreco = qtd1000 = 0

while c in 'Ss':
    print('     COMPRE O PRODUTO')
    print('*'*30)

    nomeProduto = str(input('Qual nome do produtor? '))
    preco = float(input('Qual preco do produto? '))

    if ttgasto == 0:
        menorProduto = nomeProduto 
    if preco <= menorPreco and ttgasto != 0:
        menorProduto = nomeProduto

    ttgasto += preco
    if preco < 1000:
        qtd1000 += 1

    print('-'*30)
    c = input('QUER CADASTRAR MAIS PESSOAS [S/N]? ').strip().upper()
    print('-'*30)   


print('\n===== FIM DO PROGRAMA =====')
print('Total gasto: {}'.format(ttgasto))
print('Quantos custam mais de R$1000: {}'.format(qtd1000))
print('O produto mais barato foi: {}'.format(nomeProduto))