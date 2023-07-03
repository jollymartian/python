def low_tax(income, jury):

    #Variables for maths
    #18% off
    low_tax_rate = 0.18
    #Set relief
    tax_relief = 556.2

    #Do the maths
    tax = income * low_tax_rate
    tax = tax - tax_relief
    
    #Jury concessions
    if jury == 'y':
        tax = tax / 2
    
    #Return value
    return round(tax, 0)

def high_tax(income, jury):

    #Set variable for rates
    high_tax_rate = 0.32
    tax_set = 14_839.2
    tax_threshold = 85_528

    #Do maths
    tax = income - tax_threshold
    tax = tax * high_tax_rate
    tax = tax + tax_set
    #Jury Concessions
    if jury == 'y':
        tax = tax / 2
    #Return value
    return round(tax, 0)

