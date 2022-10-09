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

#Write your code below this line 👇
import random

hands = [rock, paper, scissors]
user_choice = int(input("What do you chose?  Type 0 for Rock, 1 for Paper, and 2 for Scissors"))

print(hands[user_choice])

print("Computer chose:")

computer_choice = random.randint(0,len(hands)-1)
print(hands[computer_choice])

#Winners

#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.

if user_choice == computer_choice:
  print("It's a Draw!!")
elif user_choice == 0 and computer_choice == 2:
  print("You Win!")
elif user_choice == 2 and computer_choice == 1:
  print("You Win!")
elif user_choice == 1 and computer_choice == 0:
  print("You Win!")
else:
  print("You Lose!")