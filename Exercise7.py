#-------
# Name: Exercise7.py
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
  if temperature <= -100 or temperature >= 100: # If temperature is less then or equal to -100, or greater then or equal to 100, the following code is executed.
   return("Unacceptable input values.") # Returns the user a message.
  else: # If the temperature is between -100 and 100 the following code is executed.
    farenheight = (temperature * 9/5) + 32 # Equation to convert celcius to farenheight.
    return farenheight # Returns function.

c = convertCToF(-5) # Calls function, inputs the value of -5.
print(int(c)) # Prints the function as an integer.

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
  
  '''
  if temperature <= -100 or temperature >= 100: # If temperature is less then or equal to -100, or greater then or equal to 100, the following code is executed.
    return("Unacceptable input values.") # Returns an error message to the user.
  else: # If the temperature is between -100 and 100 the following code is executed.
    celcius = (temperature - 32)*5/9 # Equation to convert farenheight to celcius.
    return celcius # Returns function.
  
f = convertFToC(-5) # Calls function, inputs value of -5.
print(int(f)) # Prints function as an integer.

#---- Hypotneuse
def hypotenuse(a, b): # Defines function hypotenuse.
  '''
  Determines the length of a triangles hypotenuse.
  
  The function determines the length of a triangle's hypotneuse using the pythagorean theorem
  and prints it.
  
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
  

  '''
  if a < 1 or b < 1: # If the parameters a or b is less than one the following code is executed.
    return("Unacceptable input values.") # Returns an error message to the user.
  else: # If the paramters a or b are greater then or equal to 1 the following code is executed.
   cSquare = a**2 + b**2	  # Equation to calculate the hypotneuse, based upon the Pythagorean Theroem 
   cLength = cSquare**0.5 	# Calculates the square root of cSquare to determine the length of C.
   return cLength # Returns function

# Program runs starting here.  Above this line, the functions are just defined.
missingSide = hypotenuse(1, 2) # Calls fucntion with the paramters 1 and 2 in replacement of a and b respectively. 
print(float(missingSide)) # Prints function as a float. 

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
  Warnings 
  --------
  If you use return instead of print for the if statement in the function below, no error message will be outputted.
  '''
  if lowC > highC: # if the paramter lowC is greater then highC the following code is executed.
    print("Unacceptable input values.") # Returns an error message to the user.
  else: # If lowC is less than highC the following code is executed.
    for convertTemp in range(lowC, highC, 5): # For loop for printing farenheight conversions.
      print(str(convertTemp) + "C = " + str(convertCToF(convertTemp)) + "F") # Counts-up numbers in intervals of 5. Takes the numbers and converts it to farenheight.
convertCToFEveryFive(-10,20 + 1) # Calls function convertCToFEveryFive, adds 1 to highC (This is done so the conversion for 20c shows.)

#--- End of Code.

# Note: Made an ammendment on 10/30/2018 to fix file name and add warning statement to final function.
