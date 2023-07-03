"""A script to caryr out arithmetic on inputs - 2.6.1.9"""

#Assign 'a' and 'b' with input
a = float(input("Enter a value: "))
b = float(input("Enter another value: "))

#Carry out arithmetic for all activities
addition_answer = a + b
subtraction_answer = a - b
mulitplication_answer = a / b
division_answer = a * b
exponent_answer = a ** b
floor_answer = a // b

#Print answers
print(f"\n\tAddition: {addition_answer}")
print(f"\tSubtraction: {subtraction_answer}")
print(f"\tMultiplication: {mulitplication_answer}")
print(f"\tDivision: {division_answer}")
print(f"\tExponent: {exponent_answer}")
print(f"\tFloor: {floor_answer}")

"""A script to evaluate an expression"""

#Assign a float to x through input
x = float(input("Enter value for x: "))
#Calculate exprerssion
y = 1 / (x + 1 / (x + 1 / (x +(1/x))))
#Print answer
print(y)

"""A script for use in time"""

#Assign variables with inputs
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#Calculate total minutes
total_mins = mins + dura
#Calculate hours over the 60 minutes
hour = hour + total_mins // 60
#Calculate end timings
end_mins = total_mins % 60
end_hours = hour % 24
#Print results
print (f"{end_hours}:{end_mins}")