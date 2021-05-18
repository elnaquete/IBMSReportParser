import datetime as dt

HEADERS = ('CHANNEL_CODE', 'TX_DATE', 'TX_TIME', 'PROGRAMME', 'DURATION', 'HOUSE_MEDIA', 'DESCRIPTION', 'EVENT_SUB_TYPE')

FEEDS = ('AMCS', 'AMCB', 'AMCL', 'AMCN', 'AMCO', 'AMCS', 'EURL', 'FYAB', 'FYAL', 'GOUN', 'GOUS', 'GOUU', 'MASL', 'MASU')

h00 = dt.datetime(1970, 1, 1, 0, 0).time()
h06 = dt.datetime(1970, 1, 1, 6, 0).time()
h12 = dt.datetime(1970, 1, 1, 12, 0).time()
h18 = dt.datetime(1970, 1, 1, 18, 0).time()
h24 = dt.datetime(1970, 1, 1, 23, 59, 59).time()

BLOQUES_HORARIOS = ('00-06', '06-12', '12-18', '18-24')