from constants import FEEDS

def promo_counter (lista_pasadas, feed):
    """
    Dada una lista con objetos Pasada, cuenta cuantas pasadas tiene cada objeto.
    Retorna un diccionario con cantidad de pasadas segun promo.
    """ 
    dict_promos = {}
    if feed == "ALL":
        for item in lista_pasadas:
            if item.media_MI in dict_promos.keys():
                dict_promos[item.media_MI] += 1
            else:
                dict_promos[item.media_MI] = 1
    elif feed in FEEDS:
            for item in lista_pasadas:
                if item.feed == feed:
                    if item.media_MI in dict_promos.keys():
                        dict_promos[item.media_MI] += 1
                    else:
                        dict_promos[item.media_MI] = 1
    else:
        return f"No se encuentra el feed {feed}"

    return dict(sorted(dict_promos.items(), key=lambda item: item[1], reverse=True))
    