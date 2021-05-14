encoding = 'utf-8'

import csv
from classes import Pasada, Pieza_on_air
from counter import promo_counter
from constants import FEEDS
import pprint

print ("Procesando informe... por favor espere.")

with open("Test_full.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    lista_pasadas = []
    db_promos = {}
    
    for number, line in enumerate(reader):
        media_MI = line[5]
        #conformo la lista de pasadas (lista)
        lista_pasadas.append(Pasada(number,line[0], line[1], line[2], line[3], line[4], media_MI, line[6], line[7]))
        #conformo el inventario de promos (diccionario)
        #tengo forma de chequear que no haya valores repetidos?
        if media_MI not in db_promos.keys():
            db_promos[media_MI] = Pieza_on_air(line[3], line[4], media_MI)



#Inicializacion del pretty printer - luego lo borramos
pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)


#print (f"\n Lista de feeds disponibles: \n {FEEDS}")
#chosen_feed = input("De qué feed necesita el reporte? O Escriba ALL para todos\n")


#result = promo_counter(lista_pasadas[1:],chosen_feed)
#pp.pprint (result)

# para indexar dentro de una lista, usar list [2][3], x ej.
