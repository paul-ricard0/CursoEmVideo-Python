import pygame

pygame.mixer.init() #Iniciando a biblioteca pygame

pygame.mixer.music.load('maginkz.mp3') 
                        # fazendo uso do mixer 
                        # para utilizar a opção de 
                        # carregar o arquivo que 
                        # eu desejo

a = input('O que vc deseja? ')

pygame.mixer.music.play()
pygame.event.wait()