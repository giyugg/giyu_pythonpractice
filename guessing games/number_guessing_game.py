import random

def get_ordinal(n):
    if 11 <= n % 100 <= 13:  # Special case for 11th, 12th, and 13th
        return f"{n}th"
    else:
        last_digit = n % 10
        if last_digit == 1:
            return f"{n}st"
        elif last_digit == 2:
            return f"{n}nd"
        elif last_digit == 3:
            return f"{n}rd"
        else:
            return f"{n}th"

print("Hi, welcome to the game. This is a number guessing game FROM 1 TO 10.\nYou got 7 chances to guess the number. Let's start the game!")

number_to_guess = random.randrange(10)
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input('What is your guess?'))

    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and you found it right!! In the {get_ordinal(guess_counter)} attempt!')
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Oops! Sorry. The number is {number_to_guess}. Better luck next time!')
    elif my_guess > number_to_guess:
        print('Your guess is too much!')
    elif my_guess < number_to_guess:
        print('Your guess is too less!')