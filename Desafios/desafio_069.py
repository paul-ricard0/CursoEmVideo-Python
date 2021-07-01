c='S'
cFI = cM = cIdade = 0
while c in 'Ss':
    print('     CADASTRE UMA PESSOA')
    print('*'*30)
   
    idade = int(input('Qual a idade? '))
    
    while True:
        sexo = str(input('Qual o Sexo [M/F]? ').strip().upper())[0]
        if sexo in 'MmFf':
            break

    if idade > 18:
        cIdade += 1
    if sexo in 'Mm':
        cM += 1
    if sexo in 'Ff' and idade < 20:
        cFI += 1

    print('-'*30)
    c = input('QUER CADASTRAR MAIS PESSOAS [S/N]? ').strip().upper()[0]
    print('-'*30)    

print('\n===== FIM DO PROGRAMA =====')
print(f'\nTotal de pessoas com mais de 18 anos: {cIdade}')
print(f'Ao todo temos {cM} homens cadastrados')
print(f'E temos {cFI} mulheres com menos de 20 anos\n')