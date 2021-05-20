encoding = 'utf-8'

from report_parser import report_parser
from counter import promo_counter
from write2excel import write2excel

destination_filename = "final.xlsx"
source_filename = "Abril_full.csv"

#Acá estaría bueno que el programa te tire una lista de archivos .csv y te deje elegir de qué
# reporte querés hacer el excel.

# llamo a la funcion que procesa el reporte. report_parser devuelve una tupla.
lista_Pasadas, promos_database = report_parser(source_filename)

#promo_counter genera las 2 cuentas: totales por pieza y por horarios por pieza por feed.
pasadas_totales, pasadas_por_horarios = promo_counter(lista_Pasadas)

#ahora escribir al excel. Le mando ambos resultados más la base de datos de promos.
write2excel (promos_database, pasadas_totales, pasadas_por_horarios, destination_filename)