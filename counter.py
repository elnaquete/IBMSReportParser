#from constants import FEEDS

def promo_counter (lista_pasadas):
    """
    Dada una lista con objetos Pasada, cuenta cuantas pasadas tiene cada objeto.
    Retorna un diccionario con cantidad de pasadas segun promo.
    """ 
    dict_pasadas = {}
    dict_horas = {}

    for item in lista_pasadas:
        #contador total de pasadas
        identificador_total = (item.feed, item.media_MI)
        if identificador_total in dict_pasadas.keys():
            dict_pasadas[identificador_total] += 1
        else:
            dict_pasadas[identificador_total] = 1
        
        #actualizo contador de pasadas por hora, segun flags
        identificador = (item.feed,item.media_MI,item.hour_flag)
        if identificador in dict_horas.keys():
                dict_horas[identificador] += 1
        else:
            dict_horas[(item.feed,item.media_MI,item.hour_flag)] = 1
    
    return dict(sorted(dict_pasadas.items(), key=lambda x: x[1], reverse=True)), dict_horas
    return dict_pasadas, dict_horas

