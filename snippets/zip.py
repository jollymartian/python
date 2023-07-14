#zip function can create tuples of data

capital_cities = ['London', 'Paris', 'Madrid']
countries = ['UK', 'Frnace', 'Spain']

#Use zip and list to create list of paired tuples
country_tuples = list (zip (capital_cities, countries))
print(country_tuples)

#Multiple values
population = [80_000_000, 120_000_000, 100_000_000]

country_tuples = list (zip (capital_cities, countries, population))
print(country_tuples)

#To create a dictionary using zip
dict_1 = dict(zip(capital_cities, countries))
