#
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today's date is ", today)
  
  # print out the date's individual components
  print("Date Components: " ,today.day,today.month,today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday # is ", today.weekday() )
  days = ["mon","tue","wed","thu","fri","sat","sun"]
  print("Which is a: ", days[today.weekday()])

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("The current date and time is ", today)

  # Get the current time
  t = datetime.time(datetime.now())
  print(t)

  # Times and dates can be formatted using a set of predefined string
  # control codes 

  now = datetime.now()

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("%a, %d, %B , %y"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Locale date and time:  %c"))
  print(now.strftime("Locale date :  %x"))
  print(now.strftime("Locale time:  %X"))

  #### Time Formatting ####
  print(now.strftime("Current time : %I:%M:%S %p"))
  print(now.strftime("24-hour time : %H:%M "))

  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM

  
if __name__ == "__main__":
  main();
  