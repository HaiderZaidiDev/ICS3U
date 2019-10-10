#-------
# Name: Exercise6.py
# Purpose: To practice using functions with Python.
#
# Author: Haider Zaidi
# Created: 10/19/2018
# Updated: 10/26/2018 - 4:37PM
#-------

#---- Celcius -> Farenheight
def convertCToF(temperature): # Defines the function CToF
  ''' Converts the inputted celcius to farenheight.
  '''
  if temperature <= -100 or temperature >= 100: # If the statement is true the following code will execute.
   return("Unacceptable input values.") # Sends the user a message.
  else: # If the code above is false, the following code executes:
    farenheight = (temperature * 9/5) + 32 # Equation to convert celcius to farenheight.
    return farenheight # Returns function.

c = convertCToF(-5) # Calls function, inputs the value of -5.
print(int(c)) # Prints the function as an integer.

#---- Farenheight -> Celcius

def convertFToC(temperature): # Defines function convertFToC
  ''' Converts the inputted farenheight to celcius. 
  '''
  if temperature <= -100 or temperature >= 100: # If the statement is true the following code will execute.
    return("Unacceptable input values.") # Sends the user a message.
  else: # If the code above is false, the following code executes.
    celcius = (temperature - 32)*5/9 # Equation to convert farenheight to celcius.
    return celcius # Returns function.
  
f = convertFToC(-5) # Calls function, inputs value of -5.
print(int(f)) # Prints function as an integer.

#---- Hypotneuse
def hypotenuse(a, b): # Defines function hypotenuse.
  '''Calculates the hypotenuse based upon the values inputted by the user and prints it.

  '''
  if a < 1 or b < 1: # If the statement is true, the following code is executed.
    return("Unacceptable input values.") # Sends the user a message.
  else: # If the code above is false, the following code will execute.
   cSquare = a**2 + b**2	  # Equation for pythagorean theorem. 
   cLength = cSquare**0.5 	# Calculates the square root of cSquared to determine the length of C.
   return cLength # Returns function

# Program runs starting here.  Above this line, the functions are just defined.
missingSide = hypotenuse(1, 2) # Calls fucntion.
print(float(missingSide)) # Prints function as a float. 

#---- convertCToFEveryFive
def convertCToFEveryFive(lowC, highC): # Defines function convertCToFEveryFive
  '''
  Calculates the farenheight based upon the number outputted by the for loop. 
  
  '''
  if lowC > highC: # If the statement is true, the following code is executed.
    return("Unacceptable input values.") # Sends a message to the user.
  else: # If the statement above is false, the following code is executed.
    for convertTemp in range(lowC, highC, 5): # For loop for printing farenheight conversions.
      print(str(convertTemp) + "C = " + str(convertCToF(convertTemp)) + "F") # Counts-up numbers in intervals of 5. Takes the numbers and converts it to farenheight.

convertCToFEveryFive(-10,20 + 1) # Calls function convertCToFEveryFive, adds 1 to highC (This is done so the conversion for 20c shows.)
