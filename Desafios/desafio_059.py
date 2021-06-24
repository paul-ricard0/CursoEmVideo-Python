x = 1
while x != 0:
    prt = 0
    x = 1

    print('\n ############################################ \n')
    val1 = float(input('Entre com o primeiro número: '))
    val2 = float(input('Entre com o segundo número: '))
    
    print('\n[1] Somar \n[2] Multiplicar \n[3] Qual Maior \n[4] Novos números \n[5] Sair do Programa')
    do = int(input('O que vc deseja fazer? '))

    if do == 1:
        val3 = val1 + val2
        op = 'SOMA'
        prt = 1
    elif do == 2:
        val3 = val1 * val2
        op = 'MULTIPLICSÇãO'
        prt = 1
    elif do == 3:
        if val1 > val2:
            val3 = val1
        else:
            val3 =val2
        prt = 3
    elif do == 4:
        prt = 4
    elif do == 5:
        print('Fim!!!')
        x = 0
        prt = 5
    else:
        print('!!!!!!!!!!! Número Invalido !!!!!!!!!!!!!!!!')

    if prt == 1:
        print('A {} dos números {:.2f} e {:.2f} => {:.2f}'.format(op, val1, val2, val3))
    elif prt == 3:
        print('O maior número entre {:.2f} e {:.2f} => {:.2f}'.format(val1, val2, val3))

    
   
        
