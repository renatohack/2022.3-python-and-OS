"""
Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.
"""

from bs4 import BeautifulSoup
import requests
from collections import namedtuple

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url, verify=False).text

soup = BeautifulSoup(html,"lxml")

html_content = soup.html.body.div.article.center.div


# ** (a) Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
linhas = html_content.text.split("\n\n")

colunas = []

for i in linhas:
    if i:
        coluna = i.split("\n")
        for j in coluna:
            if not j:
                coluna.remove(j)
        colunas.append(coluna)
        
print(colunas)


# ** (b) Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.

dict_regioes = {}

for i in colunas:
    if len(i[0]) == 2:
        dict_regioes[i[0].lower()] = (i[1], i[2], i[3], i[4])
        
sigla = input("Entre com uma sigla da região centro oeste:")

if sigla.lower() in dict_regioes:
    print(dict_regioes[sigla.lower()])
else:
    print("Esse estado não pertence à região centro oeste.")



