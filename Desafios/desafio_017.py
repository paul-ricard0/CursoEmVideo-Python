import math
Coposto = float(input('Entre com o cateto oposto do triangulo retângulo: '))
Cadjacente= float(input('Entre com o cateto adjasente: '))
hipotenusa = math.sqrt(math.pow(Coposto, 2) + math.pow(Cadjacente, 2))

print('O Cateto Oposto sendo {} e o Cateto Adjacente sendo {}, o valor da hipotenusa então é de {}'.format(Coposto, Cadjacente, hipotenusa))