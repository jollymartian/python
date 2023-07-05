import pandas as pd

#Use head to view first 5 rows of dataframe to preview contents of dataframe
towed_cars = pd.read_csv('./datasets/Towed_cars.csv')
print(towed_cars.head())

print("\n******")

#nvoke values by referecning a column header
print(towed_cars['Color'])

print("\n******")

#Note double [[]] as passing a list not a single value
print(towed_cars[['Make', 'Color']])

print("\n******")

#To view as preview
print(towed_cars[['Make', 'Color']].head())

print("\n******")

#Specify the amount of preview
print(towed_cars[['Make', 'Color']].head(9))

print("\n******")

#Using tail for last values
print(towed_cars.tail())

print("\n******")

#Specify the row by index for all data in relation
print(towed_cars.loc[5])

print("\n******")

#Slice the dataframe
print(towed_cars.loc[4:10])

print("\n******")

#All values from rows with including columns between tow_firm and Vechicle year columns
print(towed_cars.loc[9 : , 'TowNum' : 'Vehicle_Year'])

print("\n******")