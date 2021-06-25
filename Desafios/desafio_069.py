c='S'
cFI = cM = cIdade = 0
while c in 'Ss':
    print('     CADASTRE UMA PESSOA')
    print('*'*30)
   
    idade = int(input('Qual a idade? '))
    x=1
    while(x==1):
        sexo = str(input('Qual o Sexo [M/F]? ').strip().upper())
        if sexo in 'MmFf':
            x = 0

    if idade > 18:
        cIdade += 1
    if sexo in 'Mm':
        cM += 1
    if sexo in 'Ff' and idade < 20:
        cFI += 1

    print('-'*30)
    c = input('QUER CADASTRAR MAIS PESSOAS [S/N]? ').strip().upper()
    print('-'*30)    

print('\n===== FIM DO PROGRAMA =====')
print('Total de pessoas com mais de 18 anos: {}'.format(cIdade))
print('Ao todo temos {} homens cadastrados'.format(cM))
print('E temos {} mulheres com menos de 20 anos'.format(cFI))