import pandas as pd
import sys
import numpy as np

#Values for index fields
employee_fields = ['f_name', 'l_name', 'emp_id', 'dept']

#Values for index data
employee_data = ['Susie', 'Schnieder', '2258788', 'Accounting']

print("\n*****")

#Create series object
employee_series = pd.Series(index = employee_fields, data = employee_data)

print(employee_series)

print("\n*****")

#Auto use key : values to issue index names and values
country_capitals_dict = {'Afghanistan': 'Kabul',
						'Austrlia': 'Canberra',
						'Bangladesh': 'Dhaka',
						'China': 'Beijing',
						'France': 'Paris'}

country_capital_series = pd.Series(country_capitals_dict)

print(country_capital_series)

print("\n*****")

#Take values and place into an array
print(country_capital_series.values)
print(type(country_capital_series.values))

print("\n*****")

#Returns Index values
print(country_capital_series.index)

print("\n*****")

#Use numerical positions to pull data
print(country_capital_series[0])
print(country_capital_series.index[3])

print("\n*****")

#Slice data
print(country_capital_series[1:5])

print("\n*****")

#Print value of index
print(country_capital_series['China'])

print("\n*****")

#Values of mulitple indexes
print(country_capital_series[['Afghanistan', 'France', 'Bangladesh']])

