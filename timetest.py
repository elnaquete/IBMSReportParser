from datetime import datetime


#tx_date = '20210301'
tx_time = '08:00:07'

#tx_combined = tx_date + tx_time

#py_date = datetime.strptime(tx_date, "%Y%m%d")
py_time = datetime.strptime(tx_time, "%I:%M:%S")


#py_combined = datetime.strptime(tx_combined, "%Y%m%d%I:%M:%S")

#print (tx_combined)
#print (py_combined.time())

print (py_time)
