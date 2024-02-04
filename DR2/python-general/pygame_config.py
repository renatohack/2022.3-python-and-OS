import pygame

pygame.init()
pygame.font.init()

LARGURA_TELA = 600
ALTURA_TELA = 600

LARGURA_LINHA_JOGO_DA_VELHA = 5

VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
clock = pygame.time.Clock()