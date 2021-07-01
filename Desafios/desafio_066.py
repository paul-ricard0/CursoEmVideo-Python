soma = cont = 0 
while True: 
    num = int(input('Digite um valor (999 para parar)'))
    if num == 999:
        break               #vai jogar o código para fora do loop, assim não vai somar o 999 e nem contar mais um número
    cont += 1 
    soma += num

print(f'A soma dos {cont} valores foi {soma}!')