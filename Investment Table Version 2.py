#Ask the customer for intiall investment
#Ask the customer for interest rate
#Ask the customer for number of years

SENTINAL = 0
year = 0

#Getting customer input
principal_amount = float (input ("What is your principal amount invested?: "))#Asking for principal amount
while (principal_amount <= 0) :
    print ("**Error - the Principal amount must be a positive number. You entered", principal_amount, " Please re-enter")
    principal_amount = float (input ("What is your principal amount invested?: "))#Checking for negative or zero values


initial_investment = principal_amount #Saving a second copy of Principal amount


interest_rate = float (input ("What is the interest rate for year {:.0f} (in percent)?: ".format(year+1))) #Asking for interest rate
while (interest_rate < 0) :
    print ("**Error - the interest rate must be a positive number. You entered", interest_rate, " Please re-enter")
    interest_rate = float (input ("What is the interest rate for year {:.0f} (in percent)?: ".format(year+1)))#Checking for negative or zero values

#Starting loop
while (interest_rate != SENTINAL) :
    principal_amount = principal_amount * (1+(interest_rate/100))
    year += 1
    interest_rate = float (input ("What is the interest rate for year {:.0f} (in percent)?: ".format(year+1))) #Asking for interest rate
    while (interest_rate < 0) :
        print ("**Error - the interest rate must be a positive number. You entered", interest_rate, " Please re-enter")
        interest_rate = float (input ("What is the interest rate for year {:.0f} (in percent)?: ".format(year+1)))#Checking for negative or zero values
    


print ("At the end of {:d} years, your investment will be worth ${:.2f}".format(year, principal_amount))
print ("Your average yearly income is ${:.2f}.".format((principal_amount - initial_investment)/year))



    
