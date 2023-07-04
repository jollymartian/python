#Script to return height of pyramid against full layers of blocks

blocks = int(input("Enter the number of blocks: "))

#Set top layer to one block
height = 0
number_in_layer = 0
#blocks -= 0

#Loop using blocks variable
while blocks > 0:
    
    if blocks - number_in_layer < 0:
        break
    else:
        number_in_layer += 1
        height += 1
        blocks -= number_in_layer
    
print(f"The height of the pyramid: {height}")
