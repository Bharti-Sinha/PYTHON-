# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

full_name = (name1 + name2).lower()

first_digit = full_name.count("t") + full_name.count("r") + full_name.count("u")+ full_name.count("e")

second_digit = full_name.count("l") + full_name.count("o")
+ full_name.count("v") + full_name.count("e")

per = int(str(first_digit) + str(second_digit))

if per < 10 or per > 90:
  print(f"Your score is {per}, you go together like coke and mentos.")
elif per >= 40 and per <= 50:
  print(f"Your score is {per}, you are alright together.")
else:
  print(f"Your score is {per}.")