import random
logo = r"""
,  , , ,  _  ___,'_,    ___, ,  _,   ,  , ,  , , ,  __   _,,_   
| ,| |_|,'|\' |  (_,   ' | |_|,/_,   |\ | |  ||\/| '|_) /_,|_)  
|/\|'| |  |-\ |   _)     |'| |'\_    |'\|'\__|| `| _|_)'\_'| \  
'  ` ' `  '  `'  '       ' ' `   `   '  `    `'  `'       `'  ` 
                                                                                                                            
"""
def str_converter_fn(input_str):
    return input_str.lower()

def get_input(prompt, valid_values, converter_fn):
    value = converter_fn(input(prompt))
    while value not in valid_values:
        print("Invalid input!")
        value = converter_fn(input(prompt))
    return value

Easy = 10
Hard = 5

def difficulty_level():
    choice = get_input("Choose the difficulty level: 'Easy' or 'Hard': ", {"easy", "hard"}, str_converter_fn)
    if choice == "easy":
        return Easy
    if choice == "hard":
        return Hard

def check(player_choice, comp_choice, attempts):
    if player_choice > comp_choice:
        print("Too high!")
        return attempts - 1
    elif player_choice < comp_choice:
        print("Too low!")
        return attempts -1
    else:
        print(f"You got it! The answer was: {comp_choice}")

def game():
    print(logo)
    print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100.")
    computer_choice = random.randint(1, 100)

    attempts = difficulty_level()
    guess = 0

    while guess != computer_choice:

        print(f"You have {attempts} attempts to guess the number")
        guess = get_input("Make a guess: ", set(range(1, 101)), int)
        attempts = check(guess, computer_choice, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was: {computer_choice}")
            return
        elif guess != computer_choice:
            print("Guess again.")


game()
