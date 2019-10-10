#--------------------
# Name: exercise9.py
# Purpose: To practice newly taught python methods. 
#
# Author: Haider Zaidi
# Created: 11/12/2018
# Updated: 11/12/2018 - 2:01 PM 
#--------------------

#--- Impports
import replit # Imports the replit module.
import time # Imports the time module.
from termcolor import cprint # Imports the termcolor module.

launchScreen = '''
  _____ _______   _____                        _                        _   
 |_   _|__   __| |  __ \                      | |                      | |  
   | |    | |    | |  | | ___ _ __   __ _ _ __| |_ _ __ ___   ___ _ __ | |_ 
   | |    | |    | |  | |/ _ \ '_ \ / _` | '__| __| '_ ` _ \ / _ \ '_ \| __|
  _| |_   | |    | |__| |  __/ |_) | (_| | |  | |_| | | | | |  __/ | | | |_ 
 |_____|  |_|    |_____/ \___| .__/ \__,_|_|   \__|_| |_| |_|\___|_| |_|\__|
                             | |                                            
                             |_|                                                                                     
'''
# Assigns header text to variable launchScreen.

acceptableUsername = ['Haider', 'Seidel', 'Admin', 'admin'] # All acceptable inputs when prompted to enter username.
acceptablePassword = ['Adminpass', 'adminpass', '6612'] # All acceptable inputs when prompted to enter password.

acceptableMenu = [1, 2, 3, 4, 5, 6, 7, 8, 9] # All acceptable inputs for option selection in menu.
menuOptions = ['', 'Create New Account.', 'Delete Account', 'List of Accounts', 'List of Passwords',  'Database List', 'Provide Username and Password', 'I.T Expenses', 'Raw Account Data', 'List of Priority Accounts'] # List of menu options.
databaseList = [] # Creates empty list for function Database()
 
def menu(): # Defines function menu.
  print() # Prints blank space.
  
  for i in range(1, len(menuOptions), 1): # For loop to display menu options with number prefixes.
    print(str(i) +'. ' + str(menuOptions[i])) # Prints output of the for loop.
     
  print() # Prints a blank space.
  menuAsk = input('What option would you like to select?: ') # Prompts user to select a menu option.
  print() # Prints a blank space.
  menuAskOutput = int(menuAsk) # Converts user input to integer.
  
  if menuAskOutput == 1: # If the user inputs 1 the following code is executed.
    replit.clear() # Clears console.
    print() # Prints blank space.
    print(launchScreen) # Prints header.
    createAccount() # Calls function create account.
 
  elif menuAskOutput == 2: # If the user inputs 2 the following code is executed.
    replit.clear() # Clears console.
    print() # Prints blank space.
    print(launchScreen) # Prints header.
    deleteAccount()

  elif menuAskOutput == 3: # If the user inputs 3 the following code is executed.
    replit.clear() # Clears console.
    print() # Prints blank space.
    print(launchScreen) # Prints header.
    listAccount()
  elif menuAskOutput == 4: # If the user inputs 4 the following code is executed.
    replit.clear() # Clears console.
    print() # Prints blank space.
    print(launchScreen) # Prints header.
    listPass()
  elif menuAskOutput == 5: # If the user inputs 5 the following code is executed.
    replit.clear() # Clears console.
    print() # Prints blank space.
    print(launchScreen) # Prints header.
    Database()
  elif menuAskOutput == 6: # If the user inputs 6 the following code is executed.
    replit.clear() # Clears console.
    print() # Prints blank space.
    print(launchScreen) # Prints header.
    provide()
  elif menuAskOutput == 7: # If the user inputs 7 the following code is executed.
    replit.clear() # Clears console.
    print() # Prints blank space.
    print(launchScreen) # Prints header.
    it_expenses()

  elif menuAskOutput == 8: # If the user inputs 8 the following code is executed.
    replit.clear() # Clears console.
    print() # Prints blank space.
    print(launchScreen) # Prints header.
    rawData()

  elif menuAskOutput == 9: # If the user inputs 9 the following code is executed.
    replit.clear() # Clears console.
    print() # Prints blank space.
    print(launchScreen) # Prints header.
    priority()



  elif menuAskOutput not in acceptableMenu: # If the user's input is not one of the acceptable menu options the following code is executed.
    print('Error: Option selected not found, try again') # Prints error message.
    time.sleep(3) # Delays the execution of the next line of code by 3 seconds.
    replit.clear() # Clears console.
    menu() # Calls menu function.
  return menuAsk # Returns menuAsk (Exits Function)

def provide(): # Defiens function provide.
  print('Username:' + acceptableUsername[-3]) # Prints the 3rd username from the left from the list acceptableUsername,
  print('Password:' + acceptablePassword[-2]) # Prints the 2nd password from the left in acceptablePassword.

def createAccount(): # Defines function createAccount
  print('Please fill the following fields to create a new account.') # Prints statement message.
  print() # Prints blank space.

  createUser = input('Account Username: ') # Prompts user to enter new account name.
  acceptableUsername.append(str(createUser)) # Adds users input to the list acceptableUsername.

  createPass = input('Account Password: ') # Prompts user to enter new password.
  acceptablePassword.append(str(createPass)) # Adds users input to the list acceptablePassowrd
  
  print('Notification: New account has been created.') # Prints notification message.
  time.sleep(0.5) # Delays the execution of the next line of code by 0.5 seconds.
  print('Returning to login page.') # Prints statement message.
  time.sleep(2) # Delays the execution of the next line of code by 2 seconds.
  replit.clear() # Clears console.
  print() # Prints blank space.
  login() # Calls the login function.

def deleteAccount():
  delUser = input('Account Username: ') # Prompts user to enter an account username they want to delete.
  acceptableUsername.remove(str(delUser)) # Removes an account in acceptableUsername based upon the user input.

  delPass = input('Account Password:') # Prompts user to enter an password they wantt o delete.
  acceptablePassword.remove(str(delPass)) # Removes a password in acceptablePassword based upon the user input.

  cprint('Deleting Account...', attrs=['blink']) # Prints loading message, blinks.
  time.sleep(3) # Delays the execution of the next line of code by 3 seconds.
  print() # Prints blank space.

  print('The username and password provided has been deleted, returning to login page.') # Prints statement message.
  
  login() # Calls login function,

def listAccount(): # Defines function list account.
  acceptableUsername.sort() # Sorts the list acceptableUsername in alphabetical order.
  for i in acceptableUsername: # For loop to print acceptableUsername (sorted)
    print(i) # Prints the sorted version of acceptableUsername

def listPass(): # Defines function list pass.
  acceptableUsername.sort() # Sorts the list acceptablePassword in alphabetical order.
  for i in acceptablePassword: # For loop to print acceptablePassword (sorted)
    print(i) # Prints the sorted version of acceptablePassword



def Database(): # Defines function database.
  print('List of Databases: ') # Prints statement message.
  print() # Prints blank space.
  databaseList.append('acceptableUsername') # Adds the name of the list 'acceptableUsername' to a main list called databaseList.
  databaseList.append('acceptablePassword') # Adds the name of the list 'acceptablePassword' to a main list called databaseList.
  databaseList.append('acceptableMenu') # Adds the name of the list 'acceptableMenu' to a main list called databaseList.
  databaseList.append('menuOptions') # Adds the name of the list 'acceptableMenuOptions' to a main list called databaseList.


  for item in databaseList: # For loop to print all items in databaseList.
    print(item) # Prints all items in databaseList



def it_expenses(): # Defines function it_expenses
    toppingsAsk = input('Please input all expense transactions, seperate transactions via spaces.') # Prompts user to enter expenses.
    print() # Prints blank space.
    toppingsAskOutput = toppingsAsk.split() # Converts the input from toppingsAsk into a list, seperates inputs via spaces. # Takes the users input, places it into a list, seperates inputs in the list via spaces.
    toppingsAskOutput2 = list(map(float, toppingsAskOutput)) # Converts the list created by the users input into a float.
    print('List of all I.T Expenses: ') # Statemebt nessage,
    print() # Prints blank message.


    for item in toppingsAskOutput2: # For loop to print all expenses.
      print('$' + str(item)) # Prints all expenses.

    totalExp = sum(toppingsAskOutput2) # Totals all items in the expenses list.
    print() # Prints blank space.
    print('Total I.T Expenses: $' + str(totalExp)) # Prints total expenses.

def rawData(): # Defines function rawData.
  rawDataInfo = acceptableUsername + acceptablePassword # Combines the list of acceptableUsername and acceptablePassword to one list called "rawDataInfo"
  print('List of accounts and passwords: ') # Prints statement message.
  print() # Prints blank space.

  for item in rawDataInfo: # For loop to print all raw data.
    print(item, end=', ') # Prints all raw data in one line, seperated by commas.

def priority(): # Defines function priority.
  print('The following accounts have full priority (admin privilleges): ') # Prints statement message.
  print() # Prints blank space.

  priority_list = acceptableUsername.copy() # Duplicates acceptableUsername, names duplicat as priority_list.
  priorityOutput = priority_list[2:4] # Slices priority_list 

  for accounts in priorityOutput: # For loop to print all priority accounts.
    print(accounts) # Prints prioprity accounts.




def login(): # Defines function login/
  print() # Prints blank space.
  print(launchScreen) # Prints launch screen.
  print() # Prints blank space.

  loginUsername = input('Username:') # Prompts user to enter password.
  time.sleep(0.2) # Adds 2 second delay before the next line of code is executed.
  loginPassword = input('Password:')

  if loginUsername in acceptableUsername and loginPassword in acceptablePassword: # If the users username and password is correct the following code is executed.

    print('Access granted.') # Prints success message.
    print() # Prints blank space.
    print('Welcome, ' + str(loginUsername) + '!') # Welcomes user based upon username inputted.
    menu() # Calls menu function/
  
  elif loginUsername not in acceptableUsername or loginPassword not in acceptablePassword: # If the users username or password is incorrect the following code is executed.

    print('Access denied, try again.') # Prints an error message.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    replit.clear() # Clears console.
    login() # Calls login function.
login() # Calls login function

  
