#Queston example - list in list

#EG
#Split as:
	#[3 - i for i in rane(3)]:
		#range(3) is 0, 1, 2
		#First loop:
			#3 - 0 (3)
		#Second loop:
			#3 - 1 (2)
		#Third loop:
			#3 - 2 (1)
		#List created in loop is 3, 2, 1
	#for j in range(3) - Wants to go through each list creates every time
	#range(3) is 0, 1, 2
		#First loop:
			#[3, 2, 1] index 0
		#Second loop:
			#[3, 2, 1] index 1
		#Third loop:
			#[3, 2, 1] index 2
	#Output list is [[3, 2, 1], [3, 2 ,1], [3, 2, 1]]
 	    #Index:          0          1          2
t = [[3-i for i in range(3)] for j in range (3)]
#s is initalised by assignment of 0
s = 0 
#range(3) is 0, 1, 2 
for i in range(3):
	#for each item in 0, 1, 2
	#s = t[0][0] - this means index 0 value 0, so:
	#First loop:
		#s = t[index 0][value0] - 
		#Index 0 is 3, 2, 1
		#Value 0 is 3
		#s = 3
	#Second loop
		#s = t[index 1][value 1] - 
		#Index 1 is 3, 2, 1
		#Value 1 is 2
		#from first loop:
			#s = 3 + 2
			#s = 5
	#Third loop
		#s = t[index 2][value 2] - 
		#Index 2 is 3, 2, 1
		#Value 2 is 1
		#from second loop:
			#s = 5 + 1
			#s = 6
	s += t[i][i]
#Print to confirm s = 6
print(s)
