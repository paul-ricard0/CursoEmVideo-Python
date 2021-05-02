kmp = int(input('Quantos km vc percorreu: '))
dias = int(input('Quantos dias vc ficou com o carro: '))

preco = (60 * dias) + (kmp * 0.15)

print('Com {}km percorridos e {} dias com o carro \nO totala  se pagar é de {:.2f}$'.format(kmp, dias, preco))
