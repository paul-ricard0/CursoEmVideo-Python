#Programa que simula como um local de saque que só tme notas de 50, 20, 10 e 1

print('='*30 + '\n{:^30}\n'.format('BANCO PR') + '='*30)

valorTotal = int(input('Qual valor vc deseja sacar? R$'))

nota = 50
totalNota = 0

while True:

    if valorTotal >= nota: #Aqui vou ir diminuindo no valor total a quantidade da nota e contanto quasta notas eu tirei
        valorTotal -= nota #Faço isso até o valor total ser menor que o valor da nota para deoius pular no else
        totalNota += 1
    else:
        if totalNota > 0:                               #Para não printar quando não usar nenhuma daquela nota (tipo se vai para nota vinte e o valor total ta 10 e acabo sem usar nenhuma do 20 e pulo para 10 para ai sim usar ela)
            print(f'Total de {totalNota} de R${nota}')  #Depois do valor da nota ser maior que o valor total então eu mostro essa quantidade notas que usei
        
        if nota == 50:     #Aqui é onde eu troco o valor da nota
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1

        totalNota = 0

        if valorTotal == 0: #Quando o valor total for 0 eu finalizo o loop
            break

print('='*30 + '\n{:^30}\n'.format('VOLTE SEMPRE!!!!!!') + '='*30)  
