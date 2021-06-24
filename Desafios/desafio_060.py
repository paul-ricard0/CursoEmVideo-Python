num = int(input('Entre com um número: '))
total = num
fat = 1
for c in range(1, num+1):
    fat = fat * total 
    total = total - 1

print('O fatorial de {}! é {}'.format(num, fat))