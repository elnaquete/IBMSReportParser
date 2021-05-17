encoding = 'utf-8'

from report_parser import report_parser
from counter import promo_counter
from constants import BLOQUES_HORARIOS

#Acá estaría bueno que el programa te tire una lista de archivos .csv y te deje elegir de qué
# reporte querés hacer el excel.

# llamo a la funcion que procesa el reporte. report_parser devuelve una tupla.
lista_pasadas, promos_database = report_parser("Test_full.csv")



# pregunto al usuario qué reporte quiere? O mando un Excel con una solapa por cada feed?
chosen_feed = 'ALL'

result, por_horarios = promo_counter(lista_pasadas,chosen_feed)





print (f"\nMedia MI\tDescripción\t\t\t\t\t\t\tDuración\tCan\t{BLOQUES_HORARIOS[0]}\t{BLOQUES_HORARIOS[1]}\t{BLOQUES_HORARIOS[2]}\t{BLOQUES_HORARIOS[3]}")
for key,value in result.items():
    descripcion = promos_database[key][0]
    duracion = promos_database[key][1]
    pasaduli0 = por_horarios.get((key, BLOQUES_HORARIOS[0]), 0)
    pasaduli1 = por_horarios.get((key, BLOQUES_HORARIOS[1]), 0)
    pasaduli2 = por_horarios.get((key, BLOQUES_HORARIOS[2]), 0)
    pasaduli3 = por_horarios.get((key, BLOQUES_HORARIOS[3]), 0)
    print (f"{key}\t{descripcion}\t{duracion}\t\t\t{value}\t\t{pasaduli0}\t\t{pasaduli1}\t\t{pasaduli2}\t\t{pasaduli3}")

# para indexar dentro de una lista, usar list [2][3], x ej.
