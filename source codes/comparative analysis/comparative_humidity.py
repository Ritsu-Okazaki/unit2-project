import requests
from matplotlib import pyplot as plt
from matplotlib import dates as md
import dateutil
from matplotlib.dates import HourLocator
import matplotlib.ticker as ticker
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
    return int(year), int(month), int(day), int(hour), int(minute), round(float(second),3)

server_ip = '192.168.4.137'
request = requests.get(f'http://{server_ip}/readings')
data = request.json()

readings = data['readings'][0]

sensor_206 = [] #DHT_temp
sensor_11 = []
sensor_204 = []
fdates1 = []
fdates2 = []
fdates3 = []
timeindex = []
t = 0

for r in readings:
    if r['sensor_id'] == 206:
        tf = timestamp_format(r['datetime'])
        year, month, date, hour, minute, second = tf[0],tf[1],tf[2],tf[3],tf[4],tf[5]
        if month == 12 and date == 5:
            print(r['datetime'],r['value'])
            # fdates1.append(f"{year}-{month}-{date} {hour}:{minute}:{second}")
            fdates1.append(f"{hour}:{minute}:{second}")
            timeindex.append(t)
            t += 1
            sensor_206.append(r['value'])
    if r['sensor_id'] == 11:
        tf = timestamp_format(r['datetime'])
        year, month, date, hour, minute, second = tf[0],tf[1],tf[2],tf[3],tf[4],tf[5]
        if month == 11 and date == 24:
            print(r['datetime'],r['value'])
            # fdates2.append(f"{year}-{month}-{date} {hour}:{minute}:{second}")
            fdates2.append(f"{hour}:{minute}:{second}")
            timeindex.append(t)
            t += 1
            sensor_11.append(r['value'])
    if r['sensor_id'] == 204:
        tf = timestamp_format(r['datetime'])
        year, month, date, hour, minute, second = tf[0],tf[1],tf[2],tf[3],tf[4],tf[5]
        if month == 12 and date == 5:
            print(r['datetime'],r['value'])
            # fdates1.append(f"{year}-{month}-{date} {hour}:{minute}:{second}")
            fdates3.append(f"{hour}:{minute}:{second}")
            timeindex.append(t)
            t += 1
            sensor_204.append(r['value'])

# Define x axis
ax=plt.gca()


pdates1 = [dateutil.parser.parse(s) for s in fdates1]
pdates2 = [dateutil.parser.parse(s) for s in fdates2]
pdates3 = [dateutil.parser.parse(s) for s in fdates3]

# Graph style
fig, axs = plt.subplots(3,sharex=True,sharey=True,figsize=(6,9))
fig.suptitle("Humidity Measurements Comparative Analysis")
axs[0].yaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel("Time/(Hours:Minutes)")
axs[1].set_ylabel("Humidity/%")

axs[0].plot(pdates3, sensor_204, color='grey')
axs[0].set_title('Local DHT11 Dec 5th')
axs[1].plot(pdates1, sensor_206, color='grey')
axs[1].set_title('Local BME280 Dec 5th')
axs[2].plot(pdates2, sensor_11, color='grey')
axs[2].set_title('Remote BME280 Nov 24th')

plt.xticks( rotation= 80 )

# Plot hour:minute into x axis per hour
xfmt = md.DateFormatter('%H:%M')
axs[0].xaxis.set_major_formatter(xfmt)
axs[0].xaxis.set_major_locator(HourLocator(byhour=range(0, 24, 1), tz=None))
axs[1].xaxis.set_major_formatter(xfmt)
axs[1].xaxis.set_major_locator(HourLocator(byhour=range(0, 24, 1), tz=None))



# Max
max1 = [pdates1[sensor_204.index(max(sensor_204))],max(sensor_204)]
max2 = [pdates2[sensor_206.index(max(sensor_206))],max(sensor_206)]
max3 = [pdates3[sensor_11.index(max(sensor_11))],max(sensor_11)]
axs[0].plot(max1[0],max1[1],'ro')
axs[1].plot(max2[0],max2[1],'ro')
axs[2].plot(max3[0],max3[1],'ro')
axs[0].annotate(round(max1[1],1),(max1[0],max1[1]),color='red')
axs[1].annotate(round(max2[1],1),(max2[0],max2[1]),color='red')
axs[2].annotate(round(max3[1],1),(max3[0],max3[1]),color='red')
# Min
min1 = (pdates1[sensor_204.index(min(sensor_204))],min(sensor_204))
min2 = (pdates2[sensor_206.index(min(sensor_206))],min(sensor_206))
min3 = (pdates3[sensor_11.index(min(sensor_11))],min(sensor_11))
axs[0].plot(min1[0],min1[1],'bo')
axs[1].plot(min2[0],min2[1],'bo')
axs[2].plot(min3[0],min3[1],'bo')
axs[0].annotate(round(min1[1],1),(min1[0],min1[1]),color='blue')
axs[1].annotate(round(min2[1],1),(min2[0],min2[1]),color='blue')
axs[2].annotate(round(min3[1],1),(min3[0],min3[1]),color='blue')
# Mean
axs[0].axhline(sum(sensor_204)/len(sensor_204),color='cyan',alpha=0.7,label='mean')
axs[1].axhline(sum(sensor_206)/len(sensor_206),color='cyan',alpha=0.7,label='mean')
axs[2].axhline(sum(sensor_11)/len(sensor_11),color='cyan',alpha=0.7,label='mean')
# Median
axs[0].axhline(sorted(sensor_204)[len(pdates1)//2],color='magenta',alpha=0.7,label='median')
axs[1].axhline(sorted(sensor_206)[len(pdates2)//2],color='magenta',alpha=0.7,label='median')
axs[2].axhline(sorted(sensor_11)[len(pdates3)//2],color='magenta',alpha=0.7,label='median')
# Standard deviation
axs[0].annotate(f"s={round(np.std(sensor_204),2)}",(pdates1[-100],min([min(sensor_204),min(sensor_206),min(sensor_11)])),color='black')
axs[1].annotate(f"s={round(np.std(sensor_206),2)}",(pdates1[-100],min([min(sensor_204),min(sensor_206),min(sensor_11)])),color='black')
axs[2].annotate(f"s={round(np.std(sensor_11),2)}",(pdates1[-100],min([min(sensor_204),min(sensor_206),min(sensor_11)])),color='black')


# Plot and show
axs[0].legend()
axs[1].legend()
axs[2].legend()
plt.tight_layout()
plt.show()
