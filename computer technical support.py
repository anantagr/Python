#Technical support program for the user

import sys

#Asking customer if the Computer's beeps when turned ON
computer_beep = input ("Does your computer beep when powered on? Enter Y or N: ")
if not ((computer_beep == "Y") or (computer_beep == "N")) :
    print ("Incorrect input, please restart the program and input either Y or N")
    sys.exit()

#Asking customer if the hard disk spins when turned ON
drive_spin = input ("Does your computer hard drive spins when powered on? Enter Y or N: ")
if not ((drive_spin == "Y") or (drive_spin == "N")) :
    print ("Incorrect input, please restart the program and input either Y or N")
    sys.exit()

#check the replies and print accordingly
if computer_beep == "N" and drive_spin == "Y" :
    print ("Check the speaker contacts") #Condition when computer does not beeps but hard drive spin

elif computer_beep == "Y" and drive_spin == "Y" :
    print ("Contact Tech Support") #Condition when computer beeps and hard drive spin

elif computer_beep == "Y" and drive_spin == "N" :
    print ("Check Drive cables") #Condition when computer beeps but hard drive does not spin
    
else :
    print ("Bring computer to repair center") #Condition when computer does not beeps and hard drive does not spin


#Leave a comment before exiting the program.
print ("Thank you, have a good day")

