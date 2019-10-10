#------------------------------------
# Name: Exercise5.py
# Purpose: To create a web-terminal based alarm system.
#
# Author: Haider Zaidi
# Created: 10/11/2018
# Updated: 2:13 PM (10/18/2018)
#-------------------------------------

#------ Security Assistant

import time # Imports time module (Allows the abiltiy to add a delay between prints).
from colorama import Fore, Style # Imports a color module (Allows for colored text).
arming = 10 # Assigns the value of 10 to variable arming. 
disarm = 10 # Assigns the value of 10 to the variable disarm. 

print("Hello, I'm your automated personal security assistant. Please enter one of the following options:") # Prints introductury statement. 
print(" ") # Adds space between introductury statement and option statement. 
control = input("Stay | Away | Disarm | Police: ") # Prints option statementm assigns users input to variable control. 


#---- Away 
if control == str("Away"): # If the user enters Away, the following code will execute:
  print("Arming system, 10 seconds remain.") # Outputs arming statement. 
  print() # Adds space between output statement and countdown. 
  while arming > 0 and control == str("Away"): # Executes the following code while the user is on the "Away" page.
    arming = arming - 1 # Subtracts one from the value of arming each loop.
    time.sleep(1) # Adds a 1 second delay between prints. 
    print(Fore.GREEN + str(arming)) # Prints the value of arming in green.
    if arming == 1: # If arming has a value of 1, the following code is executed. 
       print() # Adds a space between final value of arming and armed statement.
       print(Fore.RED + "System has been armed.") # Prints arming statement in red. 
       break # Any code after this isn't included in the Away loop.

#----- Stay
elif control == str("Stay"): # If the user enters Stay, the following code will execute:
  print(Fore.GREEN + "System has been armed for stay. Please close any open doors or windows now.") # Prints stay arming statement in green.
  
elif control == str("Disarm"): # If the user enters Disarm, the following code will execute:
  print(Fore. GREEN + "System is now disarming.") # Prints disarming statement in green.
  print() # Adds space between disarming statement and countdown. 
  for disarm in range(5, 0, -1): # For loop to count down from 5. 
    time.sleep(1) # Adds a delay of one second between prints. 
    print(Fore.RED + str(disarm)) # Prints the value of disarm. 
    if disarm == 1: # If the value of disarm is equal to 1, the following code will execute. l
     print() # mAdds a space between the final number of the countdown and ending disarm statement. 
  print(Fore.GREEN + "System has been disarmed. ") # prints ending disarmed statement in green.

#---- Police
elif control == str("Police"): # If the user enters Police, the following code will execute:
  print(Fore.BLUE + "The Police have been dispatched, the silent alarm has now been activiated. Your emergency contacts have also been notified.") # Prints Police statement in blue.

#---- Error
else: # If the user enters anything besides the provided options, the following code executes:
  print(Fore.RED + "Error:" + Style.RESET_ALL + " Command not recognized, make sure you're spelling and capitalization is correct.") # Executes error statement.
