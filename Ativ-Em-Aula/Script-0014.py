n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('A sua média foi {:.2}'.format(m))

if m >= 6:
    print('Sua nota foi boa!')
else:
    print('Sua média foi ruim!')