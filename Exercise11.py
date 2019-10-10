#------------
# Name: exercise11.py
# Purpose: To practice using and logging exceptions in python.
#
# Author: Haider Zaidi
# Created: 11/22/2018
# Updated:
#------------

#NOTE: I COMPLETED THIS EXERCISE BEFORE THE DUE DATE, FORGOT TO CLICK SUBMIT

import urllib.request # Imports urllib.request module, allows for reading of web pages.
from termcolor import cprint # Imports cprint from module termcolor, used for printing blinking text.
from colorama import Fore, Style # Imports Fore and Style from Colorama, allows for coloured and styled text.
import time # Imports time module, used for delaying prints.
import replit # Imports replit module, used for clearing console.

import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info('Program launch.')

location = [] # Creates empty list named location.

launchScreen = '''
  _____ _____    _                     _             
 |_   _|  __ \  | |                   | |            
   | | | |__) | | |     ___   ___ __ _| |_ ___  _ __ 
   | | |  ___/  | |    / _ \ / __/ _` | __/ _ \| '__|
  _| |_| |      | |___| (_) | (_| (_| | || (_) | |   
 |_____|_|      |______\___/ \___\__,_|\__\___/|_|   
                                                     
                                                     
                                                     '''
# Assigns ASCII Art to variable. 
logging.info('Printing launchScreen.')
print(launchScreen) # Prints launchScreen.


logging.info('Starting function ipAddress')
def ipAddress(ip): # Defines function ipAdddress.

  '''
  Determins geo-location of an IP Address.
  
  This function will determine the geo-location (Country, Province/State, City, Postal Code) of an ip address
  by using an ip-api website, the function will read data from the function api-website and output it to the user.
  
  Parameters
  ----------
  ip: string
    IP Address provided by user input.

  Returns
  -------
  none
  
  Raises
  -------
  ValueError
    If the ip parameter is more then 12 characters, the maximum length of an ip address (excluding IPv6), an exception is raised.
    
  '''
  print() # Prints blank message.
  
  logging.info('Ensuring ip address inputted is less than 12 characters.')
  logging.info('IP Address given is ' + ip + ' and has ' + str(len(ip)) + ' characters.')
  
  if len(ip) > 12:
    raise ValueError('Unexpected input, invalid IP address length. ') # Raises a value error.
  

  
  else:
    logging.info('Printing blinking header.')
    
    print() # Prints a blank message.
    cprint('Determining IP Location...', attrs=['blink']) # Prints heading message, blinks.
    time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
    print() # Prints blank message.
    
    logging.info('Determing location of IP Address.')
    
    try: # Program attempts to run the following code.
      for ipCountry in urllib.request.urlopen('https://ipinfo.io/' + ip + '/country'): # Reads the page source of the url, grabs the country the user resides in based upon their IP Address.
        
        logging.info('Fetching country of ip address.')
        ipCountryOutput = ipCountry.decode('utf-8') # Decodes the country name to avoid unwanted prefixes.
        ipCountryList = ipCountryOutput.replace('\n', '') # Removes \n suffix from ipCountryOutput.
        
        logging.info('Adding the country of the ip address to a list.')
        location.append(ipCountryList) # Places ipCountryList in the list named 'location'
      
      for ipCity in urllib.request.urlopen('https://ipinfo.io/' + ip + '/city'): # Reads the page source of the url, grabs the city the user resides in based upon their IP Address.
        logging.info('Fetching city of ip address.')
        ipCityOutput = ipCity.decode('utf-8') # Decodes the city name to avoid unwanted prefixes.
        ipCityList = ipCityOutput.replace('\n', '') # Removes \n suffix from ipCityOutput.
        
        logging.info('Adding the city of the ip address to a list.')
        location.append(ipCityList) # Places ipCityList in the list named 'location'
      
      for ipRegion in urllib.request.urlopen('https://ipinfo.io/' + ip + '/region'): # Reads the page source of the url, grabs the region the user resides in based upon their IP Address.
        
        logging.info('Fetching the region of the ip address.')
        ipRegionOutput = ipRegion.decode('utf-8') # Decodes the region name to avoid unwanted prefixes.
        ipRegionList = ipRegionOutput.replace('\n', '') # Removes \n suffix from ipRegionOutput.
        
        logging.info('Adding the region of the ip address to a list.')
        location.append(ipRegionList)# Places ipRegionList in the list named 'location'
      
      for ipPostal in urllib.request.urlopen('https://ipinfo.io/' + ip + '/postal'): # Reads the page source of the url, grabs the postal code the user resides in based upon their IP Address.
      
        logging.info('Fetching the postal code of the ip address.')
        ipPostalOutput = ipPostal.decode('utf-8') # Decodes the postal code to avoid unwanted prefixes.
        ipPostalList = ipPostalOutput.replace('\n', '') # Removes \n suffix from ipPostalOutput.
        
        logging.info('Adding the postal code of the ip address to a list.')
        location.append(ipPostalList) # Places ipPostalList in the list named 'location'
      
      logging.info('Printing location info of the ip address.')  
      for address in location: # For loop for data in list 'location'
        print(address, end=', ') # Prints data in list 'location'
        
      logging.info('Ensuring no errors were given while Fetching location of ip address.')
      
    except urllib.error.HTTPError: # If the code under 'try:' provides the error 'urllib.error.HTTPError' the following code is executed:
    
      logging.info('Printing error message.')
      print(Fore.RED + 'Error: ' + Style.RESET_ALL + 'Oh no! Something went wrong, looks line an invalid IP Address was given. Restarting application.') # Prints error message.
      
      logging.info('Clearing console, restarting function.')
      time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
      replit.clear() # Clears console.
      print() # Prints blank message.
      print(launchScreen) # Prints launchScreen.
      ipAddress(input('What is your IP Address?: ')) # Calls function ipAddress.
  
  logging.info('End of function.')
    
ipAddress(input('What is your IP Address?: ')) # Prompts user to enter IP Address.) # Calls function ipAddress with parameter 'ip' as input.

logging.info('End of program.')
#--- END OF CODE
