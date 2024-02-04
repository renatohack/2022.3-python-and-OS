"""
Usando a biblioteca ‘turtle’ crie uma função que desenhe a imagem a seguir:
"""

import turtle
from turtle_functions import *

LARGURA_TELA = 800
ALTURA_TELA = 800

turtle.shape("turtle")
turtle.speed("fastest")
turtle.bgcolor("white")
turtle.color("black")
turtle.Screen().setup(LARGURA_TELA, ALTURA_TELA)
turtle.speed(5)

# init
passo_diagonal = LARGURA_TELA / 11


turtle.penup()
turtle.goto(- LARGURA_TELA / 2, - ALTURA_TELA / 2)

while passo_diagonal > 1:
    anda_diagonal(passo_diagonal)
    desenha_figuras(passo_diagonal)
    passo_diagonal = 4 * passo_diagonal / 11


turtle.exitonclick()




