#-------
# Name: exercise10.py
# Purpose: To contrast the differences between tuples and lists.
#
# Author: Haider Zaidi:
# Created: 11/20/2018
# Updated: 11/20/2018 2:30PM
#-------

#--- Imports
from termcolor import cprint #Imports cprint from the termcolor module, allows for blinking text.
import replit # Imports replit module, used to clear the console. 
import time # Imports the time module, allows for delayed printing of text.

fundementals = [('bread', 'tomato sauce', 'cheese')] # Creates tuple named fundmentals.

def launchScreen(): # Defines function launch screen.
  header = '''
  _    _               _____ _                        _       
 | |  | |             |  __ (_)                      (_)      
 | |  | |_ __   ___   | |__) | __________ _  ___ _ __ _  __ _ 
 | |  | | '_ \ / _ \  |  ___/ |_  /_  / _` |/ _ \ '__| |/ _` |
 | |__| | | | | (_) | | |   | |/ / / / (_| |  __/ |  | | (_| |
  \____/|_| |_|\___/  |_|   |_/___/___\__,_|\___|_|  |_|\__,_|
  
                                                              '''
  # Assigns the header which is comprised of ASCII Art (http://patorjk.com/software/taag/) to the variable header.                                                            
  print(header) # Prints the header.                                                             

def pizza(): # Defines function pizza.
  launchScreen() # Calls function launchScreen
  for basePizza in fundementals: # For loop for tuple named fundementals.
    base, sauce, layer = basePizza # Assigns each value in the tuple a variable, i.e since bread is the first value in the tuple, bread will be assigned to variable 'Base'.
    baseToppings = base + ', ' + sauce + ' and ' + layer # String that combines all variables from the tuple fundementals, uses commas and keyword 'and' to seperate values.
    baseToppingsNoAnd = base + ', ' + sauce + ', ' + layer # String that combines all variables from the tuple fundementals, uses only commas to seperate the values.
  
  toppingsAsk = input('What toppings would you like on a pizza with ' + baseToppings + '?:') # Asks user what toppings they would like on a pizza with the values from the tuple fundementals.
  toppingsAskCapitalize = toppingsAsk.title() # Capitalizes the first word of every string in the list. 
  toppingsAskOutput = toppingsAskCapitalize.split() # Takes the capitalzie version of the users input, places it in a list. Seperates strings based upon spaces (default).

  if str('Pineapple') in toppingsAskOutput: # If the users input contained pineapple, the following code is executed. 
    print() # Prints a blank space.
    print('Pineapple sucks, pick something else!') # Prints a notification message.
    toppingsAskOutput.clear() # Clears the list created by the users input to allow the user to input new toppings.
    print() # Prints blank space.
    time.sleep(2) # Adds a 2 second delay before the next lien of code is executed.
    replit.clear() # Clears the console.
    pizza() # Calls function pizza.
  
  else: # If the users input doesn't contain pineapple in it, the following code is executed. 
    print() # Prints blank space.
    cprint('Ordering Pizza...', attrs=['blink']) # Prints 'Ordering Pizza' loading message, blinking.
    time.sleep(1.5) # Adds a 1,.5 second delay before the next line of code is executed.
    print() # Prints blank space.
    print('A pizza with ' + baseToppingsNoAnd + ' and ' + 'the following toppings has been ordered:') # Prints base pizza order.
    print() # Prints blank space.
    
    for toppings in toppingsAskOutput: # For loop to print users inputted toppings.
      print(toppings) # Prints the toppings inputted by the user on seperate lines.
      
pizza() # Calls function pizza.

