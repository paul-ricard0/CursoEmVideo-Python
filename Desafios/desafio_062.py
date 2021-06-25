termoP = int(input('entre com o primeiro termo: '))
razao = int(input('Entre com a razão dessa PA: '))

c = x = 0
mais = 1
roda = 10
while mais != 0:
    
    while c < roda:
        x = x + razao
        total = termoP + x
        print('{} ~> '.format(total), end='')
        c += 1
    
    print('PAUSA!')


















'''
t = 1
while t != 0:
    t = int(input('(DIGITE [0] para finalizar) \nQuer mostrar mais termos? '))
    
    if t != 0:
        c=0
        while c < t:
            x = x + razao
            total = termoP + x
            print('{} ~> '.format(total), end='')
            c += 1
'''


print('FIM!!!')