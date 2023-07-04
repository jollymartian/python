#Export/Import dataframe to csv

import numpy as np
import pandas as pd

political_figures = ['Franklin D. Roosevelt',
					'Winston Churchill',
					'Charles De Gaulle',
					'Nelson Mandela',
					'Deng Xiaoping']

countries = ['U.S.A', 'UK', 'France', 'South Africa', 'China']


#Create datafram using dictionary
politicians_dict = {'Politician Name': pd.Series(political_figures),
					'Country': pd.Series(countries)}

df_from_dict = pd.DataFrame(politicians_dict)
print(df_from_dict)

#create csv file to receive dataframe using pandas to_csv function
#Index argument specifies whether to export indexes as well. Column labels will be exported via headers argument.
#Check datasets folder exists in current directory to work
df_from_dict.to_csv('datasets/politicians.csv', index = False)

print("*****")

#Import from file using pandas read_csv function
politicians_from_file = pd.read_csv('datasets/politicians.csv')
print(politicians_from_file)