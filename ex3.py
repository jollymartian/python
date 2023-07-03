### 1 ###

#set variable
x = int(input("Enter number: "))
#evaluate if over 100 (True/False)
print(x >= 100)

### 2 ###

while True:

	var = input("Enter: ")

	if var == "Spathiphyllum":
		print("Spathipyllum is the best plant ever!")
	elif var == "spathiphyllum":
		print("No, I want a big Spathiphyllum!")
	elif var == 'q':
		break
	else:
		print(f"Spathiphyllum! Not {var}!")
