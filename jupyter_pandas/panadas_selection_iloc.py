import pandas as pd 

towed_cars = pd.read_csv('datasets/towed_cars.csv')
print(towed_cars)

#iloc only accepts integers. It will not accept column headers string.
#loc will also return row with index 6, iloc does not (upto 5 only)
print(towed_cars.iloc[2 : 6])

print("\n******")

#ERROR - iloc does not ccept string values
#print(towed_cars.iloc[2 : 6, 'Vehicle_Plate' : 'Color'])

#print("\n******")

#Values can be obtained as above commented out would invoke using integers as below
print(towed_cars.iloc[2 : 6, 3 : 7])

print("\n******")

#Specify multiple index values
print(towed_cars.iloc[[3 ,7 ,10], : ])

print("\n******")

#Select specific parts of dataframe on condition
print(towed_cars[towed_cars['Vehicle_Year'] > 2005])

print("\n******")

#Further selection
print(towed_cars[towed_cars['Vehicle_State'] == 'CT'])

print("\n******")

#Apply both conditions
print(towed_cars[(towed_cars['Vehicle_State'] == 'CT') & (towed_cars['Vehicle_Year'] > 2005)])

print("\n******")

#Further specific selection
print(towed_cars[(towed_cars['Vehicle_State'] == 'AL') | (towed_cars['Color'] == 'GRAY')])

print("\n******")

#Using not (~) - EG. not color blue
print(towed_cars[~(towed_cars['Color'] == 'BLUE')])

print("\n******")

