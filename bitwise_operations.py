#create a flag with a set flag
                                            #0000 0000 0000 x000
flag_registerA = 0x1234 #flag reset/cleared  0001 0010 0011 0100
flag_registerB = 0x1248 #flag set            0001 0010 0100 1000

#create an appropriate mask
the_mask = 8

#1 use & to check if flag set/reset
if flag_registerB & the_mask:
    print("My bit is set")
else:
    print("My bit is reset")

#2 reset(assign zero) to bit
flag_registerB &= ~the_mask

#check 2
if flag_registerB & the_mask:
    print("My bit is set")
else:
    print("My bit is reset")

#3 use | to assign bit to 1
flag_registerB |= the_mask
 
#check 3
if flag_registerB & the_mask:
    print("My bit is set")
else:
    print("My bit is reset")
 

#4 use ^ to make it the opposite/negate your bit
flag_registerB ^= the_mask 

#check 4
if flag_registerB & the_mask:
    print("My bit is set")
else:
    print("My bit is reset")
 

#5 use ^ to make it the opposite/negate your bit
flag_registerB ^= the_mask 
 

#check 5
if flag_registerB & the_mask:
    print("My bit is set")
else:
    print("My bit is reset")
 

#The above should output (ingoring the # of course)
#bit is set
#bit is reset
#bit is set
#bit is reset
#bit is set
#Press any key to continue . .
