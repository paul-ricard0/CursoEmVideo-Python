n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('A sua média foi {:.2}'.format(m))

print('Parabéns, sua nota foi boa' if m >= 6 else 'Sua nota não foi boa, estude mais!')
