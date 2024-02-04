from random import randint
import pygame
from pygame_config import *
import math

def desenha_circulo(x, y, raio):
    pygame.draw.circle(tela, AZUL, (x, y), raio, 0)

def desenha_circulo(x, y, raio, cor):
    pygame.draw.circle(tela, cor, (x, y), raio, 0)

def preencher_tela(cor):
    tela.fill(cor)

def desenha_quadrado(x, y, lado, cor):
    pygame.draw.rect(tela, cor, (x, y, lado, lado), 0)

def desenha_estrela(x, y, lado):
    
    lista_pontos = []
    angulo = 0
    raio_interno = lado // 2
    raio_externo = lado
    
    for i in range(10):
        angulo_rad = math.radians(angulo)
        
        if i % 2 == 0:
            raio = raio_interno
        else: 
            raio = raio_externo
            
        x_ponto = x + raio * math.sin(angulo_rad)
        y_ponto = y + raio * math.cos(angulo_rad)
        
        angulo += 360 // 10
        
        lista_pontos.append((x_ponto, y_ponto))
        
    for i in range (0, len(lista_pontos)):
        pygame.draw.line(tela, VERDE, lista_pontos[i - 1], lista_pontos[i])
        pygame.draw.polygon(tela, VERDE, lista_pontos, 0)

def desenha_linha(x_inicial, y_inicial, x_final, y_final, largura):
    pygame.draw.line(tela, BRANCO, (x_inicial, y_inicial), (x_final, y_final), largura)

def escreve_mensagem(texto, x, y):
    font = pygame.font.Font(None, 32)
    text = font.render(texto, False, BRANCO)
    textpos = text.get_rect()
    textpos.center = (x, y)
    tela.blit(text, textpos)

# ** JOGO DA VELHA
def desenha_arena_jogo_da_velha():
    
    largura_celula = LARGURA_TELA / 3
    altura_celula = ALTURA_TELA / 3
    
    #desenha linhas verticais
    for i in range(1, 3):
        x = (largura_celula * i) - (LARGURA_LINHA_JOGO_DA_VELHA / 2)
        y_inicial = 0
        y_final = ALTURA_TELA
        desenha_linha(x, y_inicial, x, y_final, LARGURA_LINHA_JOGO_DA_VELHA)
        
    #desenha linhas horizontais
    for i in range(1, 3):
        y = (altura_celula * i) - (LARGURA_LINHA_JOGO_DA_VELHA / 2)
        x_inicial = 0
        x_final = LARGURA_TELA
        desenha_linha(x_inicial, y, x_final, y, LARGURA_LINHA_JOGO_DA_VELHA)

def desenha_x(x_inicial, y_inicial, lado_x, lado_y):
    ponto1_x = x_inicial
    ponto1_y = y_inicial
    
    ponto2_x = x_inicial + lado_x
    ponto2_y = y_inicial
    
    ponto3_x = x_inicial 
    ponto3_y = y_inicial + lado_y
    
    ponto4_x = x_inicial + lado_x
    ponto4_y = y_inicial + lado_y
    
    desenha_linha(ponto1_x, ponto1_y, ponto4_x, ponto4_y, LARGURA_LINHA_JOGO_DA_VELHA)
    desenha_linha(ponto2_x, ponto2_y, ponto3_x, ponto3_y, LARGURA_LINHA_JOGO_DA_VELHA)
    
def desenha_bola(x, y, raio, largura):
    pygame.draw.circle(tela, BRANCO, (x, y), raio, largura)

def desenha_simbolos(lista_simbolos):
    largura_celula = LARGURA_TELA / 3
    altura_celula = ALTURA_TELA / 3
    
    offset_x = largura_celula / 3
    offset_y = altura_celula / 3
    
    raio_bola_x = offset_x / 2
    raio_bola_y = offset_y / 2
    lado_X_x = offset_x
    lado_X_y = offset_y
    
    for row in range(3):
        for col in range(3):
            if lista_simbolos[row][col] == 'X':
                x_inicial = largura_celula * col + offset_x
                y_inicial = altura_celula * row + offset_y
                desenha_x(x_inicial, y_inicial, lado_X_x, lado_X_y)
            elif lista_simbolos[row][col] == 'O':
                x_centro = largura_celula * col + offset_x + raio_bola_x
                y_centro = altura_celula * row + offset_y + raio_bola_y
                desenha_bola(x_centro, y_centro, raio_bola_x, LARGURA_LINHA_JOGO_DA_VELHA)
                
def generate_Rects():
    
    lista_rects = []
    lista_isClicked = []
    
    for i in range(3):
        lista_rects.append([0] * 3)
        lista_isClicked.append([0] * 3)
    
    
    largura_celula = LARGURA_TELA / 3
    altura_celula = ALTURA_TELA / 3
    
    for row in range(3):
        for col in range (3):
            left = largura_celula * col
            top = altura_celula * row
            rect = pygame.Rect(left, top, largura_celula, altura_celula)
            lista_rects[row][col] = rect
            lista_isClicked[row][col] = False
            
    return lista_rects, lista_isClicked

def trocar_jogador(vez_jogador_1):
    return not vez_jogador_1
    
def verificar_resultado(matriz_simbolos):
    lista_condicoes = [
        matriz_simbolos[0][0] == matriz_simbolos[0][1] and matriz_simbolos[0][0] == matriz_simbolos[0][2],
        matriz_simbolos[1][0] == matriz_simbolos[1][1] and matriz_simbolos[1][0] == matriz_simbolos[1][2],
        matriz_simbolos[2][0] == matriz_simbolos[1][1] and matriz_simbolos[2][0] == matriz_simbolos[2][2],
        matriz_simbolos[0][0] == matriz_simbolos[1][0] and matriz_simbolos[0][0] == matriz_simbolos[2][0],
        matriz_simbolos[0][1] == matriz_simbolos[1][1] and matriz_simbolos[0][1] == matriz_simbolos[2][1],
        matriz_simbolos[0][2] == matriz_simbolos[1][2] and matriz_simbolos[0][2] == matriz_simbolos[2][2],
        matriz_simbolos[0][0] == matriz_simbolos[1][1] and matriz_simbolos[0][0] == matriz_simbolos[2][2],
        matriz_simbolos[0][2] == matriz_simbolos[1][1] and matriz_simbolos[0][2] == matriz_simbolos[2][0],
        ]
    
    for condicao in lista_condicoes:
        if condicao:
            return True
    return False

# ** JOGO DA MEMÓRIA
class Carta:
    def __init__(self, simboloObj, rect, id):
        self.id = id
        self.simboloObj = simboloObj
        self.rect = rect

class Simbolo():
    def __init__(self, x, y, width, cor, isFilled):
        self.x = x
        self.y = y
        self.width = width
        self.raio = width
        self.cor = cor
        self.isFilled = isFilled
    
    def desenha_simbolo(self):
        pass

class Quadrado(Simbolo):
    def desenha_simbolo(self):
        largura = 0 if self.isFilled else 5
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.width, self.width), largura)

class Circulo(Simbolo):   
    def desenha_simbolo(self):
        largura = 0 if self.isFilled else 5
        pygame.draw.circle(tela, self.cor, (self.x, self.y), self.raio, largura)    

def embaralhar_lista_cartas():
    combinacoes = [{'simbolo':'QUADRADO', 'cor':VERMELHO, 'isFilled':True, 'id':1},
                   {'simbolo':'QUADRADO', 'cor':VERMELHO, 'isFilled':False, 'id':2},
                   {'simbolo':'QUADRADO', 'cor':VERDE, 'isFilled':True, 'id':3},
                   {'simbolo':'QUADRADO', 'cor':VERDE, 'isFilled':False, 'id':4},
                   {'simbolo':'CIRCULO', 'cor':VERMELHO, 'isFilled':True, 'id':5},
                   {'simbolo':'CIRCULO', 'cor':VERMELHO, 'isFilled':False, 'id':6},
                   {'simbolo':'CIRCULO', 'cor':VERDE, 'isFilled':True, 'id':7},
                   {'simbolo':'CIRCULO', 'cor':VERDE, 'isFilled':False, 'id':8},
                   {'simbolo':'QUADRADO', 'cor':VERMELHO, 'isFilled':True, 'id':1},
                   {'simbolo':'QUADRADO', 'cor':VERMELHO, 'isFilled':False, 'id':2},
                   {'simbolo':'QUADRADO', 'cor':VERDE, 'isFilled':True, 'id':3},
                   {'simbolo':'QUADRADO', 'cor':VERDE, 'isFilled':False, 'id':4},
                   {'simbolo':'CIRCULO', 'cor':VERMELHO, 'isFilled':True, 'id':5},
                   {'simbolo':'CIRCULO', 'cor':VERMELHO, 'isFilled':False, 'id':6},
                   {'simbolo':'CIRCULO', 'cor':VERDE, 'isFilled':True, 'id':7},
                   {'simbolo':'CIRCULO', 'cor':VERDE, 'isFilled':False, 'id':8}]
    
    lista_embaralhada = []
    iteracoes = len(combinacoes)
    for _ in range(iteracoes):
        index = randint(0, len(combinacoes) - 1)
        item = combinacoes[index]
        lista_embaralhada.append(item)
        combinacoes.remove(item)
    
    return lista_embaralhada

def generate_cartas():
    
    lista_embaralhada = embaralhar_lista_cartas()
    
    largura_carta = LARGURA_TELA / 4
    altura_carta = ALTURA_TELA / 4
    
    offset_x = largura_carta / 4
    offset_y = altura_carta / 4

    lista_cartas = []
    
    #for _ in range(4):
    #    lista_cartas.append([0] * 4)
    
    for i in range(4):
        for j in range(4):
            combinacao = lista_embaralhada[0]
            simbolo = combinacao['simbolo']
            cor = combinacao['cor']
            isFilled = combinacao['isFilled']
            id = combinacao['id']
        
            if (simbolo == "QUADRADO"):
                quadrado_left = largura_carta * j + offset_x    
                quadrado_top = altura_carta * i + offset_y
                lado_quadrado = offset_x * 2
                novo_simbolo = Quadrado(quadrado_left, quadrado_top, lado_quadrado, cor, isFilled)
                rect = pygame.Rect(largura_carta * j, altura_carta * i, largura_carta, altura_carta)
                lista_cartas.append(Carta(novo_simbolo, rect, id))
            elif (simbolo == "CIRCULO"):
                raio_circulo = offset_x
                x_circulo = largura_carta * j + offset_x + raio_circulo
                y_circulo = altura_carta * i + offset_y + raio_circulo
                novo_simbolo = Circulo(x_circulo, y_circulo, raio_circulo, cor, isFilled)
                rect = pygame.Rect(largura_carta * j, altura_carta * i, largura_carta, altura_carta)
                lista_cartas.append(Carta(novo_simbolo, rect, id))
            lista_embaralhada.remove(combinacao)
    return lista_cartas

def desenha_cartas(cartas):
    
    for carta in cartas:
        carta.simboloObj.desenha_simbolo()
    
    """
    for linha_cartas in cartas:
        for carta in linha_cartas:
            carta.simboloObj.desenha_simbolo()
    """
    
def checar_carta(cartas, x, y):
    for carta in cartas:
        if carta.rect.collidepoint(x, y):
                return carta
            
def checar_cartas_levantadas(cartas_levantadas, cartas_descobertas):
    if len(cartas_levantadas) == 2:
        carta1 = cartas_levantadas[0]
        carta2 = cartas_levantadas[1]
        
        if (carta1.id == carta2.id):
            cartas_descobertas.append(carta1)
            cartas_descobertas.append(carta2)
            cartas_levantadas = []
        else:
            pygame.time.wait(500)
            cartas_levantadas = []
        tela.fill(PRETO)
    return cartas_levantadas, cartas_descobertas

def checar_fim_jogo(cartas_descobertas, cartas):
    if (len(cartas_descobertas) != len(cartas)):
        desenha_cartas(cartas_descobertas)
    else:
        tela.fill(PRETO)
        escreve_mensagem("VOCÊ GANHOU!", LARGURA_TELA / 2, ALTURA_TELA / 2)
        
# ** questão 8 AT
def desenha_retangulo_aleatorio(lista_quadrados):
    left_quadrado = randint(0, LARGURA_TELA)
    top_quadrado = randint(0, ALTURA_TELA)
    altura_retangulo = randint(10, 50)
    largura_retangulo = randint(10, 50)
    rect = pygame.Rect(left_quadrado, top_quadrado, altura_retangulo, largura_retangulo)
    
    rectExist = False
    for quad in lista_quadrados:
        if quad.colliderect(rect):
            lista_quadrados.remove(quad)
            rectExist = True
            
    if not rectExist:
        lista_quadrados.append(rect)
    
    tela.fill("black")
    for rect in lista_quadrados:
        pygame.draw.rect(tela, "yellow", rect)
        
    return lista_quadrados