
#Ask the customer for number of eggs bought 

import sys

num_eggs = float (input ("Please enter the number of Eggs: "))

#Checking if number entered is valid and non-negative
if (num_eggs < 0) :
    print ("Value entered is not valid. It should be a positive number. You enetered", num_eggs)
    print ("Thank you, have a good day")
    sys.exit()

#If zero eggs were bought then exiting the program
if (num_eggs == 0) :
    print ("Value entered is not valid. It should be a positive number. You enetered", num_eggs)
    print ("You have bought", num_eggs, "eggs, thank you and have a good day")
    sys.exit()
    
#Calculating the dozen of eggs bought
dozen_eggs = num_eggs/12

#Finding the right price for a dozen of eggs
if dozen_eggs < 4 :
    cost_per_dozen = 0.50
elif dozen_eggs < 6 :
    cost_per_dozen = 0.45
elif dozen_eggs < 11 :
    cost_per_dozen = 0.40
else :
    cost_per_dozen = 0.35

#Calculating the total bill
total_bill = num_eggs * (cost_per_dozen/12)

#Printing the result out
print ("You cost is $", cost_per_dozen, " per dozen or $", (cost_per_dozen/12), " per egg.", sep="")
print ("Your bill comes to $", total_bill, sep="")
