import random
def number_guessing_game():
    print("welcome to the Number Guessing game....")
    target_number = random.randint(1,100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number!")

number_guessing_game()