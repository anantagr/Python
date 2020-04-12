
base_length = float (input ("Enter length of the base of the Triangle in cm: "))
height = float (input ("Enter height of the Triangle in cm: "))

#calculate the area

area_cm = (base_length * height)/2
area_m = area_cm/10000




print("A Triangle with Base ", base_length, "cm and Height ", height, "cm has an area of: " ,area_m, "m", sep="")



