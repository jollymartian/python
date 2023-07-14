#For loops iteratively work through values using an index

#Example lists
list_1 = [1, 2, 3, 4, 5]

list_2 = [0, 2, 4, 8, 16]

#Example 1
print("Example 1:")
#The for loop itertively works through each item in the list (list_1)
#This means for each item starting at the first it will carry out the action next in line
#For this example it will print 1, then once all conditions are met (only one here - print()) it will move onto,
#the next item and print 2 until there are no items left to work through
#i in this example is the variable to assign each item into to carry out the action against, it
#doesn't have to be i, it can be any valid name
for i in list_1:
	print(i)

#Example 2
print("Example 2:")
#To confirm print the secon list looping through each item
for i in list_2:
	print(i)

#Example 3
print("Example 3:")
#Other actions can occur on each loop
for i in list_1:
	#Here i = i + 1
	#EG. i = 1 + 1
	#	 i = 2
	#i is incremented by 1 on each loop as above, this will take the values from
	#list_1 and add 1 to them, so, [1 ,2, 3, 4, 5] becomes
	#[2, 3, 4, 5, 6]
	i += 1
	#On each loop the value i is printed
	print(i)

#Example 4
print("Example 4:")
#if statements can be used in for loops
#Using number as variable name in this example
for number in list_1:
	#if ststement to evaluate whether number is equivalent to 1
	#If it is then "One" will be printed
	#Else is needed to determine what happens if any other outcome other than
	#is equivalent to 1 occurs
	#Else prints the number
	if number == 1:
		#Will print "One"
		print("One")
	else:
		#Will print the number
		print(number) 

#Example 5
print("Example 5:")
#for loops can use range() to generate an index to work through
#Indexes in lists:
#Example list
list_3 = [10, 15, 20, 25, 30]

#Index:  -5  -4  -3  -2  -1
#Values [10, 15, 20, 25, 30]
#Index    0   1   2   3   4

#For loop to loop through items in list using index values
#range(2) is 0, 1
#So it will use the value at indexes 0 and 1
#It will loop through value 10, 15
for i in range(2):
	#Assign the value at each index to 'value'
	#list[i] here means list_3[index] so gets the values stored at that index
	#The first loop is 0
	#list[0] is list_3 [index 0] which returns the value 10
	value = list_3[i]
	print(value)

#Example 6
print("Example 6:")
#Multiple lists can be invoked to create new lists
list_4 = ['a', 'b', 'c']
list_5 = [1, 2, 3]
#Create an empty list to ad new values into, this intialises the list just like with variables,
#until a 'thing' exists it can;t be referenced in the for loop
list_6 = []

#For each item (x) in list_6:
for x in list_4:
	#Using append add x to list_6 from list_4
	list_6.append(x)
	#Using append add the value stored at index 0 in list_5, in this case
	list_6.append(list_5[0])

#This create a new list, list_6, with the values,
#['a', 1, 'b', 1, 'c', 1]
#Because it loops through x and each time reassigns x to the next value a, b or c and appends to list_6
#But only ever references the value at list_5[0] which is 1.
#So on each loop it appends the value at x and then the value at list_6[0]
#Eg.
#First loop is x = 'a' and list_5[0] = 1
#Second loop is x = 'b' and list_5[0] = 1.....
print(list_6)

#Example 7
print("Example 7:")
#Create an new empty list:
list_7 = []
#To append each value from seperate lists relative to each other you can use range and loop through the index
#To create the correct amount of the index values use len() to get the number of items in a list
#len(list_4) will return 3, as there are 3 itmes in it - a,b,c
#range will then be range(3) which is 0, 1, 2
#The for loop will then iteratively work through the values 0, 1, 2
for x in range(len(list_4)):
	#Using append we add list_4[x] to list_7
	list_7.append(list_4[x])
	#Using append we add list_5[x] to list_7
	list_7.append(list_5[x])

#On the first loop x is 0
#list_7.append(list_4[0]) will add the value list_4[0] to list_7.
#The value is 'a'
#list_7.append(list_5[0]) will add the value list_5[0] to list_7.
#The value is 1.....
print(list_7)

	
