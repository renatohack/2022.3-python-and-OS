import turtle
import math

import pygame


# ** q5
def anda_diagonal(lado):
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(lado)
    turtle.setheading(90)
    turtle.forward(lado)
    turtle.setheading(0)

def desenha_quadrado(lado):
    turtle.setheading(0)
    for _ in range(4):
        turtle.forward(lado)
        turtle.left(90)

def desenha_circulo(raio):
    turtle.setheading(0)
    turtle.circle(raio)
    
def desenha_figuras(passo_diagonal):
    turtle.pendown()
    desenha_quadrado(4 * passo_diagonal)
    
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(7 * passo_diagonal)
    
    turtle.pendown()
    desenha_circulo(2 * passo_diagonal)
    
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(5 * passo_diagonal)
    
    turtle.pendown()
    desenha_circulo(2 * passo_diagonal)
    
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(7 * passo_diagonal)
    
    turtle.pendown()
    desenha_quadrado(4 * passo_diagonal)
    
    turtle.penup()
    turtle.left(270)
    turtle.forward(5 * passo_diagonal)