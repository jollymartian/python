"""Snippet to create dictionary and pull certain info from it"""

#Create dictionary called people
people = {
	#Add attributes of people. first name, last name, age, location, grades
	'jack': {
		'first': 'jack',
		'last': 'lamb',
		'age': 2,
		'location': 'okeford',
		'grade': ['a', 'b', 'e'],
	},

	'jules': {
		'first': 'jules',
		'last': 'hunter',
		'age': 39,
		'location': 'blandford',
		'grade': ['f'],
	},

	'kyle': {
		'first': 'kyle',
		'last': 'lamb',
		'age': 32,
		'location': 'okehampton',
		'grade': ['a', 'c'],	
	},
	
}

#Loop through dictionary to pull out keys and values
for person, person_info in people.items():
	#Assign variables based on key values
	full_name = f"{person_info['first']} {person_info['last']}"
	age = f"{person_info['age']}"
	location = f"{person_info['location']}"
	grade = f"{person_info['grade']}"
	#Print values using variables
	print(f"Name: {full_name.title()}")
	print(f"\n\tAge: {age}")
	print(f"\tLocation: {location.title()}")
	#Loop through individual key list - grade and print
	#****Needs refining to print all under grades****
	for grade in person_info['grade']:
		if len(person_info['grade']) == 1:
			print(f"\tGrade: {grade.upper()}")
		else:
			print(f"\tGrades: {grade.upper()}")
