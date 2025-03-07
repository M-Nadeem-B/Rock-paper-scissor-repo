import tkinter as tk
import random
import numpy as np

# Updated user agreement
user_agreement = """Welcome to the Rock, Paper, Scissors Game!

By clicking 'I Accept', you agree to:
- Play for fun and fair competition.
- Enjoy the game responsibly.
- Challenge yourself and have a great time!

Let's begin!
Remember: you are playing against the computer."""

# Quotes based on game outcome
win_quotes = [
    "A champion is afraid of losing. Everyone else is afraid of winning. - Billie Jean King",
    "Victory is sweetest when you've known defeat. - Malcolm S. Forbes",
    "Champions keep playing until they get it right. - Billie Jean King",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Sometimes you win, sometimes you learn. - John Maxwell"
]

lose_quotes = [
    "Sometimes you win, sometimes you learn. - John Maxwell",
    "Defeat is not the worst of failures. Not to have tried is the true failure. - George Edward Woodberry",
    "Failure is simply the opportunity to begin again, this time more intelligently. - Henry Ford",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Sometimes you win, sometimes you learn. - John Maxwell"
]

tie_quotes = [
    "A tie is like kissing your sister. - Vince Lombardi",
    "Sometimes the best battles end in a draw. - Unknown",
    "A draw is the opportunity for a rematch! - Unknown"
]

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors - Best of 3")
        self.root.geometry("600x400")

        self.l1 = np.array([["tie", "lose", "win"],
                            ["win", "tie", "lose"],
                            ["lose", "win", "tie"]])
        self.l2 = ["rock", "paper", "scissors"]

        self.user_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.round = 0

        self.home_screen()

    def home_screen(self):
        self.label = tk.Label(self.root, text="Welcome to Rock, Paper, Scissors Game", font=("Arial", 16, "bold"))
        self.label.pack(padx=10, pady=20)
        self.root.rowconfigure(1, weight=1)

        # Set width and height to the same values
        button_width = 10  # Adjust as needed
        button_height = 1  # Adjust as needed

        self.label1 = tk.Label(self.root, text=user_agreement, height=10, width=40, font=("Arial", 14))
        self.label1.pack(pady=20)

        self.accept_button = tk.Button(self.root, text="I accept", height=button_height, width=button_width, font=("Arial", 16, "bold"), command=self.start_game)
        self.accept_button.place(x=400, y=345)

        self.reject_button = tk.Button(self.root, text="Reject", height=button_height, width=button_width, font=("Arial", 16, "bold"), command=self.root.destroy)
        self.reject_button.place(x=50, y=345)

    def start_game(self):
        self.label.pack_forget()
        self.label1.pack_forget()
        self.accept_button.place_forget()
        self.reject_button.place_forget()
        self.create_widgets()

    def create_widgets(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(1, weight=1)

        self.label = tk.Label(self.root, text="Best of Three!\nChoose your move:", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")

        self.rock_button = tk.Button(self.root, height=5, text="✊ Rock", font=("Arial", 16), command=lambda: self.play_round(0))
        self.rock_button.grid(row=1, column=0, pady=5, sticky="ew")
        self.rock_button.config(bg="#84a5b8")

        self.paper_button = tk.Button(self.root, height=5, text="✋ Paper", font=("Arial", 16), command=lambda: self.play_round(1))
        self.paper_button.grid(row=1, column=1, pady=5, sticky="ew")
        self.paper_button.config(bg="#4de39b")

        self.scissors_button = tk.Button(self.root, height=5, text="✌️ Scissors", font=("Arial", 16), command=lambda: self.play_round(2))
        self.scissors_button.grid(row=1, column=2, pady=5, sticky="ew")
        self.scissors_button.config(bg="#297de3")

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")

        self.score_label = tk.Label(self.root, text="You: 0  Computer: 0  Tie: 0", font=("Arial", 12))
        self.score_label.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")

    def play_round(self, user_choice):
        computer_choice = random.randint(0, 2)
        result = self.l1[user_choice, computer_choice]

        user_move = self.l2[user_choice]
        computer_move = self.l2[computer_choice]
        tie = user_move == computer_move

        if result == "tie":
            result_text = f"Tie! You: {user_move}, Computer: {computer_move}, Tie: {tie}"
            self.tie_score += 1
        elif result == "win":
            result_text = f"You win! You: {user_move}, Computer: {computer_move}, Tie: {tie}"
            self.user_score += 1
        else:
            result_text = f"Computer wins! You: {user_move}, Computer: {computer_move}, Tie: {tie}"
            self.computer_score += 1

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"You: {self.user_score}  Computer: {self.computer_score} Tie: {self.tie_score}")

        self.round += 1

        if self.round == 3:
            self.end_game()

    def end_game(self):
        self.clear_game_widgets()
        self.display_results()

    def clear_game_widgets(self):
        self.label.grid_forget()
        self.rock_button.grid_forget()
        self.paper_button.grid_forget()
        self.scissors_button.grid_forget()
        self.result_label.grid_forget()
        self.score_label.grid_forget()

    def display_results(self):
        result_text = ""
        if self.user_score > self.computer_score:
            result_text = "You win!"
            quote = random.choice(win_quotes)
        elif self.computer_score > self.user_score:
            result_text = "Computer wins!"
            quote = random.choice(lose_quotes)
        else:
            result_text = "It's a tie in the best of three!"
            quote = random.choice(tie_quotes)

        self.result_label.config(text=result_text, font=("Arial", 16, "bold"))
        self.result_label.pack(pady=10)

        # Set width and height to the same values
        button_width = 10  # Adjust as needed
        button_height = 2  # Adjust as needed

        # Display a random quote
        self.quote_label = tk.Label(self.root, text=quote, font=("Arial", 21, "italic"), wraplength=500, justify="center")
        self.quote_label.pack(pady=20)
        
        self.play_again_button = tk.Button(self.root, text="Play again", height=button_height, width=button_width, font=("Arial", 16, "bold"), command=self.reset_game)
        self.play_again_button.place(x=400, y=300)

        self.quit_button = tk.Button(self.root, text="Quit", height=button_height, width=button_width, font=("Arial", 16, "bold"), command=self.root.destroy)
        self.quit_button.place(x=50, y=300)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.round = 0
        self.result_label.pack_forget()
        self.quote_label.pack_forget()
        self.play_again_button.place_forget()
        self.quit_button.place_forget()
        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()