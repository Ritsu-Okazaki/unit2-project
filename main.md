# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition

My client, Luke Yang, has developed a new interest in the fascinating world of hydroponics. He decided to keep one specimen of hydroponics in his room for personal use and potentially academic experiments. He occasionally puts the plant out of the balcony for additional sunlight. Yet after a week of closely paying attention to and maintaining proper care for the plant, he realized that the plant showed some alarming visual signs of weakening color and general shape. After some online investigation, he had determined that the possible cause of this problem was the temperature of the room where the plant was kept being too low, the humidity levels being too high or perhaps too low, and the atmospheric pressure being lower due to the high altitude. Based on this knowledge, he felt that he needed to carefully monitor and successfully manage those particular variables that, one way or another, had a strong influence on the growth and overall health of the plant. Additionally, he wants to determine when and how long the plant should be located outdoors. Overall, my client is concerned about the lack of environmental monitoring capabilities both indoors and outdoors, for the wellbeing of his plant.

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

1. The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure (HL) values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. ```** [Issue tacled] **: My client's lack of environmental monitoring equipments has been resolved now. ```
1. The local variables will be measure using a set of sensors around the dormitory.```** [Issue tacled] **: Client can get more accurate data for both indoor and outdoor conditions. ```
2. The solution provides a mathematical modelling for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations. ```** [Issue tacled] **: It captures the tendency of the data and makes it easy to read, therefore it is appropriate for daily use. ```
3. The solution provides a comparative analysis for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median. ```** [Issue tacled] **: The solution highlights potential disparities and their implications for plant growth.  ```
4. The Local samples are posted to the remote server as a backup. ```** [Issue tacled] **: It ensures data integrity and accessibility for future reference and analysis.```
5. The solution provides a prediction for the subsequent 12 hours for Humidity, Temperature and atmospheric pressure (HL). ```** [Issue tacled] **: By foreseeing the values, my client can take timely actions even in his busy times.```
6. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature and atmospheric pressure (HL). ```** [Issue tacled] **: It provides concise and clear documentation for academic or other purposes.```

_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change_

1. How does our use of technology shape our understanding of the environment
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 

# Criteria B: Design

## System Diagram
![System Diagrams unit 2 (2)](https://github.com/user-attachments/assets/36775cba-6730-45d3-bccb-57b4d8a8179d)

**Fig.1** Fig. 1 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides and API for remote monitoring and storage (192.162.6.173) via the ISAK-S network. A laptop for remote work is included.

## Record of Tasks
% Please add the following required packages to your document preamble:
% \usepackage[table,xcdraw]{xcolor}
% Beamer presentation requires \usepackage{colortbl} instead of \usepackage[table,xcdraw]{xcolor}
\begin{table}[]
\begin{tabular}{|l|l|l|l|ll}
\cline{1-4}
Task No & Planned Action                                                                                                                                                   & Planned Outcome                                                                                                                        & Time Estimate                 & Target Completion Date & Criterion \\ \cline{1-4}
1       & Create the problem context                                                                                                                                       & \begin{tabular}[c]{@{}l@{}}To get detailed insight into how the problem can be \\ solved and to choose best suited tools.\end{tabular} & {\color[HTML]{000000} 30 min} & Nov 29                 & A         \\ \cline{1-4}
2       & Connect to Raspberry PI                                                                                                                                          & To learn the various ways that Raspberry PI can be used                                                                                & 30 min                        & Nov 30                 & C         \\ \cline{1-4}
3       &                                                                                                                                                                  & \begin{tabular}[c]{@{}l@{}}Display an error message\\ indicating invalid currency.\end{tabular}                                        & Pass                          &                        &           \\ \cline{1-4}
4       & \begin{tabular}[c]{@{}l@{}}Enter an amount with both numeric and non-numeric characters \\ (e.g., "100abc") for the amount to convert.\end{tabular}              & \begin{tabular}[c]{@{}l@{}}Display an error message\\ indicating invalid amount.\end{tabular}                                          & Pass                          &                        &           \\ \cline{1-4}
5       & \begin{tabular}[c]{@{}l@{}}Enter an amount with multiple decimal points \\ (e.g., "10.12.13") for the amount to convert.\end{tabular}                            & \begin{tabular}[c]{@{}l@{}}Display an error message \\ indicating invalid amount.\end{tabular}                                         & Pass                          &                        &           \\ \cline{1-4}
6       & \begin{tabular}[c]{@{}l@{}}Enter an amount with only non-numeric characters \\ (e.g., "abc.abc") for the amount to convert.\end{tabular}                         & \begin{tabular}[c]{@{}l@{}}Display an error message \\ indicating invalid amount.\end{tabular}                                         & Pass                          &                        &           \\ \cline{1-4}
7       & Enter the secret code "unique" for the amount to convert.                                                                                                        & Switch to password manager mode.                                                                                                       & Pass                          &                        &           \\ \cline{1-4}
8       & \begin{tabular}[c]{@{}l@{}}Enter a number out of range(1-6) \\ (e.g., "15") for the operation to perform.\end{tabular}                                           & \begin{tabular}[c]{@{}l@{}}Display an error message \\ indicating invalid operation number.\end{tabular}                               & Pass                          &                        &           \\ \cline{1-4}
9       & \begin{tabular}[c]{@{}l@{}}Enter a number in a range(1-6) \\ (e.g., "5") for the operation to perform.\end{tabular}                                              & \begin{tabular}[c]{@{}l@{}}Properly functions the operation \\ and asks for an app number\end{tabular}                                 & Pass                          &                        &           \\ \cline{1-4}
10      & \begin{tabular}[c]{@{}l@{}}Enter an input with non-numeric symbols \\ (e.g., "23wfjw.9?") for the operation number to perform.\end{tabular}                      & \begin{tabular}[c]{@{}l@{}}Display an error message \\ indicating invalid operation number.\end{tabular}                               & Pass                          &                        &           \\ \cline{1-4}
11      & \begin{tabular}[c]{@{}l@{}}Enter a number out of range(1-8(length of app list)) \\ (e.g., "15") for the app number to perform a selected operation.\end{tabular} & \begin{tabular}[c]{@{}l@{}}Display an error message \\ indicating invalid app number.\end{tabular}                                     & Pass                          &                        &           \\ \cline{1-4}
12      & \begin{tabular}[c]{@{}l@{}}Enter a number in a range(1-8(length of app list)) \\ (e.g., "5") for the app number to perform a selected operation.\end{tabular}    & \begin{tabular}[c]{@{}l@{}}Properly operates with selected \\ application\end{tabular}                                                 & Pass                          &                        &           \\ \cline{1-4}
13      & \begin{tabular}[c]{@{}l@{}}Enter an input with non-numeric symbols\\ (e.g., "1.rt45?") for the app number to perform a selected operation.\end{tabular}          & \begin{tabular}[c]{@{}l@{}}Display an error message \\ indicating invalid app number.\end{tabular}                                     & Pass                          &                        &           \\ \cline{1-4}
14      & Enter an existing app name for adding to the password manager                                                                                                    & \begin{tabular}[c]{@{}l@{}}Display an error message indicating that\\ the app is in already password manager\end{tabular}              & Pass                          &                        &           \\ \cline{1-4}
\end{tabular}
\end{table}

## Test Plan

# Criteria C: Development (around 1000 word max)

## List of techniques used

1. API communication with remote server
2. Filtering using moving average
3. 

### 1. Filtering using moving average

Things to explain: a) what problem are you trying to solve (what success criteria), b) demonstrate your technical
understanding, c) algorithmic thinking.

Ex: To solve SC#1 I encounter the problem that the values from teh sensors are noisy due to the changes in the
temperature and other variables. I thougt about using an algorithm to filter the data and smooth it. After some reseach
I decided to use the moving average. To make things more sustainable and organized I decided to use a function to
implemented the moving average and placed it in a library.
```.py
def moving_average(windowSize:int, x:list)->list:
    # this function  has a purpose XXXX
    #The inputs are XXXXX
    # the output is xxxx
    x_smoothed = []
    for i in range(0, len(x)-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section)/windowSize
        x_smoothed += [x_average]

    return x_smoothed
```
In the code above, we can see that the function signature includes two inputs, ```windowSize:int ``` is the size used for filtering which is of
data type integer.....


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
