
#time function to add suspense to story instead of all text printing in one block
import time
#sys function to print statements that are also buffered
import sys
#import os for clearing screen
from os import system, name

class Visuals:

  def delay_print(self, s:str="", long:float=0.02):
    """Prints characters in a string with slight delay to simulate a live program"""
    for c in s:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(long)

  # system clear screen
  def clear(self):
    """Clears terminal to empty"""
    if name == "nt":
      _ = system("cls")
    else:
      _ = system("clear")
