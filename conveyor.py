import pandas as pd
import numpy as np
from datetime import datetime

from requests import delete

data = pd.read_csv('Cyc.csv')
dates = data[['DATE']]
hour = np.array([])
minute = np.array([])
wday = np.array([])

for i in dates.values:
    date_time_obj = datetime.strptime(str(i[0]), '%d.%m.%Y %H:%M')
   
    hour = np.append(hour, date_time_obj.hour)
    minute = np.append(minute, date_time_obj.minute)
    wday = np.append(wday, date_time_obj.weekday())
    
data.insert(value= hour, column='HOUR', loc= 3 )
data.insert(value= minute, column='MIN', loc= 4 )
data.insert(value= wday, column='WDAY', loc= 5 )
data = data.drop(columns=['DATE'])
print(data)
data.to_csv('out.csv')
