nome = str(input('Qual seu nome? ')).strip

print("Em maiúsculo:  " + nome.upper())
print("Em minúsculo:  " + nome.lower())

sem = len(nome) - nome.count(' ')
print("Total de letras sem espaço:  ".format(sem))