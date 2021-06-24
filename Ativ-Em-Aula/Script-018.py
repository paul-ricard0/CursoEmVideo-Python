A = int(input('Começa em qual número? '))
B = int(input('Escrever até qual número? '))
C = int(input('Quer que pule de quantos em quantos números? '))

for c in range(A, B + 1, C):
    print(c)
print('FIM')