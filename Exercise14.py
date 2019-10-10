#------------
# Name: exercise14.py
# Purpose: To practice the use of openinig and reading files. 
#
# Creator: Haider Zaidi
# Created: 12/10/2018
# Updated: 12/10/2018 - 2:30PM
#------------

import logging # Imports logging module. 
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# Outputs all longs to file 'debug.txt'

logging.info('Start of program.')

def sqlInfo(): # Defines function sqlInfo
  '''
  Determines SQL login info. 
  
  This function reads information from numerous files using
  multiple conventions to find the login info for a SQL database. 

  Parameters
  ----------
  none
  
  Returns
  -------
  none
  '''
  
  logging.info('Start of function.')
  logging.info('Opening file sql_info.txt')
  sqlFile = open('sql_info.txt', 'r') # Opens file sql_info.txt
  
  logging.info('Reading SQL_Username.')
  sqlUser = sqlFile.readlines(1) # Reads line 1 in file sql_info.txt, assigns line data to variable.
  
  logging.info('Reading SQL_Password')
  sqlPass = sqlFile.readlines(2) # Reads line 2 in file sql_info.txt, assigns line data to variable.
  
  logging.info('Reading PORT') 
  port = sqlFile.readlines(3) # Reads line 3 in file sql_info.txt, assigns line data to variable.
  
  logging.info('Reading LOCAL')
  local = sqlFile.readlines(4) # Reads line 4 in file sql_info.txt, assigns line data to variable.
  
  logging.info('Reading SUBNET')
  subnet = sqlFile.readlines(5) # Reads line 5 in file sql_info.txt, assigns line data to variable.
  
  
  logging.info('Opening file hostname.txt')
  hostnameFile = open('hostname.txt', 'r') # Opens file hostname.txt

  logging.info('Printing SQL_USERNANME & SQL_Password.')
  for username in sqlUser: # For loop for 1st line in sql_info, username as iterator.
    for password in sqlPass: # For loop for 2nd line in sql_info, password as iterator.
      for web_port in port: # For loop for 3nd line in sql_info, web_port as iterator.
        for ip_local in local: # For loop for 4nd line in sql_info, ip_local as iterator.
          for ip_subnet in subnet: # For loop for 5nd line in sql_info, ip_subnet as iterator.
            print(username + password + web_port + ip_local + ip_subnet) # Prints iterator username, password, web_port, ip_local, ip_subnet (line 1 - 5 in file sql_info.txt)
  
  logging.info('Printing contents of file hostname.txt')    
  print(hostnameFile.read()) # Reads and then prints all lines in file hostname.txt
  
  logging.info('Closing file sql_info.txt')
  sqlFile.close() # Closes all operations in sqlFile (variable for sql_info.txt)
  logging.info('Closing file hostname.txt')
  hostnameFile.close() # Closes all operations in hostnameFile (variable for hostname.txt)
  logging.info('End of function.')
sqlInfo() # Calls function sqlInfo
logging.info('End of program.')

