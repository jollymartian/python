hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
#Using len for flexibility if list length changes
mid = len(hat_list) // 2
hat_list[mid] = int(input("Enter a number: "))

# Step 2: write a line of code that removes the last element from the list.
hat_list.pop()

# Step 3: write a line of code that prints the length of the existing list.
length = len(hat_list)
print(f"Length of list: {length}")

print(hat_list)
