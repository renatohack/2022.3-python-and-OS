"""
Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta), toda vez que a tecla espaço for pressionada ou o botão direito for clicado.
"""

import pygame
from pygame_config import *
from pygame_functions import *
import random

lado_quadrado = 50

terminou = False 
while not terminou:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                left_quadrado = randint(0, LARGURA_TELA)
                top_quadrado = randint(0, ALTURA_TELA)
                desenha_quadrado(left_quadrado, top_quadrado, lado_quadrado, "yellow")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                left_quadrado = randint(0, LARGURA_TELA)
                top_quadrado = randint(0, ALTURA_TELA)
                desenha_quadrado(left_quadrado, top_quadrado, lado_quadrado, "yellow")

    clock.tick(50)
    pygame.display.update()  
    
    
pygame.display.quit()
pygame.quit()




