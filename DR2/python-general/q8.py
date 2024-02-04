"""
Usando a biblioteca 'pygame', escreva um programa que desenha um botão (círculo) com o texto “clique” sobre ele na parte superior da tela. Quando o botão for clicado, ele deve chamar uma função que desenha um retângulo em uma posição aleatória na tela. Caso um retângulo apareça na mesma posição que um já existente, ambos devem ser eliminados.
"""

import pygame
from pygame_config import *
from pygame_functions import *
import random

# definicao circulo
raio_circulo = 50
centro_x_circulo = LARGURA_TELA / 2
centro_y_circulo = raio_circulo + 10
desenha_circulo(centro_x_circulo, centro_y_circulo, raio_circulo, "blue")

# definicao button
lado_button = math.sqrt(2) * raio_circulo
left_button = centro_x_circulo - (lado_button / 2)
top_button = centro_y_circulo - (lado_button / 2)
button = pygame.Rect(left_button, top_button, lado_button, lado_button)

escreve_mensagem("Clique aqui", centro_x_circulo, centro_y_circulo)

lista_quadrados = []
lado_quadrado = 50

terminou = False 
while not terminou:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (button.collidepoint(x, y)):
                lista_quadrados = desenha_retangulo_aleatorio(lista_quadrados)
                

    desenha_circulo(centro_x_circulo, centro_y_circulo, raio_circulo, "blue")
    escreve_mensagem("Clique aqui", centro_x_circulo, centro_y_circulo)
    
    clock.tick(50)
    pygame.display.update()  
    
    
pygame.display.quit()
pygame.quit()




