from ast import While
import random

def welcome():
  print(
    """sa> Welcome to the Age Education"""
  )
  name = input("> Please type your name: ").capitalize()
  if name.isalpha() == True:
    print(f" Hello {name}, this game sends you into an experience based on your age. Young people will be placed into the past playing through a teenage experience from the past shining a light on why older people are the way they are and think the way they do. Older people will be placed into a young person\'s experience of the world today. With all of our resources and difficulties, we face to clarify why younger people are the way they are and think the way they do.we hope to give you some knowledge about people of other generation and their thoughts about you.")
  else:
    print("Please enter your name in letters only")
    print("Restart the code and try again")
welcome()

young = False
old = False
ans_yes = ["Yes", "Y", "yes", "y"]
ans_no = ["No", "N", "no", "n"]
age = int(input("Enter your age: "))
if age > 35:
  old = True
else: 
  print()
young = True
  
while old is True:
  old_resp = input("The year is 2018. You are in your juinor year of High School, and live a pretty average lifestyle with an active social life.\n- 5:30 -\nYou wake up contemplating your life. What\'s the use of school again? You try to think of what\'s more important: high school, or your sanity. Will you actually get out of bed and prepare yourself for school? (Yes/No)\n: ")
  if old_resp in ans_yes:
    print("You go through your morning routine and set up your music and get out the house to get to school. Your music clears your mind and allows you to focus on both it and the task at hand, travel. You arrive to school on time.\nYou cruise through classes, checking your phone a few times until gym rolls around. Most of your peers are on their phones except some playing sports and others working out")

  if old_resp in ans_no:
    continue
  break


while young is True:
  young_resp = input("blank_input_temp")

  if young_resp in ans_yes:
    continue

  if young_resp in ans_no:
    continue
  break