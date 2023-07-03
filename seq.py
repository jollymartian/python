#Script to read a sequence of numbers and evaluate.

#Set counter to zero.
odd_numbers = 0
even_numbers = 0
div_three = 0

#Set number with input
number = int(input("Enter a number or type 0 to stop: "))

#Create a loop to run program in.
while number != 0:
    
    #Evaluate number against arguments.
    if number % 2 == 1:
        #Increase odd counter by 1.
        odd_numbers += 1
    else:
        #Increase even counter by 1.
        even_numbers += 1
    if number % 3 == 0:
        #Increase div_three counter by 1.
        div_three += 1
    #Read next number and loop.
    number = int(input("Enter a number or type 0 to stop: "))

#Print output of counters on break
print(f"Odd: {odd_numbers} \nEven: {even_numbers} \nDiv_3: {div_three}")




