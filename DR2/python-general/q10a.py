"""
Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
E:
Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique: No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
Curling
Patinação no gelo (skating)
Esqui (skiing)
Hóquei sobre o gelo (ice hockey)
"""

import requests
from collections import namedtuple

Medal = namedtuple("Medal", "year, city, sport, discipline, NOC, event, event_gender, medal")

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"

csv = requests.get(url).text

list_rows = csv.splitlines()
dataTable = []

dict_medalhas = {"DEN": 0, "SWE": 0, "NOR": 0}

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


for medal in dataTable:
    if medal.NOC == "DEN" or medal.NOC == "SWE" or medal.NOC == "NOR":
        if int(medal.year) >= 2001:
            if medal.sport == "Skating" or medal.sport == "Ice Hockey" or medal.sport == "Skiing" or medal.sport == "Curling":
                if medal.medal == "Gold":
                    dict_medalhas[medal.NOC] += 1
                    
print(dict_medalhas)

max = 0
pais = ""

for key in dict_medalhas:
    if int(dict_medalhas[key]) > max:
        max = int(dict_medalhas[key])
        pais = key

print("País ganhador de mais medalhas de ouro:", pais, "com", max, "medalhas.")