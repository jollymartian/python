#Iterate through strings
#Integers and floats are not iteratable

#Assign x with a string
x = "hello"

#Iterate through sting(x)
for i in x:
	#Print each letter in sting(x) on same line using end="" to overwrite \n default
	print(i, end = "")

#The same can be achieved as follows:
#Create for loop to pull index into the print
#EG: range(len(x)) - len(x) = 5, range(5) create a list =[0,1,2,3,4]
for i in range(len(x)):
	#print(x[i]) on first loop prints the value of the created list at index 0 - 'h', and so on
	print(x[i], end = '')

#Seperate examples with newline
print("\n")

#Iterate through string(x)
for i in x:
	#print each letter in string(x) on newline
	print(i)

#Seperate examples with newline
print("\n")

#Assign long string to x
x = "Hello, World! Do you like Python?"
#Iterate through string(x)
for i in x:
	#Print each letter on same line as above example
	print(i, end = "")

#Seperate examples with newline
print("\n")

#Iterate through string(x)
for i in x:
	#Print each letter on newline
	print(i)


