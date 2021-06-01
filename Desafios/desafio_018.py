import math
angulo = float(input('Entre com o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))# Estou pegando o Angulo convertendo para 
                                     # radianos (pq math.sin só funciona em radianos)
                                     # depos eu fiz o caulculo do seno com math.sin 

coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo de {:.2f} tem: \nO SENO igual a {:.2f} ' .format(angulo, seno))
print('O COSENO igual a {:.2f} \nA TANGENTE igual a {:.2f}'.format(coseno, tangente))