#-------
# Name: exercise12.py
# Purpose: Demonstrate understanding of dictionaries and their relations. 
#
# Author: Haider Zaidi
# Created: 2018-11-29
# Updated: 2018-11-29 (6:33PM)
#--------

import urllib.request # Imports urllib.request module, allows for reading of web pages.
from termcolor import cprint # Imports cprint from module termcolor, used for printing blinking text.
from colorama import Fore, Style # Imports Fore and Style from Colorama, allows for coloured and styled text.
import time # Imports time module, used for delaying prints.
import replit # Imports replit module, used for clearing console.

import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info('Program launch.')


stockList = ['','i7-8700k', 'i7-9700k', 'i9-9900k'] # Creates a list with the names of all the CPU's, data in lists can't be assigned values. 
currentStock = {'i7-8700k' : 12, 'i7-9700k' : 3, 'i9-9900k' : 7} # Creates a dictionary and assigns values to each key. 
cpuPrice = [('$490', '$549', '$749')] # Creates a tuple with prices of the CPU's, tuples can't be edited/changed in any way, meaning the MSRP of these products can't change. 

for prices in cpuPrice: # For loop with iterator prices to reference keys in the tuple 'cpuPrice'
  cpu8700k, cpu9700k, cpu9900k = prices # Assigns variables for keys in the tuple 'cpuPrice', variables represent the prices of CPUs.
  



header = ''' 
   _____ _____  _    _    _____            _             _ 
  / ____|  __ \| |  | |  / ____|          | |           | |
 | |    | |__) | |  | | | |      ___ _ __ | |_ _ __ __ _| |
 | |    |  ___/| |  | | | |     / _ \ '_ \| __| '__/ _` | |
 | |____| |    | |__| | | |____|  __/ | | | |_| | | (_| | |
  \_____|_|     \____/   \_____|\___|_| |_|\__|_|  \__,_|_|
                                                           
                     
                                                       '''
# Assigns Ascii art to variable.

logging.info('Printing header.')
print(header) # Prints header.
print('Welcome to CPU Central!') # Prints welcome message. 

logging.info('Start of function shop.') 
def shop(): #  Defines function 'shop'.
  print() # Prints blank space. 
  
  logging.info('Printing list of products in stock.')
  for i in range(1, len(stockList), 1): # For loop to display list of products carried with number suffixes. Products carried are under the list 'stockList'
    print(str(i) +'. ' + str(stockList[i])) # Prints output of the for loop.
  
  print() # Prints blank space.  
  
  logging.info('Requesting user input for CPU choice.')
  cpuAsk = input('What CPU would you like to purchase?: ') # Asks the user what CPU they would like to purchase. 
  print() # Prints blank space. 
  
  if cpuAsk == str('1'): # If the user inputs option 1 the following code is executed.
    logging.info('Checking if selected CPU is in stock.')
    if currentStock['i7-8700k'] > 0 : # Checks if the CPU is in stock.
      cpuAmount = input("How many CPUs would you like to purchase?:") # Asks the user the quantity of their purchase.
      print() # Prints a blank space.
      
      cpuAmountInt = int(cpuAmount) # Converts the users quantity input for an integer (This is only used to check if there is sufficent stock for the quantity)
      
      logging.info("Checking if there is enough stock for the user's purchase.")
      if cpuAmountInt > currentStock['i7-8700k']: # If the quantity the user wants to purchase is more then whats in stock, the following code is executed.
        logging.info('Outputting not enough stock error.')
        print("Sorry, we don't have enough stock for your purchase. There are currently: " + str(currentStock['i7-8700k']) + " i7-8700ks left in stock!") # Prints an errr message with number of remaining stock.
        print() # Prints blank message.
        print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notification.
        print() # Prints blank message.
        time.sleep(1) # Delays the execution of the next line of code by 1 second.
        shop() # Calls function shop.
        
      else:
       logging.info('Confirming CPU Purchase.')
       purchaseConfirm8700k = input('This CPU costs ' + cpu8700k + ', are you sure you would like to purchase this product?:') # Gets confirmation of product purchase from user. 
       purhcaseConfirm8700kLower = purchaseConfirm8700k.lower() # Converts users inputs to lowercase for verification purposes (Omits need to have list of acceptable options for different cAsE sEnSitiVity)
       print() # Prints blank space. 
       if purhcaseConfirm8700kLower == str('yes'): # If the user inputs yes, the following code is executed. 
         logging.info('Success! Purchase has been completed.')
         print('Your CPU has been purchased and will be deliverd wihtin 5 business days!') # Prints success message. 
         logging.info('Adjusting product stock.')
         currentStock['i7-8700k'] -= cpuAmountInt # Subtracts one from the stock amount of the 8700k.
         print('There are currently: ' + str(currentStock['i7-8700k']) + ' i7-8700ks left in stock!') # Tells the user how much of the CPU they purchased is left in stock.
       elif purhcaseConfirm8700kLower == str('no'): # If the user inputs no, the following code is executed.
         logging.info('Notification sequence for denied purchase, returning to menu.')
         print() # Prints blank space. 
         print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notificatio.
         print() # Prints blank message.
         time.sleep(1) # Adds a 1 second delay before the next line of code is executed.
         shop()
       else: 
         logging.info('Invalid input error sequence.')
         print() # Prints blank message. 
         print(Fore.RED + 'Error:' + Style.RESET_ALL + 'Invalid input, Returning to shop menu..') # Prints error
         print() # Prints blank space. 
         time.sleep(1) # Delays the execution of the next line of code by 1 second.
         shop()# Calls function shop. 
       
    else: # If the CPU the user selected is out of stock, the following code is executed.
      logging.info('Error sequence, product out of stock.')
      print(Fore.RED + 'Error:' + Style.RESET_ALL + 'Sorry, that CPU is currently out of stock!') # Prints error message. 
      print() # Prints blank message.
      print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notification message.
      print() # Prints blank message.
      time.sleep(1) # Adds a 1 second delay before the next line of code is executed.
      shop() # Calls function shop.
      
  if cpuAsk == str('2'): 
    logging.info('Checking if selected CPU is in stock.')
    if currentStock['i7-9700k'] > 0 : # Checks if the CPU is in stock.
      cpuAmount = input("How many CPUs would you like to purchase?:") # Asks the user the quantity of their purchase.
      print() # Prints a blank space.
      
      cpuAmountInt = int(cpuAmount) # Converts the users quantity input for an integer (This is only used to check if there is sufficent stock for the quantity)
      
      logging.info("Checking if there is enough stock for the user's purchase.")
      if cpuAmountInt > currentStock['i7-9700k']: # If the quantity the user wants to purchase is more then whats in stock, the following code is executed.
        logging.info('Outputting not enough stock error.')
        print("Sorry, we don't have enough stock for your purchase. There are currently: " + str(currentStock['i7-9700k']) + " i7-9700ks left in stock!") # Prints an errr message with number of remaining stock.
        print() # Prints blank message.
        print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notification.
        print() # Prints blank message.
        time.sleep(1) # Delays the execution of the next line of code by 1 second.
        shop() # Calls function shop.
        
      else:
       logging.info('Confirming CPU Purchase.')
       purchaseConfirm9700k = input('This CPU costs ' + cpu9700k + ', are you sure you would like to purchase this product?:') # Gets confirmation of product purchase from user. 
       purhcaseConfirm9700kLower = purchaseConfirm9700k.lower() # Converts users inputs to lowercase for verification purposes (Omits need to have list of acceptable options for different cAsE sEnSitiVity)
       print() # Prints blank space. 
       if purhcaseConfirm9700kLower == str('yes'): # If the user inputs yes, the following code is executed. 
         logging.info('Success! Purchase has been completed.')
         print('Your CPU has been purchased and will be deliverd wihtin 5 business days!') # Prints success message. 
         logging.info('Adjusting product stock.')
         currentStock['i7-9700k'] -= cpuAmountInt # Subtracts one from the stock amount of the 9700k.
         print('There are currently: ' + str(currentStock['i7-9700k']) + ' i7-9700ks left in stock!') # Tells the user how much of the CPU they purchased is left in stock.
       elif purhcaseConfirm9700kLower == str('no'): # If the user inputs no, the following code is executed.
         logging.info('Notification sequence for denied purchase, returning to menu.')
         print() # Prints blank space. 
         print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notificatio.
         print() # Prints blank message.
         time.sleep(1) # Adds a 1 second delay before the next line of code is executed.
         shop()
       else: 
         logging.info('Invalid input error sequence.')
         print() # Prints blank message. 
         print(Fore.RED + 'Error:' + Style.RESET_ALL + 'Invalid input, Returning to shop menu..') # Prints error
         print() # Prints blank space. 
         time.sleep(1) # Delays the execution of the next line of code by 1 second.
         shop()# Calls function shop. 
       
    else: # If the CPU the user selected is out of stock, the following code is executed.
      logging.info('Error sequence, product out of stock.')
      print(Fore.RED + 'Error:' + Style.RESET_ALL + 'Sorry, that CPU is currently out of stock!') # Prints error message. 
      print() # Prints blank message.
      print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notification message.
      print() # Prints blank message.
      time.sleep(1) # Adds a 1 second delay before the next line of code is executed.
      shop() # Calls function shop.
      
      
  if cpuAsk == str('3'):
    logging.info('Checking if selected CPU is in stock.')
    if currentStock['i9-9900k'] > 0 : # Checks if the CPU is in stock.
      cpuAmount = input("How many CPUs would you like to purchase?:") # Asks the user the quantity of their purchase.
      print() # Prints a blank space.
      
      cpuAmountInt = int(cpuAmount) # Converts the users quantity input for an integer (This is only used to check if there is sufficent stock for the quantity)
      
      logging.info("Checking if there is enough stock for the user's purchase.")
      if cpuAmountInt > currentStock['i9-9900k']: # If the quantity the user wants to purchase is more then whats in stock, the following code is executed.
        logging.info('Outputting not enough stock error.')
        print("Sorry, we don't have enough stock for your purchase. There are currently: " + str(currentStock['i9-9900k']) + " i9-9900ks left in stock!") # Prints an errr message with number of remaining stock.
        print() # Prints blank message.
        print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notification.
        print() # Prints blank message.
        time.sleep(1) # Delays the execution of the next line of code by 1 second.
        shop() # Calls function shop.
        
      else:
       logging.info('Confirming CPU Purchase.')
       purchaseConfirm9900k = input('This CPU costs ' + cpu9900k + ', are you sure you would like to purchase this product?:') # Gets confirmation of product purchase from user. 
       purhcaseConfirm9900kLower = purchaseConfirm9900k.lower() # Converts users inputs to lowercase for verification purposes (Omits need to have list of acceptable options for different cAsE sEnSitiVity)
       print() # Prints blank space. 
       if purhcaseConfirm9900kLower == str('yes'): # If the user inputs yes, the following code is executed. 
         logging.info('Success! Purchase has been completed.')
         print('Your CPU has been purchased and will be deliverd wihtin 5 business days!') # Prints success message. 
         logging.info('Adjusting product stock.')
         currentStock['i9-9900k'] -= cpuAmountInt # Subtracts one from the stock amount of the 9900k.
         print('There are currently: ' + str(currentStock['i9-9900k']) + ' i9-9900ks left in stock!') # Tells the user how much of the CPU they purchased is left in stock.
       elif purhcaseConfirm9900kLower == str('no'): # If the user inputs no, the following code is executed.
         logging.info('Notification sequence for denied purchase, returning to menu.')
         print() # Prints blank space. 
         print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notificatio.
         print() # Prints blank message.
         time.sleep(1) # Adds a 1 second delay before the next line of code is executed.
         shop()
       else: 
         logging.info('Invalid input error sequence.')
         print() # Prints blank message. 
         print(Fore.RED + 'Error:' + Style.RESET_ALL + 'Invalid input, Returning to shop menu..') # Prints error
         print() # Prints blank space. 
         time.sleep(1) # Delays the execution of the next line of code by 1 second.
         shop()# Calls function shop. 
       
    else: # If the CPU the user selected is out of stock, the following code is executed.
      logging.info('Error sequence, product out of stock.')
      print(Fore.RED + 'Error:' + Style.RESET_ALL + 'Sorry, that CPU is currently out of stock!') # Prints error message. 
      print() # Prints blank message.
      print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notification message.
      print() # Prints blank message.
      time.sleep(1) # Adds a 1 second delay before the next line of code is executed.
      shop() # Calls function shop.
      
  else: # If the user inputs an uknown menu option the following code is executed.
      print(Fore.RED + 'Error:' + Style.RESET_ALL + 'Unknown option selected, restarting!') # Prints error message.
      print() # Prints blank message.
      print(Fore.GREEN + 'Notification:' + Style.RESET_ALL + ' Returning to shop menu.') # Prints notification message.
      print() # Prints blank message.
      time.sleep(1) # Delays the execution of the next line of code by 1 second.
      shop() # Calls shop function.
    
shop() # Calls shop function.
