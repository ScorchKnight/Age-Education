<<<<<<< HEAD
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
=======
import random
from unicodedata import name

def welcome():
  print(
    """> Welcome to the Age Education"""
  )
  name = input("> Please type your first name only: ").capitalize()
  if name.isalpha() == True:
    print("> Hello " + name + "! Today you will play a game that lets you experience what people of other generation thinks of you. Through this game, we hope to give you some knowledge about people of different generation and their thoughts about you.")
>>>>>>> a99446e0867e760e2e920768669f8ebdbc407b19
  else:
    print("Please enter your name in letters only")
    print("Restart the code and try again")
welcome()

<<<<<<< HEAD
young = False
old = False
ans_yes = ["Yes", "Y", "yes", "y"]
ans_no = ["No", "N", "no", "n"]
age = int(input("Enter your age:"))
if age > 35:
  old = True
else: 
  print()
young = True
  
while old is True:
 resp1 = input("The year is 2018. You are in your juinor year of High School, and live a pretty average lifestyle with an active social life.\n5:30\nYou wake up contemplating your life. What\'s the use of school again? you try to think of what\'s more important: high school, or your sanity. Will you actually get out of bed and prepare yourself for school?? (Yes/No)\n: ")
  if resp1 in ans_yes:
    print("You go through your morning routine and set up your music and get out the house to get to school. Your music clears your mind and allows you to focus on both it and the task at hand, travel.You arrive to school on time.\n You cruise through classes checking your phone a few times until gym rolls around. Most of your peers are on there phones except some playing sports and others working out")
=======
>>>>>>> a99446e0867e760e2e920768669f8ebdbc407b19
