termoP = int(input('entre com o primeiro termo: '))
razao = int(input('Entre com a razão dessa PA: '))
c=0
x=0

while c < 2:
    x = x + razao
    total = termoP + x
    print(total)
    c += 1

print('FIM!!!')
