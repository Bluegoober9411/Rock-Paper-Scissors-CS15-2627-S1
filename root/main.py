import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    player_score = 0
    cpu_score = 0
    while True:
        clear()
        options = ['rock', 'paper', 'scissors']
        print("welcome to rock paper scissors!")
        print(" enter 'rock', 'paper', or 'scissors'")
        player_choice = input("your choice: ").lower()
        clear()
        if player_choice in options:
            cpu_choice = random.choice(options)
            print(f"you chose: {player_choice}")
            print(f"cpu chose: {cpu_choice}\n")
            if player_choice == cpu_choice:
                print("Its a tie!")
            elif (player_choice == 'rock' and cpu_choice == 'scissors') or \
                     (player_choice == 'paper' and cpu_choice == 'rock') or \
                     (player_choice == 'scissors' and cpu_choice == 'paper'):
                print("you win!")
                player_score += 1
            else:
                print("you lose!")
                cpu_score += 1
            print(f"\nYour score: {player_score}")
            print(f"cpu score: {cpu_score}")
            input()
        else:
            print("incorrect response")
            input()
main()

