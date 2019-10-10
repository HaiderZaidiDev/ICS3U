#-------
# Name: Exercise8.py
# Purpose: To practice using functions with Python.
#
# Author: Haider Zaidi
# Created: 10/19/2018
# Updated: 10/26/2018 - 4:37PM
#-------

#---- Celcius -> Farenheight
def convertCToF(temperature): # Defines the function convertCToF
  ''' 
  Converts celcius degrees to farenheight. 
  
  The function takes the celcius value inputted by the user, converts it to farenheight and outputs it. 

  Parameters
  ----------
  temperature : integer
    The celcius value inputted by the user. 
  
  Returns
  -------
  integer
    The farenheight value. 
  
  Warnings 
  --------
  None
  '''
  if temperature <= -100 or temperature >= 100: # If the statement is true the following code will execute.
   return("Unacceptable input values.") # Sends the user a message.
  else: # If the code above is false, the following code executes:
    farenheight = (temperature * 9/5) + 32 # Equation to convert celcius to farenheight.
    return farenheight # Returns function.

c = int(convertCToF(5)) # Calls function, inputs the value of -5.
print(c) # Prints the function as an integer.
#assert isinstance(c, int), 'Expecting integer.' 



#---- Farenheight -> Celcius

def convertFToC(temperature): # Defines function convertFToC
  '''
  Converts farenheight to celcius degrees.
  
  The function takes the farenheight value inputted by the user, converts it to celcius and outputs it. 

  Parameters
  ----------
  temperature : integer
    The farenheight value inputted by the user. 
  
  Returns
  -------
  integer
    The celcius value. 
  
  Warnings 
  --------
  None
  '''
  if temperature <= -100 or temperature >= 100: # If the statement is true the following code will execute.
    return("Unacceptable input values.") # Sends the user a message.
  else: # If the code above is false, the following code executes.
    celcius = (temperature - 32)*5/9 # Equation to convert farenheight to celcius.
    return celcius # Returns function.
  
f = int(convertFToC(-5)) # Calls function, inputs value of -5.
print(f) # Prints function as an integer.
#assert isinstance(f, int), 'Expecting integer.'

#---- Hypotneuse
def hypotenuse(a, b): # Defines function hypotenuse.
  '''
  Determines the length of a triangles hypotenuse.
  
  The function determines the length of a triangle's hypotneuse using the pythagorean theorem. 
  Parameters
  ----------
  a : float
      The length of one of the sides on the triangle. 
  b: float
      The length of the other side of the triangle. 
  
  Returns
  -------
  float
      The length of the hypotenuse.  
  
  Warnings 
  --------
  None  

  '''
  if a < 1 or b < 1: # If the statement is true, the following code is executed.
    return("Unacceptable input values.") # Sends the user a message.
  else: # If the code above is false, the following code will execute.
   cSquare = a**2 + b**2	  # Equation for pythagorean theorem. 
   cLength = cSquare**0.5 	# Calculates the square root of cSquared to determine the length of C.
   return cLength # Returns function

# Program runs starting here.  Above this line, the functions are just defined.
missingSide = float(hypotenuse(1,2)) # Calls fucntion.
print(missingSide) # Prints function as a float. 
#assert isinstance(missingSide, float), 'Expecting float.'

#---- convertCToFEveryFive
def convertCToFEveryFive(lowC, highC): # Defines function convertCToFEveryFive
  '''
  Converts celcius values to farenheight values in intervals of 5. 
  
  The function uses a for loop to determine integer values for celcius, in intervals of 5 (This can be edited)
  the values determined are then converted to farenheight and is printed as an integer. 
  ----------
  lowC : integer
      The lowest celcius temperature possible (starting point of for loop). 
  highC: float
      The highest celcius temperature possible (ending point of for loop). 
  
  Returns
  --------
  None
  
  Warnings 
  --------
  If you use return in the place of prnit in the if statement below the function will not output an error message.
  '''
  if lowC > highC: # If the statement is true, the following code is executed.
     return("Unacceptable input values.")
     #assert lowC > highC, 'Unacceptable, lowC must be greater than highC.'
  else: # If the statement above is false, the following code is executed.
    for convertTemp in range(lowC, highC, 5): # For loop for printing farenheight conversions.
      print(int(convertTemp) + "C = " + int(convertCToF(convertTemp)) + "F") # Counts-up numbers in intervals of 5. Takes the numbers and converts it to farenheight.

convertCToFEveryFive(-10,20 + 1) # Calls function convertCToFEveryFive, adds 1 to highC (This is done so the conversion for 20c shows.)
#--- End of Code.
