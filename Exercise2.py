#--------------------------------------------------
# Name: Exercise2.py
# Purpose: To practice using basic operations and commands in Python with variables.
#
# Author: Haider Zaidi
# Created: 10/10/2018
# Updated: 1:42 PM (10/09/2018)
#---------------------------------------------------
accounting = str('Trial Balance') # Variable for the header. 
liabillities = 6 # Assigns the value of 6 to liabilities. 
equity = 5 # Assigns the value of 5 to equity.
revenue = float(24.3) # Assigns revenue the float of 24.3.
expenses = float(6.2) # Assigns expenses to the float of 6.2
amountPurchased = float(34.5) # Assigns amountPurchased to the float of 34.5.
purchaseCost = float(2.6) # Assigns quantityPurchased to the float of 2.6.
totalCash = 50 # Assigns totalCash to the integer 50.
quantityDemand = 6 # Assigns quantityDemand to the integer 6.
productPrice = 3 # Assigns productPrice to the integer 3.
remainingStock = 4 # Assigns remainingStock to the integer 4.


print(accounting)
print(liabillities + equity) # Adds liabillities and equity (Used to calculate assets).
print(revenue - expenses) # Subtracts revenue and expenses (Used to calculate total profit).
print(amountPurchased*purchaseCost) # Multiplies amountPurchased by purchaseCost (Used to calculate total cost when buying in bulk)
print(totalCash/2) # Divides totalCash available by 2 (Used to calculate amount of cash remaining)
print(quantityDemand//4) # Divides quantityDemand by 4 and rounds to the lowest whole number. 
print(10%productPrice) # Divides productPrice by 10 and outputs the remainder. 
print(int(9/remainingStock)) # Divides remainingStock by 9.
print((amountPurchased*purchaseCost)+24/6-10//3%2) # Multiplies amountPurchased by purchaseCost and evalutes the total price including various fees. 
