#Part 2 Question 2 - Delayed Flights

#---------------------------------------------------------------------------------------------

import pandas as pdd
import calendar
# Importing the data:
flightsData = pd.read_csv('files\\flights.csv')
airportsData = pd.read_csv('files\\airports.csv')
airlinesData = pd.read_csv('files\\airlines.csv')

#---------------------------------------------------------------------------------------------

#Question 2.1: Query - Flights which departed late in the year 2015:
delayed2015 = flightsData.loc[(flightsData['YEAR']==2015) & (flightsData['DEPARTURE_DELAY']>0)]
print('Delayed flights in 2015:',delayed2015.count()['INDEX']) #note: I added an "INDEX" column for each row

#---------------------------------------------------------------------------------------------

#Question 2.2: Query - Day with the longest flight departure delay in 2015:
maxday = flightsData.loc[(flightsData['DEPARTURE_DELAY']==flightsData['DEPARTURE_DELAY'].max())&(flightsData['YEAR']==2015)].DAY_OF_WEEK
filtmaxday=maxday.to_string(index=False)

#Converting number of the day to name of the day:
convIntDay=int(filtmaxday)
convIntDay=-2 # Minus 2 for the function to match Israeli day numbers.
print('The day which had the worst delay was a',calendar.day_name[convIntDay],'.')

#---------------------------------------------------------------------------------------------

#Question 2.3: Largest Distance between two airports:

mask = flightsData['DISTANCE'] == flightsData['DISTANCE'].max()

aln = flightsData[mask]
aln.groupby(['AIRLINE'])
aln = aln.drop_duplicates(subset=['ORIGIN_AIRPORT','DESTINATION_AIRPORT'])
filtaln = aln['AIRLINE']
idx = filtaln.shape[0]
idxlist=[0,idx-1]


for x in idxlist:
     print('Largest Distance between two airports:',aln.iloc[x,18]) #Distance
     print('From Airport:',aln.iloc[x, 8]) #Origin Airport
     print('To Airport:',aln.iloc[x, 9])  #Destination Airport
     print('Flight took place on day: ',(aln.iloc[x, 4]))



#---------------------------------------------------------------------------------------------

#Question 2.4

#Merge flights and airlines:
flAirMerged = pd.merge(flightsData,airlinesData,left_on='AIRLINE',right_on='IATA_CODE',how="inner")

#Query: Airline=JetBlue Airways, Departure Delay>0, Select Tail Number
tailnum = flAirMerged['TAIL_NUMBER'][(flAirMerged['AIRLINE_y']=='JetBlue Airways')& (flAirMerged['DEPARTURE_DELAY']>0)]
print(tailnum)


