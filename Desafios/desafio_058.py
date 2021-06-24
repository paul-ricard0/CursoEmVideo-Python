import random as rd

x = rd.randint(0,10)
palpite = 1

res = int(input('O robô escolheu um número entre 0 a 10 \nQual número esse robô escolheu?'))

while x != res:
    print('!!!!! RESPOSTA ERRADA !!!!!')
    res = int(input('Tente novamente: '))
    palpite += 1

print('Vc precisou exatamente de {} tentativas'.format(palpite))
