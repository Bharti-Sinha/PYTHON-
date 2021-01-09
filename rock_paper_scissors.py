rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("I created this Rock Paper Scissors game. Lets play against the computer!\n")
user_in = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "))

if user_in == 0:
  print ("You choose Rock")
  print(rock)
elif user_in == 1:
  print ("You choose Paper")
  print(paper)
elif user_in == 2:
  print ("You choose Scissors")
  print(scissors)

computer_choice = random.randint(0,2)
if computer_choice == 0:
  print ("Computer choose Rock")
  print(rock)
elif computer_choice == 1:
  print ("Computer choose Paper")
  print(paper)
elif computer_choice == 2:
  print ("Computer choose Scissors")
  print(scissors)


posibilities = [["draw", "You lose.", "You win!"],
["You win!" , "draw", "You lose."],
["You lose.", "You win!","draw"]]


print (posibilities[user_in][computer_choice])
