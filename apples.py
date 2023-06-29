"""Script for working out toal apples and average apples"""

#Assign number of apples to each person using variables
john = 3
mary = 5
adam = 6

#Print the number of apples owned seperating by comma
print(f"Apples owned = John: {john}, Mary: {mary}, Adam: {adam}")

#Create lists of owned apples for use in 
apples = [john, mary, adam]

#Assign the total amount of apples
total_apples = sum(apples)

#Print the total apples owned
print(f"Total apples = {total_apples}")

#Work out the average apples - total apples / number of owners
average_apples = ((sum(apples) / (len(apples))))
print(f"Average apples as float: {average_apples}")

#Round down to whole apples using int to drop float
average_apples = int(average_apples)

#Print the average
print(f"Average whole apples owned = {average_apples}")
