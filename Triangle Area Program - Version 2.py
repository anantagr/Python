#Ask the user for base and height of the triangle

import sys

base_length = float (input ("Enter length of the base of the Triangle in cm: "))
if (base_length <= 0) :
    print ("**Error - the base length must be a positive number. You entered", base_length)
    sys.exit() #this command will make the system leave the program if base is zero or negative.

height = float (input ("Enter height of the Triangle in cm: "))
if (height <= 0) :
    print ("**Error - the height must be a positive number. You entered", height)
    sys.exit() #this command will make the system leave the program if height is zero or negative.


#calculate the area

area_cm = (base_length * height)/2
area_m = area_cm/10000



#Print the result
print("The Area of the triangle is ", area_m, " mtr sqr", sep="")


