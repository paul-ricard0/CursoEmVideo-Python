val = input('digite algo: ')
print(type(val))
print('É tudo maiúsculo:', val.isupper())
print('É tudo minúsculo:', val.islower())
print('É um string:', val.isalpha())
print('É um número:', val.isnumeric())
print('É um alnum:', val.isalnum())
print('É um espaço:', val.isspace())
