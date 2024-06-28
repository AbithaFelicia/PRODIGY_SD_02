import random

def guess_the_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have generated a random number between 1 and 100. Can you guess it?")

    while True:
        # Prompt the user to enter their guess
        user_guess = input("Enter your guess: ")

        # Check if the input is a valid number
        if not user_guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        # Convert the input to an integer
        user_guess = int(user_guess)
        attempts += 1

        # Compare the user's guess with the generated number
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Call the function to start the game
guess_the_number()
