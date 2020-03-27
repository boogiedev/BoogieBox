#time function to add suspense to story instead of all text printing in one block
import time
#sys function to print statements that are also buffered
import sys
#import os for clearing screen
from os import system, name

#function to delay printing letters to give the story a more natural and involving read
#there were multiple ways to do this using a forloop for each string but this one that i looked up was the smoothest running
def delay_print(s, long):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(long)

# system clear screen
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")
