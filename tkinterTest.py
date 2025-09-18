import random
def roll_dice(x):
    dices = [1, 2, 3, 4, 5, 6, 7, 8] # 7 and 8 are special dice
    weight = [10, 10, 10, 10, 8, 3, 2, 0.5] # Adjusted weights for dice frequency
    value = random.choices(dices, weights=weight, k=x)
    return value

def print_dice(dice):
    str_dice = str(dice)
    for i in str_dice:
        if i in ["[", "]", ",", "'"]:
            str_dice = str_dice.replace(i, "")
    return str_dice
money = 100
percent = 0.5
while True:
    print(f"You have ${money}. How much would you like to bet?")
    while True:
        try:
            bet = int(input("Enter your bet amount: "))
            if bet > money * percent:
                print(f"You cannot bet more than {int(percent * 100)}% of your current money.")
            elif bet <= 0:
                print("Bet must be a positive amount.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    print("Rolling the dice...")
    print("The values are...")
    dice = roll_dice(3)
    print(print_dice(dice))
    gained = False
    for i in dice:
        if dice.count(i) == 3:
            if dice.count(7) == 3:
                money += bet * i * 100
                print(f"You rolled three 7's! Jackpot! You win ${bet * i * 100}.")
            else:
                money += bet * i ** 2
                print(f"You rolled three {i}'s! You win ${bet * i ** 2}.")
            gained = True
            break
        elif dice.count(i) == 2:
            money += bet * i
            print(f"You rolled a pair of {i}'s! You win ${bet * i}.")
            gained = True
            break
        elif dice.count(8) == 1:
            print(f"You rolled an eight! You win $1000.")
            money += 500
            gained = True
            break
        elif dice.count(7) == 1:
            money += 250
            print(f"You rolled seven, you win $500.")
            gained = True
            break
        elif dice.count(6) == 1:
            money += 100
            print(f"You rolled six, you win $250.")
            gained = True
            break
    if gained == False:
        print("No matches. You lose your bet.")
    money -= bet
    print(f"You now have ${money}.")
    if money <= 0:
        print("You have run out of money. Game over.")
        break
    elif money > 500:
        percent = 0.75
        print("You can now bet up to 75% of your current money.")
    elif money > 1000:
        percent = 1
        print("You can now bet all of your current money.")
    elif money < 25:
        percent = 1
        print("You can now bet up to all of your current money.")
    elif money >= 10000:
        print("Congratulations! You've reached $10,000 and won the game!")
        try:
            exit = input("You you wish to continue or exit").strip().lower()
            if exit == "exit":
                break
            elif exit == "continue":
                money = 100
                percent = 0.5
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
root.geometry("400x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(padx=100, pady=20)
root.mainloop()