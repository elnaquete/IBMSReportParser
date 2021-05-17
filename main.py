encoding = 'utf-8'

from report_parser import report_parser
from counter import promo_counter
from constants import FEEDS

#Acá estaría bueno que el programa te tire una lista de archivos .csv y te deje elegir de qué
# reporte querés hacer el excel.

# llamo a la funcion que procesa el reporte. report_parser devuelve una tupla.
lista_pasadas, promos_database = report_parser("Test.csv")



# pregunto al usuario qué reporte quiere? O mando un Excel con una solapa por cada feed?
chosen_feed = 'ALL'

result = promo_counter(lista_pasadas,chosen_feed)
print (f"\nMedia MI\tDescripción\t\t\t\t\t\t\tDuración\tCant.pasadas")
for key,value in result.items():
    descripcion = promos_database[key][0]
    duracion = promos_database[key][1]
    print (f"{key}\t{descripcion}\t{duracion}\t\t\t{value}")

# para indexar dentro de una lista, usar list [2][3], x ej.
