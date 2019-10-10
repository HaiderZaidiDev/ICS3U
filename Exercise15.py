#-----------
# Name: exercise15.py
# Purpose: To practice using write conventions in Python.
#
# Author: Haider Zaidi
# Created: 12/11/2018
# Updated: 12/15/2018 - 1:05PM (Fixed commenting errors post submition.)
#-----------

import time # Imports time module. 

import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info('Start of program.')

acceptableMenuOptions = ['1', '2', '3'] # List containign acceptable input options in the menu. 
submitCount = {'Field Reports' : 0} # Dictionary to account for amount of field reports.


def submit(): # Defines function submit. 
  '''
  Submits field reports based on user input.
  
  This function uses writing conventions to write a users input to a file, field_reports.txt

  Parameters
  ----------
  none
  
  Returns
  -------
  none
  '''
  logging.info('Start of function submit.')
  logging.info('Increasing value of submitCount')
  submitCount['Field Reports'] += 1 # Adds 1 to the value of fieldReports in dictionary submitCount.
  print() # Prints blank space. 
  logging.info('Requesting user input for report.')
  reportAsk = input('Enter Field Report:') # Requests input from user.
  print() # Prints blank space. 
  
  logging.info('Opening file field_reports.txt to write.')
  reportFile = open('field_reports.txt', 'w') # Opens file field_reports with the intent to write, assigns file with a variable. 
  logging.info('Writing user input to file field_reports.txt')
  reportFile.writelines(reportAsk) # Writes users input to file.
  logging.info('Closing file field_reports.txt')
  reportFile.close() # Closes all operations related to file.
  
  print('Field report has been submitted, returning to menu.') # Field report submitted success message.
  print() # Prints blank space. 
  time.sleep(2) # Delays execution of next line of code by 2 seconds. 
  menu() # Calls function menu.
  logging.info('End of function submit.')

def comment(): # Defines function comment. 
  '''
  Submits field reports based on user input.
  
  This function uses writing conventions to write a users input to a file, field_reports.txt

  Parameters
  ----------
  none
  
  Returns
  -------
  none
  '''

  logging.info('Start of function comment.')
  logging.info('Requesting user input for comment.')
  commentAsk = input('Enter comment(s) to the last field report entered: ') # Requests user input.
  logging.info('Opening file field_reports.text to append. ')
  commentFile = open('field_reports.txt', 'a') # Opens file field_reports.txt with the intent to append.  
  logging.info('Appending to file field_reports.txt')
  commentFile.write(' COMMENTS: ' + commentAsk) # Appends user input to previous field report with prefix.
  logging.info('Closing file field_reports.txt')
  commentFile.close() # Closes all operations related to file.
  
  print() # Prints blank space. 
  print('Field report comments have been submitted, returning to menu.') # Prints append success message.
  print() # Prints blank space. 
  time.sleep(2) # Delays execution of next line of code by 2 seconds.
  menu() # Calls function menu.
  logging.info('End of function comment.')

  

def menu(): # Defines function menu.
  '''
  Displays menu. 
  
  This function displays menu options to the user and calls
  specific functions based upon the user input. 

  Parameters
  ----------
  none
  
  Returns
  -------
  none
  '''
  logging.info('Start of function menu.')
  logging.info('Displaying menu options.')
  print('1. Submit a field report.') # Prints option 1 description.
  print('2. View a field report.') # Prints option 2 description.
  print('3. Add comments to a field report.') # Prints option 3 description.
  print() # Prints blank space. 
  
  logging.info('Requesting user input for menu.')
  menuAsk = input('What option would you like to select?: ') # Requests user input for menu option.
  
  logging.info('Calling functions based upon user input.')
  if menuAsk == str('1'): # If user input is 1, the following code is executed.
    submit() # Calls function submit. 
    
  elif menuAsk == str('2'): # If user input is 2, the following code is executed.
    view() # Calls function view.
    
  elif menuAsk == str('3'): # If user input is 3, the following code is executed.
    comment() # Calls function comment.
  
  elif menuAsk not in acceptableMenuOptions: # If the user input is not 1, 2 or 3 (acceptableMenuOptions)
    print() # Prints blank space. 
    print('Error: Unknown option selected, restarting!') # Prints error message.
  logging.info('End of function menu.')

def view(): # Defines function view.
  '''
  Prints lines from a file.
  
  This function uses reading conventions to read all lines of a file and then
  outputs the data to the user. 

  Parameters
  ----------
  none
  
  Returns
  -------
  none
  '''
  logging.info('Start of function view.')
  logging.info('Determining if there are any active field reports.')
  if submitCount['Field Reports'] > 0: 
    logging.info('Opening file field_reports.txt with intent to read.')
    reportView = open('field_reports.txt', 'r') # Opens file field_reports.txt with the intent to read, assigns file with a variable. 
    logging.info('Reading lines in file field_reports.txt')
    fieldReports = reportView.readlines() # Reads all lines in the file field_reports.txt

    logging.info('Printing lines in field_reports.txt')  
    for lines in fieldReports: # For loop to print lines in file field_reports.txt, iterator as data in file. 
      print() # Prints blank space. 
      print(lines) # Prints lines. 
      print() # Prints blank space. 
    
    logging.info('Requesting user menu return input.')
    menuBack = input('Would you like to go back to the main menu?: ')
      
    logging.info('Calling functions based upon menu return input.')
    if menuBack.lower()== str('yes'): # If the lowercase conversion of menuBack is 'yes', the following code is executed.
      print() # Prints blank space. 
      print('Returning to menu.') # Pritns returning message.
      menu() # Calls function menu.
  
    elif menuBack.lower() == str('no'): # If the lowerase conversion of menuBack is 'no', the following code is execited. 
      print() # Prints blank space. 
      print('Restarting function.')
      view() # Calls function view.
  
    else: # If the user didn't enter either yes or no, the following code is executed. 
      print('Unknown option selected, restarting function.') # Prints error message.
      time.sleep(2) # Adds a 2 second delay before the next line of code is executed. 
      view() # Calls function view.
    
  else: # If there are no field reprots available (submitCount['Field Reports'] is equal to 0) the following code is executed.
      logging.info('Returning to menu due to no field reports available.')
      print('No field reports available, returning to menu.') # Prints error returning message.
      time.sleep(2)  # Adds a 2 second delay before the next line of code is executed.
      menu() # Calls function menu.
  logging.info('Closing file field_reports.txt')     
  reportView.close() # Closes all operations related to the file. 
  logging.info('End of function view.')
menu() # Calls function menu.
logging.info('End of program.')

#--- End of code. 
  
    
  
