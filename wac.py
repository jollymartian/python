# Simple program to work out WAC details

import math

bc_long_hours = 0
bc_long_minutes = 50

bc_short_hours = 0
bc_short_minutes = 30

# Set AC hours
ac_long_hours = 2
ac_long_minutes = 30

ac_short_hours = 1
ac_short_minutes = 15

# AC prices
ac_long_price = 14.30
ac_short_price = 7.15

# BC prices
bc_long_price = 5.50
bc_short_price = 4.40

# Create BC full/short variables
bc_full = f"{bc_long_hours}:{bc_long_minutes}"
bc_short = f"{bc_short_hours}:{bc_short_minutes}"

# Full/Brief output

full_brief = input("Do you want full output (y/n): ")

# AC

number_long = input("\nEnter full Afterschool days: ")
number_short = input("Enter short Afterschool days: ")
number_long = int(number_long)
number_short = int(number_short)

# Create AC full/short variables
ac_long_total_hours = number_long * ac_long_hours
ac_long_total_minutes = number_long * ac_long_minutes

ac_short_total_hours = number_short * ac_short_hours
ac_short_total_minutes = number_short * ac_short_minutes 

# Deal with over 60 minutes - long
if ac_long_total_minutes >= 60:
	# Convert over hour mins to hours.mins
	ac_long_total_minutes = ac_long_total_minutes / 60
	# Use math to seperate integer/decimal values into list
	ac_long_math = math.modf(ac_long_total_minutes)
	# Set additional hours variable
	ac_long_total_additional = ac_long_math[1]
	ac_long_total_hours = ac_long_total_additional + ac_long_total_hours
	# Set remaining minutes as total minutes
	ac_long_total_conversion = ac_long_math[0] * 60
	ac_long_total_minutes = ac_long_total_conversion

ac_long_total_hours = int(ac_long_total_hours)
ac_long_total_minutes = int(ac_long_total_minutes)

# Deal with over 60 minutes - short
if ac_short_total_minutes >= 60:
	# Convert over hour mins to hours.mins
	ac_short_total_minutes = ac_short_total_minutes / 60
	# Use math to seperate integer/decimal values into list
	ac_short_math = math.modf(ac_short_total_minutes)
	# Set additional hours variable
	ac_short_total_additional = ac_short_math[1]
	ac_short_total_hours = ac_short_total_additional + ac_short_total_hours
	# Set remaining minutes as total minutes
	ac_short_total_conversion = ac_short_math[0] * 60
	ac_short_total_minutes = ac_short_total_conversion
	
ac_short_total_hours = int(ac_short_total_hours)
ac_short_total_minutes = int(ac_short_total_minutes)

# Total AC time
total_ac_minutes = ac_short_total_minutes + ac_long_total_minutes
total_ac_hours = ac_short_total_hours + ac_long_total_hours

if total_ac_minutes >= 60:
	# Convert over hour mins to hours.mins
	total_ac_minutes = total_ac_minutes / 60
	# Use math to seperate integer/decimal values into list
	ac_total_math = math.modf(total_ac_minutes)
	# Set additional hours variable
	ac_total_additional = ac_total_math[1]
	total_ac_hours = ac_total_additional + total_ac_hours
	# Set remaining minutes as total minutes
	ac_total_conversion = ac_total_math[0] * 60
	total_ac_minutes = ac_total_conversion

total_ac_hours = int(total_ac_hours)
total_ac_minutes = int(total_ac_minutes)

# AC cost
ac_long_cost = number_long * ac_long_price
ac_short_cost = number_short * ac_short_price
ac_total_cost = ac_short_cost + ac_long_cost 

# BC

number_long = input("Enter long Breakfast days: ")
number_short = input("Enter short Breakfast days: ")
number_long = int(number_long)
number_short = int(number_short)

# Create BC full/short variables
bc_long_total_hours = number_long * bc_long_hours
bc_long_total_minutes = number_long * bc_long_minutes

bc_short_total_hours = number_short * bc_short_hours
bc_short_total_minutes = number_short * bc_short_minutes 

# Deal with over 60 minutes - long
if bc_long_total_minutes >= 60:
	# Convert over hour mins to hours.mins
	bc_long_total_minutes = bc_long_total_minutes / 60
	# Use math to seperate integer/decimal values into list
	bc_long_math = math.modf(bc_long_total_minutes)
	# Set additional hours variable
	bc_long_total_additional = bc_long_math[1]
	bc_long_total_hours = bc_long_total_additional + bc_long_total_hours
	# Set remaining minutes as total minutes
	bc_long_total_conversion = bc_long_math[0] * 60
	bc_long_total_minutes = bc_long_total_conversion

bc_long_total_hours = int(bc_long_total_hours)
bc_long_total_minutes = int(bc_long_total_minutes)

# Deal with over 60 minutes - short
if bc_short_total_minutes >= 60:
	# Convert over hour mins to hours.mins
	bc_short_total_minutes = bc_short_total_minutes / 60
	# Use math to seperate integer/decimal values into list
	bc_short_math = math.modf(bc_short_total_minutes)
	# Set additional hours variable
	bc_short_total_additional = bc_short_math[1]
	bc_short_total_hours = bc_short_total_additional + bc_short_total_hours
	# Set remaining minutes as total minutes
	bc_short_total_conversion = bc_short_math[0] * 60
	bc_short_total_minutes = bc_short_total_conversion
	
bc_short_total_hours = int(bc_short_total_hours)
bc_short_total_minutes = int(bc_short_total_minutes)

# Total BC time
total_bc_minutes = bc_short_total_minutes + bc_long_total_minutes
total_bc_hours = bc_short_total_hours + bc_long_total_hours

if total_bc_minutes >= 60:
	# Convert over hour mins to hours.mins
	total_bc_minutes = total_bc_minutes / 60
	# Use math to seperate integer/decimal values into list
	bc_total_math = math.modf(total_bc_minutes)
	# Set additional hours variable
	bc_total_additional = bc_total_math[1]
	total_bc_hours = bc_total_additional + total_bc_hours
	# Set remaining minutes as total minutes
	bc_total_conversion = bc_total_math[0] * 60
	total_bc_minutes = bc_total_conversion

total_bc_hours = int(total_bc_hours)
total_bc_minutes = int(total_bc_minutes)

# BC cost
bc_long_cost = number_long * bc_long_price
bc_short_cost = number_short * bc_short_price
bc_total_cost = bc_short_cost + bc_long_cost

# Total time
total_minutes = total_bc_minutes + total_ac_minutes
total_hours = total_bc_hours + total_ac_hours

if total_minutes >= 60:
	# Convert over hour mins to hours.mins
	total_minutes = total_minutes / 60
	# Use math to seperate integer/decimal values into list
	total_math = math.modf(total_minutes)
	# Set additional hours variable
	total_additional = total_math[1]
	total_hours = total_additional + total_hours
	# Set remaining minutes as total minutes
	total_conversion = total_math[0] * 60
	total_minutes = total_conversion


# Prints
# AC data
if full_brief == 'y':
	print(f"\nFull Afterschool Club days: {number_long}")
	print(f"\n\t{ac_long_total_hours}hrs {ac_long_total_minutes}mins.\n")
	print(f"Short Afterschool Club days: {number_short}")
	print(f"\n\t{ac_short_total_hours}hrs {ac_short_total_minutes}mins.\n")
	print(f"\n***Total AC hours: {total_ac_hours}hrs {total_ac_minutes}mins.***\n")
	print(f"\n***Total AC cost: {ac_total_cost}") 

# BC data

	print(f"\nFull Breakfast Club days: {number_long}")
	print(f"\n\t{bc_long_total_hours}hrs {bc_long_total_minutes}mins.\n")
	print(f"Short Breakfast Club days: {number_short}")
	print(f"\n\t{bc_short_total_hours}hrs {bc_short_total_minutes}mins.\n")
	print(f"\n***Total BC hours: {total_bc_hours}hrs {total_bc_minutes}mins.***\n")
	print(f"\n***Total BC cost: {bc_total_cost}")

# Total data
	print(f"\n\t!!!TOTAL TIME: {total_hours}hrs {total_minutes}mins.!!!\n")
	total_cost = ac_total_cost + bc_total_cost
	print(f"\n***Total cost: {total_cost}")

else:
# Totals data
	print(f"\n\t!!!TOTAL TIME: {total_hours}hrs {total_minutes}mins.!!!\n")
	total_cost = ac_total_cost + bc_total_cost
	print(f"\n***Total cost: {total_cost}")

# *** WHILE LOOP NEEDS MAKING - use input to pause for now
close = input("Enter: ")

# Use math module to get decimal/integer
#x = ac_long_total_minutes
#x = math.modf(x)
#print(x)

#Formula
#190 min * [1 hr / 60 min] = 190/60 hr = 3.16667 hr

#3 is the hours part.

#The minutes part is calculated as 0.16667 * 60 = 10

#So, 190 minutes = 3 hours and 10 minutes.