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

sensor_210 = []
sensor_12 = []
fdates1 = []
fdates2 = []
timeindex = []
t = 0

for r in readings:
    if r['sensor_id'] == 210:
        tf = timestamp_format(r['datetime'])
        year, month, date, hour, minute, second = tf[0],tf[1],tf[2],tf[3],tf[4],tf[5]
        if month == 12 and date == 5:
            print(r['datetime'],r['value'])
            # fdates1.append(f"{year}-{month}-{date} {hour}:{minute}:{second}")
            fdates1.append(f"{hour}:{minute}:{second}")
            timeindex.append(t)
            t += 1
            sensor_210.append(r['value'])
    if r['sensor_id'] == 12:
        tf = timestamp_format(r['datetime'])
        year, month, date, hour, minute, second = tf[0],tf[1],tf[2],tf[3],tf[4],tf[5]
        if month == 11 and date == 24:
            print(r['datetime'],r['value'])
            # fdates2.append(f"{year}-{month}-{date} {hour}:{minute}:{second}")
            fdates2.append(f"{hour}:{minute}:{second}")
            timeindex.append(t)
            t += 1
            sensor_12.append(r['value'])

# Define x axis
ax=plt.gca()


pdates1 = [dateutil.parser.parse(s) for s in fdates1]
pdates2 = [dateutil.parser.parse(s) for s in fdates2]

# Graph style
fig, axs = plt.subplots(2,sharex=True,sharey=True,figsize=(6,9))
fig.suptitle("Atmospheric Pressure Measurements Comparative Analysis")
axs[0].yaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel("Time/(Hours:Minutes)")
axs[1].set_ylabel("Atmospheric Pressure/hPa")

axs[0].plot(pdates1, sensor_210, color='grey')
axs[0].set_title('Local BME280 Dec 5th')
axs[1].plot(pdates2, sensor_12, color='grey')
axs[1].set_title('Remote BME280 Nov 24th')

plt.xticks( rotation= 80 )

# Plot hour:minute into x axis per hour
xfmt = md.DateFormatter('%H:%M')
axs[0].xaxis.set_major_formatter(xfmt)
axs[0].xaxis.set_major_locator(HourLocator(byhour=range(0, 24, 1), tz=None))
axs[1].xaxis.set_major_formatter(xfmt)
axs[1].xaxis.set_major_locator(HourLocator(byhour=range(0, 24, 1), tz=None))


# Max
max1 = [pdates1[sensor_210.index(max(sensor_210))],max(sensor_210)]
max2 = [pdates2[sensor_12.index(max(sensor_12))],max(sensor_12)]
axs[0].plot(max1[0],max1[1],'ro')
axs[1].plot(max2[0],max2[1],'ro')
axs[0].annotate(round(max1[1],1),(max1[0],max1[1]),color='red')
axs[1].annotate(round(max2[1],1),(max2[0],max2[1]),color='red')
# Min
min1 = (pdates1[sensor_210.index(min(sensor_210))],min(sensor_210))
min2 = (pdates2[sensor_12.index(min(sensor_12))],min(sensor_12))
axs[0].plot(min1[0],min1[1],'bo')
axs[1].plot(min2[0],min2[1],'bo')
axs[0].annotate(round(min1[1],1),(min1[0],min1[1]),color='blue')
axs[1].annotate(round(min2[1],1),(min2[0],min2[1]),color='blue')
# Mean
axs[0].axhline(sum(sensor_210)/len(sensor_210),color='cyan',alpha=0.7,label='mean')
axs[1].axhline(sum(sensor_12)/len(sensor_12),color='cyan',alpha=0.7,label='mean')
# Median
axs[0].axhline(sorted(sensor_210)[len(pdates1)//2],color='magenta',alpha=0.7,label='median')
axs[1].axhline(sorted(sensor_12)[len(pdates2)//2],color='magenta',alpha=0.7,label='median')
# Standard deviation
axs[0].annotate(f"s={round(np.std(sensor_210),2)}",(pdates1[-100],min([min(sensor_210),min(sensor_12)])),color='black')
axs[1].annotate(f"s={round(np.std(sensor_12),2)}",(pdates1[-100],min([min(sensor_210),min(sensor_12)])),color='black')


# Plot and show
axs[0].legend()
axs[1].legend()
plt.tight_layout()
plt.show()
