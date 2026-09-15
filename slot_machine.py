import random

def starting_balance():
    while True:
        try:
            balance = int(input("Enter your starting balance: ₹"))
            if balance <= 0:
                print("Your balance must be greater than zero. Please try again.")
            else:
                return balance
        except ValueError:
            print("❌Invalid input")

def bet_amount(balance):
    while True:
        try:
            bet = int(input("Enter your bet amount: ₹"))
            if bet <= 0:
                print("Your bet must be greater than zero. Please try again.")
            elif bet > balance:
                print(f"Your bet cannot exceed your balance{balance}₹.")
            else:
                return bet
        except ValueError:
            print("❌Invalid input. ")

def spin_reels():
            symbols = ['🍒','🍉','🍇','🍓','🥝']
            return [random.choice(symbols) for _ in range(3)]

def display_reels(reels):
    print(f'{reels[0]} | {reels[1]} | {reels[2]} ')

def calculate_payout(reels, bet):
    if not reels:
        return 0
    if reels[0] == reels[1] == reels[2]:        
        return bet * 10
    if reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        return bet * 2
    return 0

def main():
    balance = starting_balance()
    print("=====================================")
    print("Welcome to Slot Machine Game! 🎰")
    print(f'You start with a balance of ₹{balance}.')

    while balance > 0:
        print(f'Current balance: ₹{balance}')
        bet = bet_amount(balance)
        print("Spinning the reels...")
        print("🎰🎰🎰")

        print("************")
        reels =spin_reels()
        display_reels(reels)
        print("************")

        payout = calculate_payout(reels, bet)
        balance += payout - bet
        if payout > 0:
            print(f'Congratulations! You won🏆 ₹{payout}!')
        else:
            print(f'Sorry, you lost ₹{bet}. Better luck next time!')
            print(f'Your new balance is ₹{balance}.')

        if balance <= 0:
            print("You have run out of balance. Game over!")
            break   

if __name__ == "__main__":
    main()