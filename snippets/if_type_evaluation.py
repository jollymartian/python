"""Snippet testing the use of type and isinstance to determine actions based on
the type of value, such as integer or string."""

#Set variables for loops to True for use in nested while loops
type_loop = True
isinstance_loop = True

#Set main loop to run program in
while True:

	#Set while loop for using type
	while type_loop == True:
		#User input variable
		x = input("Enter (type): ")
		#Evaluate if statement against x to match 'q' to quit by changing type_loop to False
		if x == 'q':
			type_loop = False
		#Use try to manage ValueErrors when trying to convert string/float to integer
		try:
			#Successful inputs converted to integer
			x = int(x)
		except ValueError:
			#Pass skips over any ValueErrors and continues the code, leaving the type as string
			pass
		#If statement evaluates the type of x
		if type(x) != int:
			#If x is NOT an integer prints the below
			print(f"Not integer: {type(x)}")
		else:
			#If x IS an integer prints the below
			print(f"Integer: {type(x)}")

	#Set while loop for using isinstance
	while isinstance_loop == True:
		#User input variable
		x = input("Enter (isinstance): ")
		#Evaluate if statement against x to match 'q' to quit by changing isinstance_loop to False
		if x == 'q':
			isinstance_loop = False
		#Use try to manage ValueErrors when trying to convert string/float to integer
		try:
			#Successful inputs converted to integer
			x = int(x)
		except ValueError:
			#Pass skips over any ValueErrors and continues the code, leaving the type as string
			pass
		#isinstance evaluates whether x is an integer. If so it prints 'Integer', else it prints 'Not integer'.
		#isinstance returns True or False on outcome
		if isinstance(x, int):
			print("Integer!")
		else:
			print("Not integer")
	break

