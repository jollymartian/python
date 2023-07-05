import pandas as pd
import numpy as np

politicians_from_file = pd.read_csv('datasets/politicians.csv')
print(politicians_from_file)

print("\n*****")

#Add column 'Year of birth' with value '1900' (single value) to dataframe
politicians_from_file["Year of birth"] = 1900
print(politicians_from_file)

print("\n*****")

#Add column 'Year of Birth' and list to provide multiple values'.
#As column already exists it overwrites the column values
politicians_from_file["Year of birth"] =[1881,
										1882,
										1883,
										1884,
										1885
										]
print(politicians_from_file)

print("\n*****")

#Delete column
del politicians_from_file["Year of birth"]
print(politicians_from_file)

print("\n*****")

#Add new row with index (-1).
#If row with index -1 doesn't exist it create a new row. If it does, it overwites.
politicians_from_file.loc[-1] = ['Otto van Bismark', 'Germany']
print(politicians_from_file)

print("\n*****")

#Modify index - increment index values by 1
politicians_from_file.index = politicians_from_file.index +1
print(politicians_from_file)

print("\n*****")

#Sort indexes - index() does ascending numerical order
politicians_from_file = politicians_from_file.sort_index()
print(politicians_from_file)

print("\n*****")

#Drop an row by index value
politicians_from_file = politicians_from_file.drop(politicians_from_file.index[5])
print(politicians_from_file)

print("\n*****")

#Set custom index values for rows
row_values=[111, 222, 333, 444, 555]
politicians_from_file.index = row_values
print(politicians_from_file)

print("\n*****")

#Reset indexes
politicians_from_file = politicians_from_file.reset_index()
print(politicians_from_file)

print("\n*****")

#Delete new index column using drop
politicians_from_file = politicians_from_file.drop(columns=['index'])
print(politicians_from_file)