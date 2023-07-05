import pandas as pd 

#Print dataframe in groups relating to region an date in sorted manner 
#Combination of region and date is t be used as index
avocados = pd.read_csv('datasets/avocado.csv', index_col = ['region', 'Date'])
print(avocados.sort_index())

print("\n******")

#Ensure the combo of index uniquely identifies to a row - Trim to roganic only
avocados = avocados[avocados['type'] == 'organic']
print(avocados)

print("\n******")

#Filter dataframe
avocados = avocados.loc[(avocados.index.get_level_values('Date') > '2018-03-01')]
print(avocados)

print("\n******")

#View index for dataframe - displays multi-index with defined levels
print(avocados.index)

print("\n******")

#Use pivot table from panadas_reshape
avocados = pd.read_csv('datasets/avocado.csv')
avocados['region'].unique()
avocados_totalUS = avocados[(avocados['region'] == 'TotalUS') & (avocados['Date'] > '2018-01-01')]
avocados_totalUS = avocados_totalUS.sort_values(['Date'])
avocados_pivot = avocados_totalUS.pivot(index = 'Date',
										columns = 'type',
										values = 'AveragePrice')
print(avocados_pivot.head())

print("\n******")

#Stack operation stacks the contents of a single row into multiple rows
#Combines data by sacking mutiple rows into one
avocados_stack = avocados_pivot.stack()
print(avocados_stack)

print("\n******")

#Unstack to recover
avocados_unstack = avocados_stack.unstack()
print(avocados_unstack)

print("\n******")

#lose the pivot for examples below - reload csv
avocados = pd.read_csv('datasets/avocado.csv', index_col = ['region', 'Date'])
avocados = avocados[avocados['type'] == 'organic']
avocados = avocados.loc[(avocados.index.get_level_values('Date') > '2018-03-01')]

#View index for dataframe - displays multi-index with defined levels
print(avocados.index)

print("\n******")

#Stack multiindex
avocados_multiindex_stack = avocados.stack()
print(avocados_multiindex_stack)

print("\n******")

#Melt function - reload csv
#Melt will produce a dataframe with one row for each {ID_Combo, Value_var}
avocados = pd.read_csv('datasets/avocado.csv')
avocados = avocados[avocados['Date'] > '2018-03-01']
#ID var for columns / measured variables for values
avocados_melted = avocados.melt(id_vars = ['region', 'type', 'Date'],
	value_vars = ['AveragePrice', 'Total Volume'])
print(avocados_melted)

print("\n******")



