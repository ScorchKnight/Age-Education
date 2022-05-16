from ast import While
import random

def welcome():
  print(
    """
    > Welcome to the Age Education"""
  )
  name = input("> Please type your name: ").capitalize()
  if name.isalpha() == True:
    print(f" Hello {name} , This game sends you into an experience based on your age. Young people will be placed into the past playing through a teenage experience from the past shining a light on why older people are the way they are and think the way they do. Older people will be placed into a young person\'s experience of the world today. With all of our resources and difficulties we face to clarify why younger people are the way they are and think the way they do.we hope to give you some knowledge about people of other generation and their thoughts about you.")
  else:
    print("Please enter your name in letters only")
    print("Restart the code and try again")
welcome()



def ageEd():
  age = int(input("Enter your age:"))
  if age > 35:
    print("The year is 2018. You are in your juinor year of High School, and live a pretty average lifestyle, have an active social life and ")




  else: 
    print()
  
  

ageEd()