import pandas as pd

#Create empty datafram using dataframe constructor in pandas
empty_dataframe = pd.DataFrame()
#Print empty dataframe
print(empty_dataframe)

print("\n******")

political_figures = ['Franklin D. Roosevelt',
					'Winston Churchill',
					'Charles De Gaulle',
					'Nelson Mandela',
					'Deng Xiaoping']

#Create dataframe of political figures
df_from_list = pd.DataFrame(political_figures)
print(df_from_list)

print("\n******")

#Create another list to create key and values
countries = ['U.S.A', 'UK', 'France', 'South Africa', 'China']

#Create tuples for each pairing using zip function
politician_tuples = list (zip(political_figures, countries))

print(politician_tuples)

print("\n******")

df_from_list_of_tuples = pd.DataFrame(politician_tuples)
print(df_from_list_of_tuples)

print("\n******")

#Reload data with column names
df_from_list_of_tuples = pd.DataFrame(politician_tuples, columns = ['Politician Name', 'Country'])
print(df_from_list_of_tuples)

print("\n******")

#Create datafram using dictionary
politicians_dict = {'Politician Name': pd.Series(political_figures),
					'Country': pd.Series(countries)}

df_from_dict = pd.DataFrame(politicians_dict)
print(df_from_dict)