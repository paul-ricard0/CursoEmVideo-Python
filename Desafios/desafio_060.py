import time
num = int(input('Entre com um número: '))
total = num
fat = 1

print('O fatorial de {} é...'.format(num))
time.sleep(1)
for c in range(1, num+1):
    print('{}'.format(c), end='') #para aparecer todos os números do fatorial
    print(' x ' if total > 1 else ' = ', end='') # para adicionar o X e o = no local certo
    fat = fat * total 
    total = total - 1

print('{}'.format(fat))