#------
# Name: Exercise13.py
# Purpose: To practice string manipulation. 
#
# Author: Haider Zaidi
# Created: 12/3/2018
# Updated: 12/12/2018 - 7:58PM
#------


import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info('Start of program.')
logging.info('Start of function.')

def start(): # Defines function start. 
  '''
  Provides information of an input. 
  
  This function uses conventions in relation to string manipulation to provide information
  of the users input, the function provides both informative and novelty data.

  Parameters
  ----------
  none
  
  Returns
  -------
  none
  
  Warnings (this section is optional)
  --------
  1 - This function may not perform correctly with a user input below 3 characters, some conventions in this function require 4 or more words. 
  
  2 -   here appears to be an issue with .isalnum where regardless of whether numbers or characters are entered, it will alwayus thinks it's alphanumeric.
        I have tested this issue for about 30 minutes and it appears to be an issue with spacing of the input. If you add a space before the input
        it is read as if it's not alphanumeric, if you don't it will always read as if it's alphanumeric. This could be an issue with Replit's project 
        mode however I'm not 100% sure. I have contacted Replit's support team about this via twitter (can provide proof and demonstation if requested).   
  '''

  logging.info('Variable assignment.')
#--- Variable Assignment 
  
  startAsk = input('What is your favorite quote?: ') # Requests user input.
  wordList = startAsk.split() # Takes the users input, splits each word seperated by a space and puts it into a list named 'wordList'
  stars = '*'.join(wordList) # Joins all words in the list named 'wordList' with asteriks. 
  wordCount = len(wordList) # Checks how many words are in the list named 'wordList', assigns it to variable wordCount
  
  halfCount = int(wordCount/2) # Assigns half of wordCount to halfCount
  halfWord = halfCount - 1 # Assigns the value of halfCount - 1 to halfWord
  
  firstHalf = str(wordList[0:halfCount]) # Slices wordList into the first half of words, assigns said words to a list.
  middle = str(wordList[halfWord:halfCount]) # Finds the word in the middle of the users input from wordList.
  secondHalf = str(wordList[halfCount:wordCount]) # Slices wordList into the second half of words, assigns said words to a list.

  logging.info('Tuple assignment.')
#--- Tuple Assignment
  alphabet = tuple('abcdefjhijklmnopqrstuvwxyz') # Tuple for letters in the alphabet. 
  numerals = tuple('1234567890') # Tuple for numbers 1 through - 9 + 0. 
  

  logging.info('Novelty message based upon users case sensitity.') 
  if startAsk.isupper(): # If the user's input is in all capitals the following code is executed.
    print('''Console Says: "Okay, maybe don't scream at me you potato. I'm trying to help you!"''') # Prints message imitating console.
  
  if startAsk.islower(): # If the user's input is in all lowercase letters the following code is exexecuted.
    print('''Console Says: "I could barely hear you, next time don't whisper!"''') # Prints message imitiating console.
  
  logging.info('Printing header.')
  print() # Prints blank space.
  print("Below is some information about your favourite quote: ") # Beggining header..
  print() # Prints blank space. 
  
  logging.info('Printing user input in different case level.')
  print('The quote in uppercase is: ' + startAsk.upper()) # Prints users input in all upercase.
  print('The quote in lowercase is: ' + startAsk.lower()) # Prints users input in all lowercase.
  print() # Prints blank space.
  
  logging.info('Checking if users input is alphabetic.')
  if startAsk.isalpha(): # If the users input contains letters, the following code is executed. 
    print('The quote contains characters from the alphabet. ') # Prints message stating alhabetic letters were found.
    print() # Prints blank message.
  
  ### Note: There appears to be an issue with .isalnum where regardless of whether numbers or characters are entered, it will alwayus thinks it's alphanumeric.
  ###       I have tested this issue for about 30 minutes and it appears to be an issue with spacing of the input. If you add a space before the input
  ###       it is read as if it's not alphanumeric, if you don't it will always read as if it's alphanumeric. This could be an issue with Replit's project 
  ###       mode however I'm not 100% sure. I have contacted Replit's support team about this via twitter (can provide proof and demonstation if requested).   
  
  logging.info('Checking if users input is alphanumeric.')
  if startAsk.isalnum(): # if the users input contains both numbers and letters (alphanumeric), the following code is executed.
    print('The quote is alphanumeric (contains both numbers and letters).\nHow does a quote even have a number in it? Weird...') # Prints message to user stating alphanumeric characters were found. 
    
  print() # Prints blank space.
  
  logging.info('Checking if users input is a decimal.')
  if startAsk.isdecimal(): # If the users input contains a decimal the following code is executed.
    print('The quote contains a decimal, HOW IS THAT EVEN POSSIBLE?!?!') # Prints message stating quote contains a decimal.
    print() # Prints blank space. 
  
  logging.info('Checking if users input is a space.')
  if startAsk.isspace(): # If the users input is only a space, the following code is executed.
    print('The quote is a space... Yep, just a space... Why are you like this?') # Prints message to user stating their input was simply a space. 
    print() # Prints a blank space. 
  
  logging.info('Finding first word of the users input.')  
  firstWord = wordList[0:1] # Slices the first word of the users input, assigns it to list firstWord.
  
  for item in firstWord: # For loop to print firstWord, since firstWord slices off data from a list, it too is a list and needs to use propper conventions to be printed out A.K.A the for loop.
    if startAsk.startswith(alphabet): # If the first word of the users input begins with a letter, the following code is executed.
      print('The quote starts with the word: ' + item) # Prints first word of users input.
  
  if startAsk.startswith(numerals): # If the first word of the users input begins with a number, the following code is executed.
    print('The quote starts with the number: ' + firstWord + 'How is that even possible?!?!') # Prints the first number of the users input. 
  
  logging.info('Finding the last word of the users input.')
  lastWordCalc = wordCount - 1 # Subtracts 1 from the total word count, assigns it to variable. 
  lastWord = wordList[lastWordCalc:wordCount] # Slices off data from wordList, finds last word from the users input and assigns it to a list. 
  
  for last in lastWord: # For loop to print last word of users input from list lastWord
    if startAsk.endswith(alphabet): # If the last word of the users input is a word... The following code is executed.
      print('The quote ends with the word: ' + last)
    if startAsk.endswith(numerals): # If the last word of the users input is a number (I know, sounds weird right?) the following code is executed.
      print('The last number used in your quote: ' + last + ' How is that even possible?!?!') # Prints blank space.
  
  logging.info('Printing total word count. ')
  print('The quote contains: ' + str(wordCount) +  ' words.') # Prints the total number of words the user inputted.
  print() # Prints blank space. 
  logging.info('Printing users input join with asteriks.')
  print('The quote with stars in between in it: ' + stars) # Prints out all the words the user inputted, joint with stars.
  print() # Prints blank space. 
  
  logging.info('Aligning text for outpuit of first half, middle and second half of the users input.')
  ### Note: Alignment may vary pending upon user's resolution and monitor size (DPI), as a precaution inform user to stretch their screen before running application. 
  firstHalfOutput = firstHalf.ljust(0, ' ') # Aligns the first half of the users input to be at the left side of the console using spaces. 
  middleWordOutput = middle.center(75, ' ') # Aligns the word in the middle of the users input to be in the middle of the console using spaces.
  secondHalfOutput = secondHalf.rjust(75, ' ') # Aligns the second half of the users input to the right side of the console using spaces. 
  
  logging.info('Printing first half, middle and second half of the users input.')
  print('The first half of your quote contains the words: ' + firstHalfOutput ) # Prints first half of the users input. 
  print() # Prints blank space. 
  print('The word in the middle of your quote is: ' + middleWordOutput ) # Prints the word in the middle of the users input. 
  print() # Prints blank space. 
  print('The second half of your quote contains the words: ' + secondHalfOutput) # Prints the second half of the users input. 
  print() # Prints blank space. 
  
  logging.info('Printing first half, middle and second half of the users input without alignment.')
  print("Now here's the same information about but without that fancy spacing: ") # Prints output from code above, without text alignment. 
  print() # Prints blank space. 
  print('First Half' + firstHalfOutput.rstrip(' ')) # Strips all spaces from the right side of firstHalfOutput, prints it.
  print('Second Half' + middleWordOutput.strip(' ')) # Strips all spaces from both the right and left side of firstHalfOutput, prints it. 
  print('Third Half' + secondHalf.lstrip(' ')) # Strips all spaces from the left side of firstHalfOutput, prints it. 
  logging.info('End of function.')
start() # Calls function start. 
logging.info('End of program.')

#--- End of code. 
