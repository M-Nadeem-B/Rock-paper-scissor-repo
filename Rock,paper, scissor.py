import random
import numpy as np

# Constants for choices
choices = ["rock", "paper", "scissor"]
result_matrix = np.array([
    ["tie", "lose", "win"],
    ["win", "tie", "lose"],
    ["lose", "win", "tie"]
])


def get_user_choice():
    """Handles user input and ensures a valid choice."""
    while True:
        try:
            choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor: ").strip())
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid choice! Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a number (0, 1, or 2).")


def play_round():
    """Plays one round and returns the result."""
    user_choice = get_user_choice()
    computer_choice = random.randint(0, 2)
    
    print(f"\nYou chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    
    result = result_matrix[user_choice, computer_choice]
    print(f"Result: {result.capitalize()}!\n")
    
    return result


def game():
    """Manages the game loop and score tracking."""
    print("Welcome to Rock, Paper, Scissors Game!\nBest of three rounds wins the game.")
    player_name = input("Enter your name: ").strip().capitalize()
    
    user_score, computer_score = 0, 0
    rounds_to_win = 2  # Best of 3 system
    
    while user_score < rounds_to_win and computer_score < rounds_to_win:
        result = play_round()
        
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        
        print(f"Score -> {player_name}: {user_score}, Computer: {computer_score}\n")
    
    if user_score > computer_score:
        print(f"Congratulations {player_name}, you won the game! 🎉")
    else:
        print("Computer wins the game! Better luck next time.😔")
    
    print("Thanks for playing! 👋")


game()
