#List relationships

#When deleting values to create empty list [:] 
nums = [1, 2, 3]
vals = nums 
#Deleting the values affects the original nums list
del vals[:]

print(nums)
print(vals)
print(len(nums))
print(len(vals))

#When deleting the list entirely it doesn't affect the orignal nums list
nums = [1, 2, 3]
vals = nums 
del vals

#Anything vals related no longer exists
print(nums)
print(vals)
print(len(nums))
print(len(vals))
