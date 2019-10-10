#------------------------------------
# Name: Exercise4.py
# Purpose: To calculate if a invidiual or business is making profit, lets the user know the final result. 
#
# Author: Haider Zaidi
# Created: 10/11/2018
# Updated: 1:01 PM (10/11/2018)
#-------------------------------------

#--- Profit Output
revenue = input('What is your total revenue?: ') # Input for total revenue.
expenses = input('What are your total expenses?: ') # Input for total expenses.
profit = (int(revenue) - int(expenses)) # Calculates total profit (revenue subtracted by expenses) and outputs it.
print('Your total profit is: \u0024' + str(profit))  # example 2

print('') # Adds a space between profit output and profit statement. 

#--- Profit statement

if profit < 0: # Checks if profit is less then 0. 
  print("You're loosing money! Profit is in the red.") # Outputs if profit is less than 0.
elif profit >= 1: # Checks if profit is greater than or equal to 1. 
  print("You're making money! Profit is in the black.") # Outputs if profit is greater than or equal to 1. 
elif profit == 0: # Checks if profit is 0 (Only number left). 
    print("You're not making any money! You're breaking even.") # Outputs if profit breakes even. 
# End of code.
    
