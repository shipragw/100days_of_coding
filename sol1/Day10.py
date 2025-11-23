logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def get_input(prompt, valid_values):
    value = input(prompt)
    while value not in valid_values:
        print("Invalid input!")
        value = input(prompt)
    return value

def calculator():
    continue_calculating = True
    n1 = float(input("What's the first number?: "))
    while continue_calculating:
        for symbol in calculations:
            print(symbol)
        operation = get_input("Pick an operation: ", set(calculations.keys()))
        n2 = float(input("What's the next number?: "))
        value = calculations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {value}")
        more_calculation = get_input(f"Type 'y' if you want to continue calculating with {value}. Else type 'n' to start a new calculation:\n", {"y", "n"} )
        if more_calculation == "y":
            n1 = value
        else:
            continue_calculating = False
            print("\n" * 50)
            calculator()

calculator()



