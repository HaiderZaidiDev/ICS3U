#-----------------------------------------------------------------------------
# Name:        Pre-Exam Question
# Purpose:     To complete a pre-exam question for ICS3U.
#
# Author:      Haider Zaidi
# Created:     1/22/2019
# Updated:     1/22/2019 - 2:40PM
#-----------------------------------------------------------------------------

import logging # Imports logging library.
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') # Logs logging related information to file log.txt

logging.info('Start of program.')
def volume_of_cone(radius, height): # Defines function volume_of_cone with parameters radius and height.
  '''
  Calculate the volume of a cone.
  
  This function calculatues the volume of a cone given the radius and height using
  the formulas for the area and volume of a circle.

  Parameters
  ----------
  radius : float
    The radius of the base of the cone.
  height : float
    The vertical height of the cone.
  
  Returns
  -------
  float
    The volume of the cone with the radius and height provided.
  
  Warnings 
  --------
  The assertion near of the bottom of the code will result in the function being logged again. 


  Raises 
  ------
  TypeError
    When the parameters for radius or height or not an integer or a string.
  '''
  
  logging.info('Starting function volume_of_cone.')
  
  logging.debug('Ensuring parameters of radius and height are either an integer or float.')
  if not isinstance(radius, (int, float)): # If the radius is not an integer or float the following code is executed.
    raise TypeError('Expecting radius to be integer or float!') # Raises a type error if the radius is not an integer or float.
  
  if not isinstance(height, (int, float)): # If the height is not an integer or a float the following code is executed.
    raise TypeError('Expecting height integer or float!') # Raises a type error if the radius is not an integer or float.
  
  logging.debug('Parameters of radius and height are not strings.')
  
  pi = 3.141592654 # Assigns variable pi with a shortened version of the mathetmical equation pi. 
  area_of_circle = pi * radius * radius # Calculates the formula of the base of the cone (the circle).
  logging.debug('The area of the circle is: ' + str(area_of_circle))
  volume = area_of_circle * height / 3.0 # Cakcykates the volume of the cone. 
  logging.debug('The volume of the circle is: '  + str(volume))
  logging.info('End of function volume_of_cone') 
  return volume # Returns the volume of the cone to the function.

# Start of program here

assert volume_of_cone(5,5) == 130.89969391666668, 'Expecting cone with radius 5 and height 5 to have volume of 130.89969391666668' # Ensures that the function volume_of_cone is working correctly.

try: # The program will try to execute the following code. 
  print(volume_of_cone(5,5)) # Calls the function volume_of_cone with radius 5, height 5 and prints the return result. 
  
except TypeError as e: # If an TypeError occurs while the code under 'try:' is executed, the following code is executed (catches errors).
  print('Oops! Looks like something went wrong: {}'.format(e)) # Prints an error message to the user, containing the error.

logging.info('End of program.')
