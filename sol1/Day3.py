print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
path = input("Will you like to go left or right?").lower()
if path == "left":
    option = input("You have arrived on a bank of a lake. Will you like to 'swim' or 'wait'?").lower()
    if option == "wait":
        print("Great choice, your boat is on it's way!")
        door = input("Now that you landed on the other side, choose from one of the doors you see in front of you: red, blue or yellow?").lower()
        if door == "red":
            print("Sorry, you got caught in a fire and could not find the treasure.")
        elif door == "blue":
            print("Sorry, you have been caught by the wild boar and could not find the treasure.")
        elif door == "yellow":
            print("Congratulations! You are rich!")
        else:
            print("Sorry, you are lost without food and water and will die soon")
    elif option == "swim":
        print("Sorry swimming was not a great idea, looks like lake is full of hungry crocodiles. You wont' make it.")
    else:
        print("Sorry, you are lost without food and water and will die soon.")
else:
    print("Sorry looks like you fell in a crater and won't make out of it.")
