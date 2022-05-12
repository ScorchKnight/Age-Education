import random
from unicodedata import name

def welcome():
  print(
    """> Welcome to the Age Education"""
  )
  name = input("> Please type your first name only: ").capitalize()
  if name.isalpha() == True:
    print("> Hello " + name + "! Today you will play a game that lets you experience what people of other generation thinks of you. Through this game, we hope to give you some knowledge about people of different generation and their thoughts about you.")
  else:
    print("Please enter your name in letters only")
    print("Restart the code and try again")
welcome()

