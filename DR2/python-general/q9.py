"""
Usando o código anterior, escreva um novo programa que, quando as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas, ele movimente o círculo com o texto “clique” nas direções corretas. Caso colida com algum retângulo, o retângulo que participou da colisão deve desaparecer.
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
    
    tela.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (button.collidepoint(x, y)):
                lista_quadrados = desenha_retangulo_aleatorio(lista_quadrados)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                centro_x_circulo -= 10
                button.centerx -= 10
            if event.key == pygame.K_d:
                centro_x_circulo += 10
                button.centerx += 10
            if event.key == pygame.K_w:
                centro_y_circulo -= 10
                button.centery -= 10
            if event.key == pygame.K_s:
                centro_y_circulo += 10
                button.centery += 10

    desenha_circulo(centro_x_circulo, centro_y_circulo, raio_circulo, "blue")
    escreve_mensagem("Clique aqui", centro_x_circulo, centro_y_circulo)
    
    for quad in lista_quadrados:
        if quad.colliderect(button):
            lista_quadrados.remove(quad)
    
    for quad in lista_quadrados:
        pygame.draw.rect(tela, "yellow", quad)
            
    
    
    clock.tick(50)
    pygame.display.update()  
    
    
pygame.display.quit()
pygame.quit()




