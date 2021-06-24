idade = int(input('Qual a sua idade?'))

if idade < 12:
    print('Vc tem idade de uma criança')
elif idade < 18:
    print('Vc tem idade de um adolescente')
elif idade < 60:
    print('Vc tem idade de um adulto')
else:
    print('Vc tem idade de um idoso')