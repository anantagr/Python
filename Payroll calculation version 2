#Calculation of Employee's net pay and print its pay slip


#Defining function to ensure non-negative, numeric and maximum 168 hours value is entered by the employee
def get_hours(prompt,minimum,maximum) :

    need_value = True
    while (need_value) :
        try :
            value = float(input(prompt))
            if (value < minimum) :
                print("Number of hours cannot be negative, please enter the correct value")
            elif (value> maximum) :
                print("Number of hours cannot be more than 168 hours in a week, please enter the correct value")
            else :
                need_value = False
        except ValueError :
            print("You entered a non numeric value..... Please enter the correct value")
    return value


#Defining Hourly Rate function to ensure non-negative and numeric value is entered by the employee
def get_rate (prompt,minimum) :
    need_value = True
    while (need_value) :
        try :
            value = float(input(prompt))
            if(value < minimum) :
                print("Hourly rate cannot be negative, please enter the correct value")
            else :
                need_value = False
        except ValueError :
            print("You entered a non numeric value..... Please enter the correct value")
    return value

        
#Defining Deduction percentage function to ensure non-negative and integral value is entered by the employee
def int_deductions (prompt,minimum) :
    need_value = True
    while (need_value) :
        try :
            value = int(input(prompt))
            
            if value < minimum :
                print("Percentage deduction cannot be negative value, please enter the correct value")
                                
            else :
                need_value = False

        except ValueError :
            print("You entered a non integral value..... Please enter the correct value")
    return value


#Ask the employee for first name and last name
first_name = input ("What is your first name?: ")
last_name = input ("What is your last name?: ")

#Ask the employee for number of hours worked in a week
num_hours = get_hours("How many hours worked in a week?: ", 0, 168)

#Ask the employee for hourly pay rate
hourly_rate = get_rate("What is your per hour rate?: $",0)

#Ask the employee for deductions
while True :
    deductions = input("Do you want your deductions removed from your gross pay? (Y/N) :")

    if deductions == "Y" :                                                          #If deductions is Yes, then ask for %tage
        percent_deducted = int_deductions ("What percent of Gross pay you want to deduct before calculation of your Net pay? :",0)
        break
    elif deductions == "N" :                                                        #If deductions is No, then set deductions as zero
        percent_deducted = 0
        break
    else :
        print ("Please enter either Y or N as your response")

#Check for over time
if (num_hours <= 40) :                                                              #If no over time
    gross_pay = (num_hours * hourly_rate)
else :
    gross_pay = ((40 * hourly_rate)+((num_hours-40) * 1.5 * hourly_rate))           #If worked over time then 1.5 times of hourly pay
    
#Calculate netpay
    deduction_amount = gross_pay * (percent_deducted/100)                           #Calculating deduction amount
    net_pay = gross_pay - deduction_amount                                          #Calculating Net pay

#Final outcomes
print ("Employee Name: ",first_name," ",last_name, sep="")
print ("Total hours worked in a week: ", num_hours," hours", sep="")
if (num_hours > 40) :
    print ("Total overtime hours worked: ",num_hours - 40," hours", sep="")         #printing overtime only if over time applies
print ("The hourly rate pay: ${0:,.2f}".format(hourly_rate))
print ("The gross pay: ${0:,.2f}".format(gross_pay))
print ("Total deductions: ${0:,.2f}".format(deduction_amount))
print ("Total Net pay: ${0:,.2f}".format(net_pay))




    




