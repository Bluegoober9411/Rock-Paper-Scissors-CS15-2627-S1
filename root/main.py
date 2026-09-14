import random

def get_cpu_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice in valid_choices:
            return player_choice
        else:
            print("Invalid choice. Try again.")

def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        return "Tie"

    if cpu_choice == "rock":
        return "PLAYER" if player_choice == "paper" else "CPU"

    if cpu_choice == "paper":
        return "PLAYER" if player_choice == "scissors" else "CPU"

    # cpu_choice == "scissors"
    return "PLAYER" if player_choice == "rock" else "CPU"

def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()
    winner = check_winner(cpu_choice, player_choice)

    print(f"\nCPU chose: {cpu_choice}")
    print(f"Round winner: {winner}\n")

    return winner

# Tournament logic
player_wins = 0
cpu_wins = 0
ties = 0

print("Welcome to Rock, Paper, Scissors — First to 3 wins!")

while player_wins < 3 and cpu_wins < 3:
    result = play_round()

    if result == "PLAYER":
        player_wins += 1
    elif result == "CPU":
        cpu_wins += 1
    else:
        ties += 1

    print(f"Score — Player: {player_wins}, CPU: {cpu_wins}, Ties: {ties}")
    print("-" * 40)

# Final result
if player_wins == 3:
    print(" You win the tournament!")
else:
    print(" CPU wins the tournament!")

print("Thanks for playing!")
