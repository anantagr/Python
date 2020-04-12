#Ask the customer for intiall investment
#Ask the customer for interest rate
#Ask the customer for number of years


#Getting customer input
principal_amount = float (input ("What is your principal amount invested?: "))
while (principal_amount <= 0) :
    print ("**Error - the Principal amount must be a positive number. You entered", principal_amount, " Please re-enter")
    principal_amount = float (input ("What is your principal amount invested?: ")) #Checking for negative values and zero

interest_rate = float (input ("What is the annual interest rate (in percet)?: "))
while (interest_rate <= 0) :
    print ("**Error - the interest rate must be a positive number. You entered", interest_rate, " Please re-enter")
    interest_rate = float (input ("What is the annual interest rate (in percet)?: ")) #Checking for negative values and zero

years = int (input ("How many years will this be invested for?: "))
while (years <= 0) :
    print ("**Error - the time period must be a positive number. You entered", years, " Please re-enter")
    years = int (input ("How many years will this be invested for?: ")) #Checking for negative values and zero


print ("Year    Balance")

#Starting loop
for time in range(0, years) :
    principal_amount = principal_amount * (1+(interest_rate/100))
    print (time+1,"     ", "${:.2f}".format(principal_amount))

    
    
