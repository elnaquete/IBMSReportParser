import csv
from classes import Pasada
from time_handler import time_handler

def report_parser(filename):

    print ("Procesando informe... por favor espere.")

    with open(filename, "r") as f:
        archivo_original = csv.reader(f, delimiter=";")
        lista_pasadas = []
        promos_database = {}
        for number, line in enumerate(archivo_original):
            try:   
                feed = line[0] 
                tx_date = line [1]
                tx_time = time_handler(line[2])
                programme = line[3]
                duration = line[4]
                media_MI = line[5]
                description = line[6]
                event_sub_type = line[7]
                hour_flag = hour_flags_maker(tx_time)
                #conformo la lista de pasadas (list)
                lista_pasadas.append(Pasada(number,feed, tx_date, tx_time, programme, duration, media_MI, description, event_sub_type, hour_flag))
                
                #conformo el inventario de promos (diccionario)
                if media_MI not in promos_database.keys():
                    promos_database[media_MI] = (programme, duration, description)
            except ValueError: #Para que no cuente al encabezado como una pasada.
                pass
    return lista_pasadas, promos_database


def hour_flags_maker (tx_time):
    '''
    IN: Time, transmission time of the promo (datetime object)
    OUT: Boolean flags for the 4 time slots defined in BLOQUES_HORARIOS (dict)
    '''
    from constants import h00, h06, h12, h18, h24, BLOQUES_HORARIOS

    #defino subgrupo según hora de pasada
    if h00 <= tx_time < h06:
        hour_flag = BLOQUES_HORARIOS[0]
    elif h06 <= tx_time < h12:
        hour_flag = BLOQUES_HORARIOS[1]
    elif h12 <= tx_time < h18:
        hour_flag = BLOQUES_HORARIOS[2] 
    elif h18 <= tx_time < h24:
        hour_flag = BLOQUES_HORARIOS[3]
    
    return hour_flag

