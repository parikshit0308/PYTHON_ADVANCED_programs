import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = int(input("Enter the length of the Code: "))

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    
    return code

def guess_code():
    while True:
        guess = input("Guess the Color: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"Please enter {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try Again")
                break
        else:
            break

    return guess    

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Colors_Match! You have {TRIES} to guess the color code.")
    print("Colors Available: ", *COLORS)
    print("-------------------------------------------------------------------")

    code  = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You Guessed the code in {attempts} Tries!!")
            break

        print(f"Correct_Positions: {correct_pos} | Incorrect_Positions: {incorrect_pos}")    
        print("------------------------------------------------------------------------") 

    else:
        print("Sorry, You couldn't guess the code in 10 tries, The code Was: ", *code)

if __name__ == "__main__":
    game()