#Indexes/Keys must be unique

#Example dictionary 1
print("Example 1:")
dict_1 = {'John': 50, 'Paul': 100, 'Jones': 275}
#Printing the dictionary prints as expected
print(dict_1)

#Example dictionary
print("\nExample 2:")
dict_2 = {'John': 50, 'Paul': 100, 'Jones': 275, 'Paul': "Overwritten Value!"}
#There are two 'Paul' indexes/keys. This means the latest value in the list will be assigned
#to the original 'Paul' index in the middle of list
print(dict_2)

#Reassign index 'Paul' to 'Paul_1'
print("\nExample 3:")
dict_2 = {'John': 50, 'Paul': 100, 'Jones': 275, 'Paul_1': "Overwritten Value!"}
#Paul and Paul_1 are now unique and their values are associated as expected
print(dict_2)

#When using zip() to create dictionaries from lists this is also relevant
print("\nExample 4:")
#People and number lists for demo 
people = ['John', 'Paul', 'Jones', 'Paul']
people_1 = ['John', 'Paul', 'Jones', 'Paul_1']
number = [50, 150, 275, 'Overwritten Value!']
#Print to see same result as having to of the same indexes/keys 'Paul'
zipped_dict_1 = dict(zip(people, number))
print(zipped_dict_1)
#Using people_1 with unique values works
zipped_dict_2 = dict(zip(people_1, number))
print(zipped_dict_2)
