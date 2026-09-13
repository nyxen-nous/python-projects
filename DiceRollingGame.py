import random 

while True:
    roll = input("Roll the dice🎲 (y/n): ")
    if roll.lower() == 'y':
        dice_roll = random.randint(1,6)
        print(f"you rolled a 🎲{dice_roll}")
    elif roll.lower() == 'n':
        print("You chose not to roll the dice🎲.")
        break
    else: print("Invalid input. Please enter 'y' to roll or 'n' to quit.")
