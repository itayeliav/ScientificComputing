#Part 2 Question 1 - Intro

#-----------------------------------------------------------------------

import pandas as pd
flightsData = pd.read_csv('files\\flights.csv')
airportsData = pd.read_csv('files\\airports.csv')
airlinesData = pd.read_csv('files\\airlines.csv')

#-----------------------------------------------------------------------

#Question 1.1
print("Rows:", flightsData.shape[0]) # prints number of rows

#Question 1.2
for col in flightsData.columns: #prints each column's name
    print(col)

#Question 1.3
print("Rows:", airportsData.shape[0]) # prints number of rows


for col in airportsData.columns: #prints each column's name
    print(col)

#Question 1.4
print("Rows:", airlinesData.shape[0]) # prints number of rows


for col in airlinesData.columns: #prints each column's name
    print(col)

#Question 1.5
#Conclusions:
# Each flight has Airline, Airport and Airport Code (IATA_CODE)
# Airport Code column (IATA_CODE) can be used as the foreign key to the Airport Table (which makes the airport column in flights redundant).
# Same conclusion goes to the Airline Code column (IATA_CODE) in the airlines file.
# Problem: Both of the foreign keys mentioned above have the same column name (IATA_CODE) which could cause problems of ambiguity using the column's name.
# Solution: IATA_CODE column name should be changed to Airplane_Code and Airport_Code in order to avoid future complications.
