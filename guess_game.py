import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 10

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.\n")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed the number {secret_number} correctly!")
                break
            elif guess < secret_number:
                print("🔻 Too low!")
            else:
                print("🔺 Too high!")

            attempts -= 1
            print(f"Attempts left: {attempts}\n")

        except ValueError:
            print("❗ Invalid input. Please enter a number.\n")

    if attempts == 0:
        print(f"😞 Game Over! The number was {secret_number}.")

# Start the game
number_guessing_game()
