x = int(input("Enter number: "))
print(x >= 100)
input()

#######

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
