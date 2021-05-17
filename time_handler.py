def time_handler (time_string):
    '''
    IN: Time strings in "hh:mm:ss" TV Broadcast notation, where day starts at 08:00:00 and ends at 31:59:59
    OUT: a time object, in 0 to 23:59:59 'human-readable' format
    '''
    from datetime import datetime
    

    troubling_hours = (24, 25, 26, 27, 28, 29, 30, 31)
    promo_hour = int (time_string[:2])
    
    if promo_hour in troubling_hours:
        time_string = '0' + str(promo_hour - 24) + time_string[2:]
    
    return datetime.strptime(time_string, "%I:%M:%S")
    

