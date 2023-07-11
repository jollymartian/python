#Slicing lists

#Create list for examples
#Descending    -9 -8 -7 -6 -5 -4 -3 -2 -1	   
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Ascending      0  1  2  3  4  5  6  7  8

#Print range of items in list (item 2 - item 4, last item is not printed - see example ends at item 5 (value = 6)
#however, only up to item 4 is printed (vlaue = 5)). This is due to first item index being 0.
print(example_list[2:5])

#Print first 5 items - starts at item 0 and ends at item 5
print(example_list[:5])

#Print last 5 items - negative numbers descend, starts from last item in list an back to item -5
print(example_list[-5:])

#Print last 5 items - if list length known can choose to start 5 items from end
print(example_list[4:]) 

#Print from item 0 an move 2 items each time
print(example_list[0::2])

#Print from item 0 and move 4 items each time
print(example_list[0::4])

#Print in reverse order using reverse slice operator :: - does not edit orignal list
print(example_list[::-1])

#Print values from 7 in reverse
print(example_list[-3::-1])

#Print 7, 8 in ascending order using negative numbers
print(example_list[-3:-1])