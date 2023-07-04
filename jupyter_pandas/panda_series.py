#Create a series - serial and associated data value

import pandas as pd 
import sys

#print(sys.version)
#print(pd.__version__)

data = ['Sunday',
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday']

#Create pandas series object. Similar to python list - but can use a sting for index rather than just number
week = pd.Series(data)

#Index auto created, data becomes values associated with indexes
print(week)

print("\n*****")

#Pandas built on top of numpy - abstraction of numpy arrays
import numpy as np

square_numbers = np.array([0, 1, 4, 9, 16, 25, 36, 49,
							64, 81,100, 121, 144, 169])

square_series = pd.Series(square_numbers)
print(square_series)

