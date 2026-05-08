import pygame
import math

pygame.init()

LARGURA, ALTURA = 800, 600

tela_principal = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("OSPEND - Simulador de Pendulo Simples")
relogio = pygame.time.Clock()

BRANCO = (
    255,
    255,
    255
    )
CINZA = (
    150,
    150,
    150
    )
BLACK = (
    0,
    0,
    0
    )

#Calcula a posição onde o teto vai ficar preso.
origem_x, origem_y = LARGURA // 2, 100

comprimento = 300
angulo = math.radians(10)


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    relogio.tick(27) #Ela define a velocidade de execução do meu simulador que vem de python.time.clock()
    tela_principal.fill(BRANCO)

    #Calcula a posição onde a bolinha vai ficar.
    bolinha_x = origem_x + comprimento * math.sin(angulo)
    bolinha_y = origem_y + comprimento * math.cos(angulo)

    pygame.draw.line(
        tela_principal, 
        BLACK , 
        (origem_x - 1000, origem_y - 100), 
        (origem_x + 1000, origem_y - 100), 
        100
    )
    pygame.draw.line(
        tela_principal,
        BLACK,
        (origem_x - 10, origem_y - 50), 
        (bolinha_x - 60, bolinha_y),
        3
    )
    pygame.draw.circle(
        tela_principal,
        CINZA, 
        (bolinha_x - 60, bolinha_y),
        60, 
        100
    )
    pygame.display.update() #atualiza a tela a dentro do loop

pygame.quit()
