termoP = int(input('entre com o primeiro termo: '))
razao = int(input('Entre com a razão dessa PA: '))
c=0
x=0

while c < 10:
    
    print('{} ~> '.format(x), end='')
    x = x + razao
    c += 1

print('FIM!!!')
