# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition

My client, L.Y., has developed a new interest in the fascinating world of hydroponics. He decided to keep one specimen of hydroponics in his room for personal use and potentially academic experiments. He occasionally puts the plant out to a different location in the campus when the room environment is too unsuitable. Yet after a week of closely paying attention to and maintaining proper care for the plant, he realized that the plant showed some alarming visual signs of weakening color and general shape. After some online investigation, he had determined that the possible cause of this problem was the temperature of the room where the plant was kept being too low, the humidity levels being too high or perhaps too low, and the atmospheric pressure being lower due to the high altitude. Based on this knowledge, he felt that he needed to carefully monitor and successfully manage those particular variables that, one way or another, had a strong influence on the growth and overall health of the plant. Additionally, he wants to determine when and how long the plant should be located in the alternate position. Overall, my client is concerned about the lack of environmental monitoring capabilities both indoors and outdoors, for the wellbeing of his plant.

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity, temperature and atmospheric pressure, and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Additionally, BME280 sensor is an affordable, satisfactory contender for providing high accuracy atmospheric pressure data through I2C communication, one of the required variables for the client (Pressure range: 300hPa to 1100 hPa)[^5]. Connecting the DHT11 sensor and BME280 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Raspberry Pi 3b+ single-board computer [^3]. "The Raspberry Pi is a very cheap computer that runs Linux, but it also provides a set of GPIO (general purpose input/output) pins, allowing you to control electronic components for physical computing and explore the Internet of Things (IoT)."[^4]. In additon to the low cost of the Raspberry Pi (< 60USD), this device is programable and expandable, with features such as internet connection[^4]. I considered alternatives such different versions of the Raspberry Pi but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability without the need for extensive redevelopment. [^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  


## Success Criteria

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:“What is a Raspberry Pi?” opensource.com | Red Hat, Inc., https://opensource.com/resources/raspberry-pi  
[^5]:BOSCH. "Humidity sensor BME280" Bosch Sensortec GmbH, https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]:Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
[^8]:Matplotlib Development Team. "Matplotlib: Visualization with Python", https://matplotlib.org/
[^9]:Kenneth Reitz. "Requests: HTTP for Humans", https://requests.readthedocs.io/en/latest/

1. The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. ```** [Issue tacled] **: My client's lack of environmental monitoring equipments has been resolved now. ```
2. The local variables will be measure using a set of sensors around the dormitory.```** [Issue tacled] **: Client can get more accurate data for both indoor and outdoor conditions. ```
3. The solution provides a mathematical modelling for the Humidity, Temperature and atmospheric pressure levels for each Local and Remote locations. ```** [Issue tacled] **: It captures the tendency of the data and makes it easy to read, therefore it is appropriate for daily use. ```
4. The solution provides a comparative analysis for the Humidity, Temperature and atmospheric pressure levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median. ```** [Issue tacled] **: The solution highlights potential disparities and their implications for plant growth.  ```
5. The Local samples are posted to the remote server as a backup. ```** [Issue tacled] **: It ensures data integrity and accessibility for future reference and analysis.```
6. The solution provides a prediction for the subsequent 12 hours for Humidity, Temperature and atmospheric pressure. ```** [Issue tacled] **: By foreseeing the values, my client can take timely actions even in his busy times.```
7. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature and atmospheric pressure . ```** [Issue tacled] **: It provides concise and clear documentation for academic or other purposes.```

_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change_

1. How does our use of technology shape our understanding of the environment
```Technology greatly influences the perception of the environment because of the delivery of data, quite accurately and in real-time, that would have been impossible to retrieve without such systems. These data provide the capability of detecting subtle changes and patterns in environmental conditions that might not have been detected otherwise. But at the same time, it has to be recognized that it is our very technological toolsets that frame the perspective and so must considered. ```
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
```As personal data management technologists, interested in living spaces, data privacy and security should be observed. Transparency is needed in the methods of collection, storage, and usage of data, and consent shall be informed and obtained from the persons in whose living spaces the monitoring is conducted. Further, we are ethically committed to handling this kind of data responsibly, never misusing or exploiting personal information of any kind. ``` 
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 
```While cultural and contextual factors are generally important in data interpretation, their impact is minimal in our case of comparing local data to that of the school. Our focus on standardized measurements of temperature, humidity, and atmospheric pressure ensures objectivity, minimizing subjective influences. Any variations we observe are more likely due to differences in measurement locations or equipment rather than cultural interpretations.```


# Criteria B: Design

## System Diagram
![System Diagrams unit 2 (2)](https://github.com/user-attachments/assets/36775cba-6730-45d3-bccb-57b4d8a8179d)

**Fig.1** Fig. 1 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides and API for remote monitoring and storage (192.162.6.173) via the ISAK-S network. A laptop for remote work is included.


## Flow diagrams for algorithms
![image](https://github.com/user-attachments/assets/ca365701-0527-4dfe-9d98-3040e1117661)

**Fig.2**  This flowchart describes the process of continuously reading sensor data, extracting relevant information, and sending it to a server for further processing. The process is repeated indefinitely, with a delay of 1 second between each iteration and a pause of 1 minute between each measurement.

![image](https://github.com/user-attachments/assets/9ea1d165-8287-402b-b5ad-f920c1c2facc)



**Fig.3** The flowchart demonstrates a smoothing function that reduces noise in a given dataset. It takes a window size and a list of raw data as input. The function iterates through the data, calculates the average of a window of data points, and appends the average to a new list. This process continues until all data points are processed, resulting in a smoothed dataset.





![image](https://github.com/user-attachments/assets/6cdab434-2982-4260-8f15-9b59e9d2d0f0)


**Fig.4** The flowchart outlines a process for fetching data from a server, filtering it based on a specific sensor ID, and then plotting the filtered data over time. The data is processed and visualized using various libraries, and a smoothing technique is applied to the plot for better readability.




## Data storing method

### Online API Server
The data of temperature, humidity, and pressure is being stored in an online API server: http://192.168.4.137/readings. Every 1 minute for 48 hours, the program will send data to the server. As there are 2 sensors, each minute, the server will receive a total of 5 data: 2 temperature data (DHT11 and BME280), 2 humidity data (DHT11 and BME280), and 1 atmospheric pressure data (only BME280) . The data will be sent to the server in a particular format. The following is an example of the 5 data sent each time:
```.py

{"sensor_id": 203, "value": 18.0, "datetime": "2024-12-04T22:40:00.016697", "id": 6181253}, {"sensor_id": 204, "value": 31.0, "datetime": "2024-12-04T22:40:00.016697", "id": 6181254}, {"sensor_id": 206, "value": 29.813148, "datetime": "2024-12-04T22:40:00.016697", "id": 6181255}, {"sensor_id": 210, "value": 884.3764, "datetime": "2024-12-04T22:40:00.016697", "id": 6181256}, {"sensor_id": 205, "value": 18.399817, "datetime": "2024-12-04T22:40:00.016697", "id": 6181257}

```
Each data tells different information separated by commas, the first element tells the sensor id of one of the DHT 11 and BME280 sensors and each sensor represents some of temperature, humidity, and pressure. We set the sensors as follows :
1. Sensor id 203 - the temperature sensor of DHT11
2. Sensor id 204 - the humidity sensor of DHT11 
3. Sensor id 205 - the temperature sensor of BME280 
4. Sensor id 206 - the humidity sensor of BME280 
5. Sensor id 210 - the pressure sensor of BME280 

The second element, “value”, tells the value of either temperature(celcius), humidity(%), and the pressure(hPa). The third element “datetime”, tells the date (Year-Month-Day) and the time in hours, minutes, seconds, and milliseconds. The fourth element, “id” shows the id of the data. 

For example, this data, {"sensor_id": 203, "value": 18.0, "datetime": "2024-12-04T22:40:00.016697", "id": 6181253}, shows that the sensor detects temperature as the sensor id is “203”. It also shows that the temperature is 18 degrees Celsius, the id of this sensor is 6181253, and the date of the data is 4th December 2024 at 8pm 40 minutes.

![image](https://github.com/user-attachments/assets/c5585a8d-6fdd-462e-99c8-4dfe81f1b9d1)


**Fig.5** Shows a section of the online API server http://192.168.4.137/readings where the data is being stored in real time every 1 minute

## Test Plan
| Test NO | Test Goal                                                                                                                                                                                                  | Test Description                                                                                                                                                             | Supposed Outcome                                                                              | Pass/Error |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------|
| 1       | Verify that the system displays a visual representation of humidity, temperature,  and atmospheric pressure for both local (dormitory) and remote (outside) locations  for at least the past 48 hours.     | Run the codes Abme280_dec4a5.py,Armt_nov24a25.py, Hbme280_dec4a5.py,Hdht11h_dec4a5.py,Hrmt_nov24a25.py, Tbme280_dec4a5.py,Tdht11_dec4a5.py,Trmt_nov24a25.py for  each graph | For each code, output  showing the graph of  spesific value over 48 hours                     |            |
| 2       | Verify that the local humidity, temperature, and atmospheric pressure values  are measured using a set of sensors placed around the dormitory.                                                             | Check the evidence in documentation.md in github repository                                                                                                                  | Photos of location and  a set of sensors                                                      |            |
| 3       | Verify that the graphs provide a mathematical model for values from both  local and remote sensors.                                                                                                        | Check whether there are octic lines in the graphs shown in the poster                                                                                                        | There are octic lines  in every graph                                                         |            |
| 4       | Verify that the solution provides a comparative analysis of values from both local and remote sensors, including statistical measures like mean, standard deviation, minimum, maximum, and median.         | For temperature run comparative_temperature.py, For humidity run comparative_humidity.py, For pressure run comparative_pressure.py                                           | For the graph of each code, there are mean, standard deviation,  minimum, maximum, and median |            |
| 5       | Verify that the local data is being sent to the remote server as a backup.                                                                                                                                 | Go to the link http://192.168.4.137/readings, check the values with the sensor id of 203,204, 205,206, and 210                                                               | In that link values with mentioned sensor ids                                                 |            |
| 6       | Verify that the solution provides accurate predictions for from both local  and remote sensors values for the next 12 hours.                                                                               | Run the codes prediction_temperature.py and  prediction_humidity.py (take it from github repository-source codes)                                                            | For each graph, the output showing the  prediction graphs for subsequent 12 hours             |            |
| 7       | Verify that the system includes a poster summarizing the visual representations,  model, and analysis, and provides recommendations for healthy levels of Humidity, Temperature, and atmospheric pressure. | Check the evidence in github repository                                                                                                                                      | Poster with the required features                                                             |            |                                                          |                 |            |

## Record of Tasks
| Task No | Planned Action                                                                                              | Planned Outcome                                                                              | Time Estimate | Target Completion Date | Criterion |
|---------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | 1st Meeting with the client                                                                                 | To obtain a problem definition, understanding what the situation is                          | 30 min        | November 29            | A         |
| 2       | Presenting our draft solution to the client                                                                 | To discuss success criterions and getting confirmation                                       | 30 min        | November 30            | A         |
| 3       | Connect and set up Raspberry Pi                                                                             | To figure out and look up how to use the Raspberry PI 3                                      | 1 hour        | November 30            | C         |
| 4       | Install necessary Python libraries like requests, datetime, pytz, dht11, BME280, matplotlib, and so on.     | A ready Python environment for data collection and analysis                                  | 40 min        | November 30            | C         |
| 5       | Create a system diagram and share it with client                                                            | To have a clear idea of the hardware and software  requirements for the proposal solution    | 1 hour        | December 1             | B         |
| 6       | Wiring DHT11 and BME280 sensors to the raspberry pi                                                         | To get physically connected sensors ready for data acquisition                               | 30 min        | December 1             | B         |
| 7       | Develop a Python code to read the sensor data                                                               | A working code that collects sensor data                                                     | 30 min        | December 2             | C         |
| 8       | Develop a code in the Raspberry Pi to connect to the ISAK server using the provided API                     | Successful connection to the server for data transmission                                    | 30 min        | December 2             | C         |
| 9       | Write a code to send sensor data to the server at regular intervals                                         | Regular and reliable data transmission to the server                                         | 30 min        | December 3             | C         |
| 10      | Develop a program to get the outside measurements from ISAK server                                          | To complete outdoors data requirement of the project                                         | 30 min        | December 3             | C         |
| 11      | Develop Python program using Matplotlib to create various visualizations of 48-hour data                    | To get visual representations of the collected data for our scientific poster                | 1 hour        | December 4             | C         |
| 12      | Implement Data Filtering and Smoothing using techniques like moving average and so on                       | To get cleaner and more accurate sensor data                                                 | 1 hour        | December 4             | C         |
| 13      | Develop models to predict future trends of next 12 hours using 48-hour data                                 | To get predictive models for temperature, humidity, and pressure                             | 2 hours       | December 5             | C         |
| 14      | Creating 3 flowcharts for the algorithms used for data acquisition, transmission, and mathematical modeling | To get deeper understanding of how the algorithms of my program work                         | 4 hours       | December 5             | B         |
| 15      | Create a test plan                                                                                          | To ensure that program fulfills the success criterions                                       | 2 hours       | December 6             | B         |
| 16      | Document the list of techniques used for coding part                                                        | To make documentation of the coding part more understandable                                 | 2 hours       | December 6             | C         |
| 17      | Give information about our data storing method- API server                                                  | To give description of the data format used                                                  | 1 hour        | December 7             | C         |
| 18      | To create scientific poster showing the visualization of the data and mathematical modeling                 | To accurately reflect the project's focus                                                    | 3 hours       | December 7             | C and D   |
| 19      | Take 7 min video demonstrating the proposed solution with narration                                         | To achieve clear and concise explanation of the project, its results, and its implementation | 2 hours       | December 8             | D         |


# Criteria C: Development

## List of techniques used

1. API communication with remote server
2. Filtering using moving average
3. Plotting x-axis with hourly format

### 1. API communication with remote server

To solve SC#5: data backup to a remote server, and address SC#1/SC#3/SC#4: acquire data from a remote location, we needed a way to pull and push data to a server from both Raspberry Pi and personal computer. We used UWC ISAK Japan Weather API as our server: a centralized database for values such as temperature, humidity and atmospheric pressure measured regularly on campus. In order to communicate with the server, we used an HTTP python library called Requests, which enable us to get and post data with simple coding[^9].
```.py
import requests

server_ip = '192.168.4.137'
request = requests.get(f'http://{server_ip}/readings')
data = request.json()
readings = data['readings'][0]

sensor_205 = []

for r in readings:
    if r['sensor_id'] == 205:
        print((r['value'],r['datetime']))
```
This is a basic representation of the pulling procedure to the personal computer from the server. The program first specifies the IP address of the server, then uses the .get method, which sends a GET request to the specified url. To the returned JSON response object, using .json() converts the body into a python object, in this case a dictionary. With appropriate arrangement of key access and "if" conditions, the program can acquire the desired data from a specific sensor or datetime.

```.py
import requests

server_ip="192.168.4.137"
user={ 'username':'example','password':'example'}

answer= requests.post(f'http://{server_ip}/login', json=user)
cookie=answer.json()['access_token']

auth = {"Authorization": f"Bearer {cookie}"}
new_record = {"sensor_id":203, "value":temp_dht, "datetime":now}  # temp_dht: value read from DHT11  now: datetime.now()
answer = requests.post(f'http://{server_ip}/reading/new', json = new_record, headers = auth)
```
This is a basic representation of the upload procedure from the Raspberry Pi to the server. Authorization is done using the .post method towards the login url, which will send a POST request with the username and password for a user which already had been registered to the server. Its answer provides an access token which can be used for the header for posting the sensor values. The posting of the data is also done using the .post method but now directed towards new readings url, taking the dictionary object which will be converted to json.

### 2. Filtering using moving average

To solve SC#1 I encounter the problem that the values from teh sensors are noisy due to the changes in the
temperature and other variables. I thougt about using an algorithm to filter the data and smooth it. After some reseach
I decided to use the moving average. To make things more sustainable and organized I decided to use a function to
implemented the moving average and placed it in a library.
```.py
def moving_average(windowSize:int, x:list)->list:
    # this function has a purpose to increase the readability of the graph by regulating the oscillation of the data.
    # the output is the smoothed list
    x_smoothed = []
    for i in range(0, len(x)-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section)/windowSize
        x_smoothed += [x_average]

    return x_smoothed
```
In the code above, we can see that the function signature includes two inputs, ```windowSize:int ``` is the size used for filtering which is of
data type integer that decides the range of values which the function will generate averages from, into ```x_smoothed```. Another input is ```x```, which is a list that the function will apply the smoothing to. All the values in ```x``` are intended to be integers or floats.

### 3. Plotting x-axis with hourly format

To solve SC#1/SC#4, that requires a visual representation of the data, we used matplotlib: a comprehensive library for creating static, animated, and interactive visualizations in Python[^8]. Its simple two dimentional graph plotting methods allow users to plot y values that correspond with the values in the x-axis. However, we realized that there are occasional skips in the data, so if we plot the graphs with equal intervals for x (time), the labels for the ticks will not indicate roundnumbers. We struggled for a long time to find a solution to this problem using our knowledge, so we conducted internet research and found out how to force the format of the x-axis into hourly ticks using methods in Matplotlib.
```.py
# ax: current x axis (plt.gca())

xfmt = matplotlib.dates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.xaxis.set_major_locator(HourLocator(byhour=range(0, 24, 1), tz=None))
```
```DateFormatter``` is a formatter that will create hourly ticks. ```set_major_formatter``` is a formatter that apply a format to major ticks in the x-axis, that has been set to hourly ticks in this program. ```HourLocator``` is a locator of labels which distribute the value from 0 to 24 with 1 step, which is applied through the use of ```set_major_locator```.

# Criteria D: Functionality

Youtube link: https://youtu.be/PFyvl0cmCiM
