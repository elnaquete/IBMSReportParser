from constants import FEEDS

def promo_counter (lista_pasadas, feed):
    """
    Dada una lista con objetos Pasada, cuenta cuantas pasadas tiene cada objeto.
    Retorna un diccionario con cantidad de pasadas segun promo.
    """ 
    from constants import h00, h06, h12, h18, h24, BLOQUES_HORARIOS

    dict_pasadas = {}
    dict_horas = {}

    for item in lista_pasadas:
        #contador total de pasadas
        if item.media_MI in dict_pasadas.keys():
            dict_pasadas[item.media_MI] += 1
        else:
            dict_pasadas[item.media_MI] = 1
        
        #defino subgrupo según hora de pasada
        if h00 < item.tx_time <= h06:
            key = (item.media_MI, BLOQUES_HORARIOS[0])
        elif h06 < item.tx_time <= h12:
            key = (item.media_MI, BLOQUES_HORARIOS[1])
        elif h12 < item.tx_time <= h18:
            key = (item.media_MI, BLOQUES_HORARIOS[2])
        elif h18 < item.tx_time <= h24:
            key = (item.media_MI, BLOQUES_HORARIOS[3])      
        
        #actualizo contador de pasadas por hora
        if key in dict_horas.keys():
                dict_horas[key] += 1
        else:
            dict_horas[key] = 1

    return dict(sorted(dict_pasadas.items(), key=lambda item: item[1], reverse=True)), dict_horas

