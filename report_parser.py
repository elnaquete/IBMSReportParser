import csv
from classes import Pasada
from datetime import datetime

def report_parser(filename):

    print ("Procesando informe... por favor espere.")

    with open(filename, "r") as f:
        archivo_original = csv.reader(f, delimiter=";")
        lista_pasadas = []
        promos_database = {}
        for number, line in enumerate(archivo_original):
            try:   
                feed = line[0] 
                tx_date_time = datetime.strptime(line[1] + line[2], "%Y%m%d%I:%M:%S")
                programme = line[3]
                duration = line[4]
                media_MI = line[5]
                description = line[6]
                event_sub_type = line[7]
                #conformo la lista de pasadas (list)
                lista_pasadas.append(Pasada(number,feed, tx_date_time, programme, duration, media_MI, description, event_sub_type))
                
                #conformo el inventario de promos (diccionario)
                if media_MI not in promos_database.keys():
                    promos_database[media_MI] = (programme, duration, description)
            except ValueError: #Para que no cuente al encabezado como una pasada.
                pass
    return lista_pasadas, promos_database