#Part 2 Question 3 - Canceled Flights

#---------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing the data:
flightsData = pd.read_csv('files\\flights.csv')
airportsData = pd.read_csv('files\\airports.csv')
airlinesData = pd.read_csv('files\\airlines.csv')

#---------------------------------------------------------------------------------------------

#Qurstion 3.1: Counting Canceled flights:
canceled = flightsData[(flightsData['CANCELED']>0)&(flightsData['YEAR']==2015)]
print('Canceled flights in 2015:', canceled.shape[0])

#---------------------------------------------------------------------------------------------

#Question 3.2: Most common reason for cancelation:

print(flightsData['CANCELLATION_REASON'].value_counts())
flightsData['CANCELLATION_REASON'].value_counts().plot(kind='bar')
plt.xlabel('Cancelation Reason')
plt.ylabel('Frequency')
plt.title('Frequency of Cancellation Reasons')
plt.show()

#---------------------------------------------------------------------------------------------

#Question 3.3: Percentage of delayed flights:

notcanceled=(flightsData.groupby('CANCELED').count().iloc[0]['INDEX'])
canceled=(flightsData.groupby('CANCELED').count().iloc[1]['INDEX'])
sum = notcanceled + canceled
notCanPer = notcanceled/sum*100
CanPer = canceled/sum*100
print('Percentage of flights which were not canceled::',"{0:.2f}".format(notCanPer),'%')
print('Percentage of flights which were canceled::',"{0:.2f}".format(CanPer),"%")

