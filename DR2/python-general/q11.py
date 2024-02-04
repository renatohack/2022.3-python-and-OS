"""
Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv
Obtenha, dentre os jogos do gênero de ação (Action), tiro (Shooter) e plataforma (Platform):
Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.
Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.
Qual é a marca com mais publicações em cada um dos gêneros nos últimos dez anos no Japão? Indique também o número total de jogos dela.
Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.
"""

import requests
from collections import namedtuple

Game = namedtuple("Game", "name, platform, year_of_release, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales, critic_score, critic_count, user_score, user_count, developer, rating")

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

csv = requests.get(url).text

list_rows = csv.splitlines()

dataTable = []

counter = 0
index = 1
for i in list_rows:
    if i[0] == '"':
        index = i.index('"', 1)
        name = i[0 : index + 1 : 1]
        remaining = i.replace(name, "")
        splitted_row = remaining.split(",")
        splitted_row[0] = name
    else:
        splitted_row = i.split(",")
    if splitted_row[3].lower() == "action" or splitted_row[3].lower() == "shooter" or splitted_row[3].lower() == "platform":
        game = Game(splitted_row[0],
                    splitted_row[1],
                    splitted_row[2],
                    splitted_row[3],
                    splitted_row[4],
                    splitted_row[5],
                    splitted_row[6],
                    splitted_row[7],
                    splitted_row[8],
                    splitted_row[9],
                    splitted_row[10],
                    splitted_row[11],
                    splitted_row[12],
                    splitted_row[13],
                    splitted_row[14],
                    splitted_row[15]
                    )
        dataTable.append(game)
    
    
# ** (a) Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.

dict_publicacoes = {}

for game in dataTable:
    if not game.publisher in dict_publicacoes:
        dict_publicacoes[game.publisher] = 1
    else:
        dict_publicacoes[game.publisher] += 1

list_publicacoes = list(dict_publicacoes.items())
sorted_publicacoes = sorted(list_publicacoes, key = lambda item:item[1], reverse = True)

print("As 3 marcas que mais publicaram jogos dos três gêneros combinados são:")
print("1 - {0} : {1} publicações".format(sorted_publicacoes[0][0], sorted_publicacoes[0][1]))
print("2 - {0} : {1} publicações".format(sorted_publicacoes[1][0], sorted_publicacoes[1][1]))
print("3 - {0} : {1} publicações".format(sorted_publicacoes[2][0], sorted_publicacoes[2][1]))
print("---------------------------------------------------------------------------")


# ** (b) Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.

dict_global_sales = {}

for game in dataTable:
    if not game.publisher in dict_global_sales:
        dict_global_sales[game.publisher] = float(game.global_sales)
    else:
        dict_global_sales[game.publisher] += float(game.global_sales)
        
list_global_sales = list(dict_global_sales.items())
sorted_global_sales = sorted(list_global_sales, key = lambda item:item[1], reverse = True)

print("As 3 marcas que mais venderam os três gêneros combinados são:")
print("1 - {0} : {1} vendas globais".format(sorted_global_sales[0][0], round(sorted_global_sales[0][1], 2)))
print("2 - {0} : {1} vendas globais".format(sorted_global_sales[1][0], round(sorted_global_sales[1][1], 2)))
print("3 - {0} : {1} vendas globais".format(sorted_global_sales[2][0], round(sorted_global_sales[2][1], 2)))
print("---------------------------------------------------------------------------")


# ** (c) Qual é a marca com mais publicações em cada um dos gêneros nos últimos dez anos no Japão? Indique também o número total de jogos dela.

# TODO : NAO HA INFORMACAO SOBRE PUBLICACAO NO JAPAO
    
# ** (d) Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.

#filter datatable
dataTable_past10years = []
for game in dataTable:
    if game.year_of_release != "N/A":
        if int(game.year_of_release) >= 2007:
            dataTable_past10years.append(game) 

dict_genre = {}

for game in dataTable_past10years:
    if not game.genre in dict_genre:
        dict_genre[game.genre] = {}
        dict_genre[game.genre][game.publisher] = float(game.jp_sales)
    else:
        if not game.publisher in dict_genre[game.genre]:
            dict_genre[game.genre][game.publisher] = float(game.jp_sales)
        else:
            dict_genre[game.genre][game.publisher] += float(game.jp_sales)


print("As marcas que mais venderam cada um dos gêneros no Japão foram:")
for genre in dict_genre:
    list_jp_sales = list(dict_genre[genre].items())
    sorted_jp_sales = sorted(list_jp_sales, key = lambda item:item[1], reverse = True)
    print("{0} - {1} : {2} vendas no Japão".format(genre, sorted_jp_sales[0][0], round(sorted_jp_sales[0][1], 2)))
print("---------------------------------------------------------------------------")
    