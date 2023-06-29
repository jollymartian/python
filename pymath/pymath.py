def pymath_addition(numbers):
	"""addition with inputs"""

	#Set x to 0 to begin addition from 0
	x = 0

	#Loop through all numbers adding them to the previous
	for number in numbers:
		x = x + number

	#Print the answer
	print(x)

	#Return the value - need a variable on returned end to take value
	#return x

def pymath_subtraction(numbers):
	"""subtraction with inputs"""

	#Set x to first number in list
	x = numbers[0]
	#Change the value to 0 to avoid numbers[0] - numbers[0] when subtracting
	numbers[0] = 0

	#Loop through all numbers subtracting them from the previous
	for number in numbers:
		x = x - number

	#Print the answer
	print(x)

def pymath_multiplication(numbers):
	"""mulitply with inputs"""

	#Set x to first numner in list
	x = numbers[0]
	#Change the value to 1 to avoid numbers[0] * numbers[0]
	numbers[0] = 1

	#Loop through all numbers mulitplying them to the previous
	for number in numbers:
		x = x * number

	#Print the answer
	print(x)

def pymath_division(numbers):
	"""divide with inputs"""

	#Set x to first number in list
	x = numbers[0]
	#Change to 1 to avoid numbers[0] / numbers[0]
	numbers[0] = 1

	#Loop through all numbers dividing from previous
	for number in numbers:
		x = x / number

	#Print the answer
	print(x)

