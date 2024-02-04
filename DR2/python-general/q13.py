"""
Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
Conte quantas vezes apareceu a palavra ladies no conteúdo da página
"""

from bs4 import BeautifulSoup
import requests
from collections import namedtuple

url = "http://brasil.pyladies.com/about"

html = requests.get(url, verify=False).text

soup = BeautifulSoup(html,"lxml")


# ** Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.

body_content = soup.html.body

linhas = body_content.text.split("\n")

linhas_filtradas = []

for i in linhas:
    if i:
        linhas_filtradas.append(i)


palavras = []

for i in linhas_filtradas:
    if i:
        palavras.append(i.split(" "))
        
        
palavras_filtradas = []

for i in palavras:
    if i:
        for j in i:
            if j:
                palavras_filtradas.append(j)


dict_palavras = {}
ladies_count = 0
for i in palavras_filtradas:
    if i in dict_palavras:
        dict_palavras[i] += 1
    else:
        dict_palavras[i] = 1
    
    if i.lower() == "ladies":
        ladies_count += 1
        

palavras_1x = []

for i in dict_palavras:
    if dict_palavras[i] == 1:
        palavras_1x.append(i)

print("Quantidade de palavras no corpo (tag 'body') da página: {0}".format(len(palavras_filtradas)))
print("----------------------------------------------------------------")
print("Palavras que apareceram somente 1 vez: {0}".format(palavras_1x))
print("----------------------------------------------------------------")
print("Quantidade de palavras 'ladies': {0}".format(ladies_count))










