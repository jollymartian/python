"""Snippet for creating and editing a block of items in a list,
using aliens as an example"""

#Make empty list for storing aliens

aliens = []

#Make 30 green aliens with same attributes

for alien_number in range(30):
	new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

#For the first 3 aliens evaluate the following
for alien in aliens[0:3]:
	if alien['colour'] == 'green':
		alien['colour'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['colour'] == 'yellow':
		alien['colour'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

#For the first 7 aliens evaluate the following
for alien in aliens[0:7]:
	if alien['colour'] == 'green':
		alien['colour'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['colour'] == 'yellow':
		alien['colour'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

#show first 10 aliens
#Because the first 3 had already been changed to yellow in the,
#first for loop they will become red. The next 4 become yellow
#and the rest stay green
for alien in aliens[:10]:
	print(alien)
print("...")

#Show many have been created using len to display total items in list

print(f"Total aliens: {len(aliens)}")