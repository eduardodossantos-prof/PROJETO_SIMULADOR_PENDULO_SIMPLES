import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 1300
altura = 680

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pendulo Simulation')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()
        pygame.display.update()

        #DESENHANDO O TETO DO SIMULADOR
        pygame.draw.rect(
            tela, (150,75,0), (0, 0, 1300, 70)
        )
        #FIM DESENHANDO O TETO DO SIMULADOR

        #DESENHANDO A LINHA DO SIMULADOR
        pygame.draw.line(
            tela, (255,255,255), (400, 70), (400, 500), 6
        )
        #FIM DO DESENHO DA LINHA DO SIMULADOR

        #DESENHANDO O CIRCUITO DA MASSA ESFERICA DO PENDULO 
        pygame.draw.circle(
            tela, (255,255,255), (400,500), 50
        ) 
        #FIM DO DESENHO DA MASSA ESFERICA DO PENDULO

        #DESENHANDO A TABELA DE DADOS DO SIMULADOR
        pygame.draw.rect(
            tela, (255,255,255), (880, 100, 400, 450) 
        )
        #FIM DO DESENHAR A TABELA DE DADOS DO SIMULADOR

        #DESENHANDO A TABELA MANUAL DE DADOS
        pygame.draw.rect(
            tela, (255,255,255), (880, 570, 400, 80)
        )
        #FIM DO DESENHO DA TABELA MANUAL DE DADOS