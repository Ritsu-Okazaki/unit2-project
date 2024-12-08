import requests
from matplotlib import pyplot as plt
from matplotlib import dates as md
import dateutil
from matplotlib.dates import HourLocator
import numpy as np
from Project.my_lib import moving_average

plt.style.use('ggplot')

def timestamp_format(timestamp:str):
    year, month, temp = timestamp.split("-")
    day, temp = temp.split("T")
    hour, minute, second = temp.split(":")
    minute = int(minute)
    second = float(second)
    if second == 60:
        minute += 1
        second = 0
    return int(year), int(month), int(day), int(hour), int(minute), round(float(second),1)

server_ip = '192.168.4.137'
request = requests.get(f'http://{server_ip}/readings')
data = request.json()

readings = data['readings'][0]

sensor_10 = [] #DHT_temp
fdates = []
timeindex = []
t = 0

for r in readings:
    if r['sensor_id'] == 10:
        tf = timestamp_format(r['datetime'])
        year, month, date, hour, minute, second = tf[0],tf[1],tf[2],tf[3],tf[4],tf[5]
        if month == 11 and date == 24 or date == 25:
            print(r['datetime'],r['value'])
            fdates.append(f"{year}-{month}-{date} {hour}:{minute}:{second}")
            timeindex.append(t)
            t += 1
            sensor_10.append(r['value'])

# Graph style
fig = plt.figure(figsize=(10,6))
plt.subplots_adjust(bottom=0.2)
plt.xticks( rotation= 80 )
plt.xlabel("Time/(Hours:Minutes)")
plt.ylabel("Temperature/℃")
plt.title("Remote BME280 Temperature Measurements Nov 24th ~ Nov 25th")

# Define x axis
ax=plt.gca()

# Plot hour:minute into x axis per hour
pdates = [dateutil.parser.parse(s) for s in fdates]
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.xaxis.set_major_locator(HourLocator(byhour=range(0, 24, 1), tz=None))
plt.plot(pdates,sensor_10)

# Smoothed
plt.plot(pdates[:-40],moving_average(40, sensor_10),color='black',alpha = 0.7,label='smoothed by window 40')

# Mathematical model
y_octic = []
a,b,c,d,e,f,g,h,I = np.polyfit(timeindex, sensor_10, deg=8)
for i in timeindex:
    y_octic += [a*i**8 + b*i**7 + c*i**6 + d*i**5 + e*i**4 + f*i**3 + g*i**2 + h*i + I]
plt.plot(pdates,y_octic, color='purple', label='octic model')

# Plot and show
plt.legend()
plt.tight_layout()
plt.show()
