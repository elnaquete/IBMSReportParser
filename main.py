encoding = 'utf-8'

import csv
from classes import Pasada
from counter import promo_counter
from constants import FEEDS
import pprint

print ("Procesando informe... por favor espere.")

with open("Test_full.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    lista_pasadas = []
    for number, line in enumerate(reader):
        lista_pasadas.append(Pasada(number,line[0], (line[1]+ " " +line[2]), line[3], line[4], line[5], line[6], line[7]))

#Inicializacion del pretty printer - luego lo borramos
pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)


print (f"\n Lista de feeds disponibles: \n {FEEDS}")
chosen_feed = input("De qué feed necesita el reporte? \n")


result = promo_counter(lista_pasadas[1:],chosen_feed)
pp.pprint (result)

# para indexar dentro de una lista, usar list [2][3], x ej.
