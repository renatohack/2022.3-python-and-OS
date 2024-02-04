"""
Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
E:
Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino. Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.
"""

import requests
from collections import namedtuple

Medal = namedtuple("Medal", "year, city, sport, discipline, NOC, event, event_gender, medal")

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"

csv = requests.get(url).text

list_rows = csv.splitlines()
dataTable = []

for i in list_rows:
    splitted_row = i.split(",")
    medal = Medal(splitted_row[0],
                  splitted_row[1],
                  splitted_row[2],
                  splitted_row[3],
                  splitted_row[4],
                  splitted_row[5],
                  splitted_row[6],
                  splitted_row[7]
                  )
    dataTable.append(medal)

dict_paises = {}

for medal in dataTable:
    if not medal.NOC in dict_paises:
        dict_paises[medal.NOC] = [(medal.sport, medal.year, medal.city, medal.event_gender)]
    else:
        dict_paises[medal.NOC].append((medal.sport, medal.year, medal.city, medal.event_gender))
        
dict_paises.pop("NOC")

total_medalhas = 0
for key in dict_paises:
    print("Total de medalhas do pais {0}: {1}".format(key, len(dict_paises[key])))
    for medal in dict_paises[key]:
        print(medal)
    print("----------------------------------------------------------------")

