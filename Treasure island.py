print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
#my first cool game ever

first = (input("You are at a crossroad. Where do you want to go? Type 'left' or 'right' ")).lower()
if first == "left":
  second = (input("You\'ve come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat or 'swim' to swim acorss")).lower()
  if second  == "wait":
    third = (input("You arrive at the island unharmed. There is a house with three doors. One yellow, one blue and one red. Which one do you choose?")).lower()
    if third == "Yellow":
      print("You win!!")
    elif third == "blue":
      print("You are eaten by Beasts. Game Over")
    elif third == "red":
      print("You are Burned by fire. Game Over")
    else:
      print("There is no such door. I am not a fool, you lose. Game Over.")

  else:
    print("You are attacked by trout. You die. Game Over")

else:
  print("You fall into a hole. Game Over")




