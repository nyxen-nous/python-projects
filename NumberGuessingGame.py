import random

number_guess = random.randint(1,100)

while True:
    guess = input("Guess a number between 1 and 100 (q to quit): ")
    if guess.lower() =='q':
        print("Thanks for playing!")
        break
    else:
        try:
            guess = int(guess)
            if guess == number_guess:
                print("Congratulations! You guessed the correct number!")
                break
            elif guess < number_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")