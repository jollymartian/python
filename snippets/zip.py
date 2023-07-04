#zip function can create tuples of data

capital_cities = ['London', 'Paris', 'Madrid']
countries = ['UK', 'Frnace', 'Spain']

#Use zip and list to create list of paired tuples
country_tuples = list (zip (capital_cities, countries))
print(country_tuples)