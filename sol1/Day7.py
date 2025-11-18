import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
with open("word_list.txt") as fd:
    word_list = [w.strip() for w in fd.readlines()]

chosen_word = random.choice(word_list)
#print(chosen_word)


placeholder = []
for i in range(len(chosen_word)):
    placeholder.append("_")
print ("".join(placeholder))
display = placeholder[:]
count = 0
lives = 6
while count < len(chosen_word) and lives >0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed the {guess}")

    life_lost = True
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            count +=1
            life_lost = False

    if life_lost:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life!")


    print("".join(display))
    print(f"Lives remaining: {lives}")
    print(stages[lives])
if lives == 0:
    print(f"Word was {chosen_word}. You lose! Try again.")
else:
    print("You win!")

