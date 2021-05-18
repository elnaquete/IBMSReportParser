
class Pieza(object):
    pass

class Pieza_on_air(Pieza):
    """
    Por ahora no la usamos, usamos una tupla con programme y duration en su lugar
    """
    def __init__(self, programme, duration, media_MI):
        self.programme = programme
        self.duration = duration
        self.media_MI = media_MI
    
    def __str__(self):
        return f"Nombre de promo: {self.programme}\nDuración: {self.duration}\nMedia MI: {self.media_MI}"

class Pasada(object):
    def __init__(self, number, feed, tx_date, tx_time, programme, duration, media_MI, description, event_sub_type, hour_flag):
        self.number = number
        self.feed = feed
        self.tx_date = tx_date
        self.tx_time = tx_time
        self.programme = programme
        self.duration = duration
        self.media_MI = media_MI
        self.description = description
        self.event_sub_type = event_sub_type
        self.hour_flag = hour_flag

    def __str__(self):
        return f""" number: {self.number} \n feed: {self.feed} \n tx_date and time: {self.tx_date} {self.tx_time} \n programme: {self.programme} \n duration: {self.duration} \n media_MI: {self.media_MI} \n description: {self.description} \n event_sub_type: {self.event_sub_type}
            """




