#example python assessment

#**************
#To view anything in lists, variable etc - do:
#print(variable/list)

#q1) - create a variable called numOne and assign it with a float of 2
#Cast as float using float
import numbers


numOne = float(2)

#2) Create another varaible called numTwo and assign it with a float of 5
#Cast as float using float
numTwo = float(5)

#3) create a third variable called numSum which captures the sum of numOne and numTwo
#Carry out arithmetic when assigning
numSum = (numOne + numTwo)

#4) take an input from the user called numUser
#Assuming a number to be inputted, as above examples using floats will continue with float
#Will not acceept a value that is not a number, no error handling in place.
numUser = float(input("Enter a number: "))

#5)a create a variable called highNumber with the value assigned to 10
#Integer 10 assigned to highNumber
highNumber = 10

#5b perform a decision within the code which will output "High Number" 
#if the product of numUser and numSum is greater than highNumber
#and "Low Number" if smaller than 10

#Create variable to assign product of numUser and numSum
num_product = (numUser * numSum) 
#If statement to evauate num_product against highNumber
if num_product > highNumber:
    #If num_product greater than 10 print High Number
    print("High Number")
else:
    #Any other result print Low Number
    print("Low Number")

#6) using a for loop create a list called firstList with the numbers 1-20 stored in it
#Create empty list to append into

firstList = []
#for loop with range to loop through number 1 - 20
for i in range(1,21):
    #Use append to add each value in range(1-20) to first number
    firstList.append(i)

#7) create a second list called secondList which stores the value of the corresponding 
#index in the first list multiplied by 2. e.g. [2,4,6,8....]
#Create empty list to append into
secondList = []
#Using for loop to iteratively work through values in firstList
for i in firstList:
    #For each value in firstList, multiply by 2
    i *= 2
    #Append product into secondList
    secondList.append(i)

#8) create a third list called boolList which stores whether each element in secondList
#is higher than highNumber (True) or lower (False)

#Creat empty boolList to work with
boolList =[]
#Using for loop iteratively work through values in secondList
for i in secondList:
    #Is statement to evaluate whether each value in secondList is greater than highNumber
    if i > highNumber:
        #If value is greater than 10 assign True to i
        i = True
    else:
        #Anything else assign False to i
        i = False
    #Append the value of i into boolList
    boolList.append(i)

#Question 9 will be once we have completed Mod 41 and Mod 42 review Tuesday

#9a) create a func called numPrint that outputs a list of numbers between a starting 
#number and a finish number. The function should have two parameters startNumber and endNumber

#Define function
def numPrint(startNumber, endNumber):
    #Create empty list to use in function
    number_list = []
    
    #Use for loop to create a list of values to iteratively work through using the 
    #passed argument startNumber and endNumber
    #NOTE: The endNumber will not be printed. TO print endNumber in list do something like:
    #endNumebr += 1
    #before running for loop, or in the argument istelf:
    #for i in range(startNumber, endNumber + 1)
    for i in range(startNumber, endNumber):
        #Append each value into number_list
        number_list.append(i)
    #Print the list
    print(number_list)

#Invoke the function
numPrint(1, 5)

#9b) once you have done 9a, make a change so that if the user doesnt input an end number 
#it automatically uses 10

#Define function with new parameter
#Using endNumber = 10 when defining the funciton sets a 'default argument' of that value assigned
def numPrint(startNumber, endNumber = 10):
    #Create empty list to use in function
    number_list = []
        #Use for loop to create a list of values to iteratively work through using the 
    #passed argument startNumber and endNumber
    #NOTE: endNumber will be 10 unless a new argument is passed to explicitly change it
    #NOTE: 10 will not be printed unless you change default argument to 11 or
    #do something like:
    #endNumebr += 1
    #before running for loop, or in the argument istelf:
    #for i in range(startNumber, endNumber + 1)
    for i in range(startNumber, endNumber):
        #Append each value into number_list
        number_list.append(i)
    #Print the list
    print(number_list)

#Invoke function
numPrint(1)

#10)create a function which takes in a list of numbers as an argument. It then returns the number
#of odd numbers within the list. For example [3,4,5] should return 2

#Define function with number as argument
def is_it_odd(numbers):
    #Create a counter for number of odd numbers
    number_odd = 0
    #Using for loop to iteratively work through values in passed list
    for i in numbers:
        #If modulo 2 of value is not 0, it is odd
        if i % 2 != 0:
            #Increment the value of counter to show an odd number is present in list
            number_odd += 1
        #No else required as nothing else needs to happen
    #Print the number odd numbers in list
    print(number_odd)
    
#Create test list
number_list = [3,4,5]
#Invoke function with test list
#This function expects a list to be passed as an argument fue to the for loop wihin it
#Passing invdivdual values will not work as you cannot iteratviely work through a single value
is_it_odd(number_list)

#11) create a tuple which stores the following values 3,4,6,5,3,5,7,8,5
numbers_tuple = ('3','4','6','5','3','5','7','8','5')

#12) The values shown in question 11 refer to the number of goals scored by the following players 
#Rooney, Vardy, Heskey, Owen, Grielish, Sterling, Pele, Maradona, Walker
#Create a second tuple which stores these players
players_tuple = ('Rooney', 'Vardy', 'Heskey', 'Owen', 'Grielish', 'Sterling', 'Pele', 'Maradona', 'Walker')

#13)) using the above tuples, link them via a dictionary.
#for example, Rooney:3, Vardy:4 etc. You should use your two tuples to construct the 
#dictionary

#Use built in functionality to invoke 2 tuples and compund into dictionary
#Dictionary called goals_scored assigned indexes and values as required
goals_scored = dict(zip(players_tuple, numbers_tuple))
print(goals_scored)    
