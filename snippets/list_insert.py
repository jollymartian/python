#Inserting into lists

#example list
example_list = [1,2,3]

#Use range to create numbers to add
for i in range(2):
    #Insert at -1 position (end) in example_list - inserts at beginning shifting
    #rest to the right
    example_list.insert(-1, example_list[i])

print(example_list)

#example list
example_list = [1,2,3]

#Use range to create numbers to add
for i in range(2):
    #Insert at 1 position (middle) in example_list
    #rest to the right
    example_list.insert(1, example_list[i])

print(example_list)

