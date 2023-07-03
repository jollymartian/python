#Function for calculationg leap year

def leap_year(year):
    """Script to calculate a leap year."""
    #Return true if it's a leap year
    #Set variables for calculations
    divisible_by_four = year % 4
    divisible_by_onehundred = year % 100
    divisible_by_fourhundred = year % 400
    if divisible_by_four != 0:
        #Common year
        return False
    elif divisible_by_onehundred != 0:
        #Leap year
        return True
    elif divisible_by_fourhundred != 0:
        #Common year
        return False
    else:
        #Leap year
        return True
    
