#Import pymath module to use the addition/subtraction functions within
import pymath

#Run the main loop
while True:

	#Create empty numbers list to append inputs into
	numbers = []
	#Prompt for use with inputs
	prompt = "Enter number: "
	#Create True state for each loop within main loop - easier to see what loop is for what action
	create_list = True
	activity = True

	while create_list == True:

		#User input
		number = input(prompt)

		#Set break parameter
		if number == 'q':
			break
		else:
			#Append inputted numbers into list as float
			numbers.append(float(number))
			#Print the list to show user entered numbers
			print(numbers)

	while activity == True:

		#Choose action
		action = input("What do you want to do (add, sub, multi, div): ")

		if action == 'add':
			#Call pymath_addition function from pymath
			pymath.pymath_addition(numbers)
			break
		elif action == 'sub':
			#Call pymath_subtraction function from pymath
			pymath.pymath_subtraction(numbers)
			break
		elif action == 'multi':
			pymath.pymath_multiplication(numbers)
			break
		elif action == 'div':
			pymath.pymath_division(numbers)
			break
		else:
			#Anything other than add/sub starts activity loop again
			print("Incorrect input")

	#Option to do another round
	go_again = input("Again?: ")

	if go_again == 'y':
		continue
	else:
		break
