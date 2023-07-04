#Main diff between arrays and lists is arrays can be used as below
import numpy as np

array = np.array([3, 6, 9, 12])
division = array / 3
print(division)

#Will error
list = [3, 6, 9, 12]
division = list / 3
print(division)

#Would have to do something like this this:
division = []
for i in list:
	i = int(i / 3)
	division.append(i)
print(division)