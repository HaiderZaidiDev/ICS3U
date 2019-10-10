#--------------------------------------------------
# Name: Exercise3.py
# Purpose: To calculate total profit after accounting for revenue and expenses.
#
# Author: Haider Zaidi
# Created: 10/11/2018
# Updated: 12:31 PM (10/11/2018)
#---------------------------------------------------
revenue = input('What is your total revenue?: ') # Input for total revenue.
expenses = input('What are your total expenses?: ') # Input for total expenses.
profit = (int(revenue) - int(expenses)) # Variable to calculate profit.
print('Your total profit is: \u0024' + str(profit))  # Calculates total profit and outputs it.
