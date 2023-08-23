import random


def guess(x):
    """
    Allows user to guess a number based on a random integer chosen by the program and see if the user can guess the
    random number chosen by the program.
    :param x: user input integer
    :return: None
    """
    guess = 0
    valid_responses = ["yes", "no"]
    negative_numbers = input("Would you like to use negative numbers? (Please enter 'Yes' or 'No'): ").lower()

    while negative_numbers not in valid_responses:
        negative_numbers = input('Please either choose "Yes" or "No": ').lower()

    if negative_numbers == "no":
        random_number = random.randint(1, x)
        range_text = f'between 1 and {x}'
    else:
        random_number = random.randint(-x, x)
        range_text = f'between {-x} and {x}'

    while guess != random_number:
        guess = int(input(f'Guess a number {range_text}: '))
        if guess < -x or guess > x:
            print("Error: Number not in range")
        elif guess < random_number:
            print("Try again, a little higher this time")
        elif guess > random_number:
            print("Try again, a little lower this time")
        else:
            print(f"Yay!, you found the number. The correct number was: {guess}")


def main():
    user_input_for_x = int(input("Please pick a number, any number: "))
    guess(user_input_for_x)


main()
