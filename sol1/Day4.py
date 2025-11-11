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
images = [rock, paper, scissors]
print("Let's play Rock, Paper, Scissors!")
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if player_choice<0 or player_choice >2:
    print("Incorrect choice. Restart")
    exit(1)

if player_choice >= 0 and player_choice <=2:
    print(images[player_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose:\n{computer_choice}")
print(images[computer_choice])

if player_choice == computer_choice:
    print("It's a draw! Try Again")
elif player_choice == 0 and computer_choice == 1:
    print("Uh-Oh! Looks like you lose!")
elif player_choice == 1 and computer_choice == 2:
    print("Uh-Oh! Looks like you lose!")
elif player_choice == 2 and computer_choice == 0:
    print("Uh-Oh! Looks like you lose!")
else:
    print("Yay! Good job! You win")
