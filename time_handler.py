def time_handler (date_string, time_string):
    '''
    IN: 
    Date string in "yyyymmdd" format
    Time strings in "hh:mm:ss" TV Broadcast notation, where day starts at 08:00:00 and ends at 31:59:59
    OUT: a time object, in 0 to 23:59:59 'human-readable' format
    '''
    from datetime import datetime
    from datetime import timedelta

    promo_hour = int (time_string[:2])
    
    if promo_hour >= 24:
        time_string = '0' + str(promo_hour - 24) + time_string[2:] 
        fecha_y_hora = datetime.strptime(str(date_string) + time_string, "%Y%m%d%H:%M:%S")
        fecha_y_hora += timedelta(days=1)
    else:
        fecha_y_hora = datetime.strptime(str(date_string) + time_string, "%Y%m%d%H:%M:%S")
    
    return fecha_y_hora

if __name__ == "__main__":
    print (time_handler("20210301", "08:00:07"))
    print (time_handler("20210301", "26:00:07"))
    print (time_handler("20210301", "30:00:07"))
