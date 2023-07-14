#If statements evaulate something against something else

#When evaluating use == to evaluate if something equilavent
#!= for not equivalent
# >= for greater or equal 
# <= for less than or equal

#Indentation is important to determine what belongs to each statement
#if:
#	'action_1'
#else:
#	'action_2'

#action_1 belongs to if
#ection_2 belongs to else

#Example 1
print("Example 1")
#If 1 is equivalent to 1 then do the next thing, otherwise continue with the code
#1 is equivalent, so do the print
#If it wasn't it would not print and continue to the next bit of code
if 1 == 1:
	print("Yes")

#Example 2
print("\nExample 2:")
#if 1 is equivalent to 0 then do the next thing, else do the other
#1 is not equivalent to 0, so else
if 1 == 0:
	print("Yes")
else:
	print("No")

#Example 3
print("\nExample 3:")

#use variable in if statement
x = 5

#if x is equivalent to 10 print yes, else no
if x == 10:
	print("Yes")
else:
	#x (5) not equivalent so print no
	print("No")

#Example 4
print("\nExample 4:")
#else-if blocks.
#elif means else if to create multiple statements
#if block will run until it hits its true statement, runs through all with none true,
#or hits and else and does that
if 1 == 0:
	print("No")
elif 1 != 1:
	print("Yes")
elif 5 == 5:
	#Will print CORRECT as it is the true statement.
	print("CORRECT!")
else:
	print("NOT THIS")

#Example 5
print("\nExample 5:")
#else-if blocks.
#elif means else if to create multiple statements
#if block will run until it hits its true statement, runs through all with none true,
#or hits and else and does that
if 1 == 0:
	print("No")
elif 1 != 1:
	print("Yes")
elif 5 > 9:
	print("CORRECT!")
else:
	#Will print NOT THIS as no statements were true so else is invoked
	print("NOT THIS")

#Example 6
print("\nExample 6:")
#else-if blocks.
#elif means else if to create multiple statements
#if block will run until it hits its true statement, runs through all with none true,
#or hits and else and does that
x = 'strings work too'

#Strings can be evaluated also
if x == 'strings work too':
	print("Yes")
elif 1 != 1:
	print("No")
#5 is also greater than 9 however, a statement above has already been found true so ends the block,
#before it reaches here
elif 5 < 9:
	print("CORRECT!")
else:
	#Will print NOT THIS as no statements were true so else is invoked
	print("NOT THIS")

#Nested if blocks
#Example 7
print("\nExample 7:")
x = 5
y = 99

if x == 5:
	#The below come into play as x is equivalent to 5
	if y != 0:
		#Prints No as y (99) is not 0 and therefore true
		print("No")
	else:
		print("Yes")
	#The next if block is reference once previous finished
	if y == 99:
		#Prints Yes as y (99) is equivalent to 99 and true
		print("Yes")
	else:
		print("No")