#Part 2 Question 4

#---------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calendar
# Importing the data:
flightsData = pd.read_csv('files\\flights.csv')
airportsData = pd.read_csv('files\\airports.csv')
airlinesData = pd.read_csv('files\\airlines.csv')

#---------------------------------------------------------------------------------------------

#Visualization of departure delays by flight index:
plt.plot(flightsData.DEPARTURE_DELAY)
plt.ylabel('Delay in Departures [min]')
plt.xlabel('flight index')
plt.show()
