#Casting refers to changing the type of something
#Use the following to output the type os a thing:
#print(type('thing'))

#Type, int, string, float, list, tuple
#Int
#Assign an integer (1) to x
x = 1
print("Variable 'x':")
#Print the value and type of x
print(f"Value: {x}\nType: {type(x)}")

#Assign the dstring (using '') '1'' to y 
y = '1'
print("\nVariable 'y':")
#Print the value adn type of x
print(f"Value: {y}\nType: {type(y)}")

#Assign the float '1.0' to z
z = 1.0
print("\nVariable z:")
print(f"Value: {z}\nType: {type(z)}")

#Python will automatically decide for integers and floats
#Integers are whoe numbers, floats are decimal
#Casting
#To force and integer:
x = int(1)
#To force a string
x = str(1)
#To force a float
x = float(1)
#This will force (where no errors occur) the type.
#A string 'hello' cannot be an integer or a float 

#Casting lists
#Create a tuple 'a'
a = (1,2,3,4,5)
print("\nVariable a Original:")
print(f"Variable: {a}\nType: {type(a)}")
#Cast a as a list
a = list(a)
#a is now a list not a tuple
print("\nVariable a NEW")
print(f"Value: {a}\nType: {type(a)}")

#Casting a tuple
#Create a list 'b'
b = [10, 11, 12, 13]
print("\nVariable b Original:")
print(f"Variable: {b}\nType: {type(b)}")
#Cast as tuple
b = tuple(b)
#b is now a tuple not a list
print("\nVariable b NEW")
print(f"Value: {b}\nType: {type(b)}")
