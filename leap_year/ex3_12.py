#Input a year and determine if it is a leap year.
import ex3_12_mod

#Create running loop.
while True:
    #Input year to test.
    year = input("Enter a year: ")
    #Break while loop on 'q'.
    if year == 'q':
        break
    #issue warning and break if year < 1582.
    if year < '1582':
        print("Not within the Gregorian calendar period.")
        continue
    #call leap_year function to evaluate years.
    is_leap_year = ex3_12_mod.leap_year(int(year))
    #Print relevant output depending on return from leap_year function.
    if is_leap_year == True:
        print("Leap year")
    else:
        print("Common year")


