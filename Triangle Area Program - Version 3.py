#Ask the user for base and height of the triangle
#Check for negative entriens and ask again

import sys

base_length = float (input ("Enter length of the base of the Triangle in cm: "))

while (base_length <= 0) :
    print ("**Error - the base length must be a positive number. You entered", base_length, " Please re-enter")
    base_length = float (input ("Enter length of the base of the Triangle in cm: "))


height = float (input ("Enter height of the Triangle in cm: "))

while (height <= 0) :
    print ("**Error - the height must be a positive number. You entered", height, " Please re-enter")
    height = float (input ("Enter height of the Triangle in cm: "))

#calculate the area

area_cm = (base_length * height)/2
area_m = area_cm/10000



#Print the result
print("The Area of the triangle is ", area_m, " mtr sqr", sep="")


