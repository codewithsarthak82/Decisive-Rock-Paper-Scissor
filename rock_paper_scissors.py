"""
Rock, Paper, Scissors Game -  A complete GUI implementation using Tkinter
"""

import tkinter as tk
import random


class RockPaperScissorsGame:
    """Main game class for Rock, Paper, Scissors"""
    
    def __init__(self, root):
        """Initialize the game window and components"""
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("700x550")
        self.root.resizable(True, True)
        
        # Game state variables
        self.player_score = 0
        self.computer_score = 0
        self.draw_count = 0
        
        # Window state variables
        self.is_maximized = False
        self.normal_width = 700
        self.normal_height = 550
        
        # Create and place UI elements
        self.create_widgets()
        
        # Center the window on screen
        self.center_window()
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Create and arrange all UI widgets"""
        
        # Title label
        title_label = tk.Label(
            self.root,
            text="Rock Paper Scissors",
            font=("Arial", 24, "bold"),
            pady=20
        )
        title_label.pack()
        
        # Player choice display
        self.player_choice_label = tk.Label(
            self.root,
            text="Your choice: -",
            font=("Arial", 14),
            pady=10
        )
        self.player_choice_label.pack()
        
        # Computer choice display
        self.computer_choice_label = tk.Label(
            self.root,
            text="Computer choice: -",
            font=("Arial", 14),
            pady=10
        )
        self.computer_choice_label.pack()
        
        # Result display
        self.result_label = tk.Label(
            self.root,
            text="Make your choice!",
            font=("Arial", 16, "bold"),
            pady=20,
            fg="blue"
        )
        self.result_label.pack()
        
        # Scoreboard frame
        scoreboard_frame = tk.Frame(self.root)
        scoreboard_frame.pack(pady=15)
        
        # Scoreboard title
        scoreboard_title = tk.Label(
            scoreboard_frame,
            text="Scoreboard",
            font=("Arial", 14, "bold")
        )
        scoreboard_title.pack()
        
        # Player score
        self.player_score_label = tk.Label(
            scoreboard_frame,
            text="Player: 0",
            font=("Arial", 12),
            pady=5
        )
        self.player_score_label.pack()
        
        # Computer score
        self.computer_score_label = tk.Label(
            scoreboard_frame,
            text="Computer: 0",
            font=("Arial", 12),
            pady=5
        )
        self.computer_score_label.pack()
        
        # Draw count
        self.draw_count_label = tk.Label(
            scoreboard_frame,
            text="Draws: 0",
            font=("Arial", 12),
            pady=5
        )
        self.draw_count_label.pack()
        
        # Choice buttons label
        choice_label = tk.Label(
            self.root,
            text="Choose your move:",
            font=("Arial", 12, "bold"),
            pady=10
        )
        choice_label.pack()
        
        # Buttons frame for horizontal layout
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)
        
        # Choice buttons arranged horizontally
        self.rock_button = tk.Button(
            buttons_frame,
            text="Rock",
            font=("Arial", 14),
            width=12,
            height=2,
            command=lambda: self.handle_player_choice("Rock")
        )
        self.rock_button.pack(side=tk.LEFT, padx=15)
        
        self.paper_button = tk.Button(
            buttons_frame,
            text="Paper",
            font=("Arial", 14),
            width=12,
            height=2,
            command=lambda: self.handle_player_choice("Paper")
        )
        self.paper_button.pack(side=tk.LEFT, padx=15)
        
        self.scissors_button = tk.Button(
            buttons_frame,
            text="Scissors",
            font=("Arial", 14),
            width=12,
            height=2,
            command=lambda: self.handle_player_choice("Scissors")
        )
        self.scissors_button.pack(side=tk.LEFT, padx=15)
        
        # Control buttons frame
        control_buttons_frame = tk.Frame(self.root)
        control_buttons_frame.pack(pady=15)
        
        # Maximize/Restore button
        self.maximize_button = tk.Button(
            control_buttons_frame,
            text="Maximize Window",
            font=("Arial", 11),
            width=18,
            height=2,
            command=self.toggle_maximize,
            bg="#4ecdc4",
            fg="white"
        )
        self.maximize_button.pack(side=tk.LEFT, padx=10)
        
        # Reset button
        self.reset_button = tk.Button(
            control_buttons_frame,
            text="Reset Game",
            font=("Arial", 12),
            width=15,
            height=2,
            command=self.reset_game,
            bg="#ff6b6b",
            fg="white"
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)
    
    def get_computer_choice(self):
        """Generate a random choice for the computer"""
        choices = ["Rock", "Paper", "Scissors"]
        return random.choice(choices)
    
    def calculate_result(self, player_choice, computer_choice):
        """
        Determine the game result based on player and computer choices
        
        Returns:
            "Win" if player wins
            "Lose" if player loses
            "Draw" if it's a tie
        """
        if player_choice == computer_choice:
            return "Draw"
        
        # Winning combinations
        winning_combinations = {
            "Rock": "Scissors",      # Rock beats Scissors
            "Paper": "Rock",         # Paper beats Rock
            "Scissors": "Paper"      # Scissors beats Paper
        }
        
        if winning_combinations[player_choice] == computer_choice:
            return "Win"
        else:
            return "Lose"
    
    def update_scoreboard(self, result):
        """Update the scoreboard based on the game result"""
        if result == "Win":
            self.player_score += 1
        elif result == "Lose":
            self.computer_score += 1
        else:  # Draw
            self.draw_count += 1
        
        # Update scoreboard labels
        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
        self.draw_count_label.config(text=f"Draws: {self.draw_count}")
    
    def update_ui(self, player_choice, computer_choice, result):
        """Update all UI elements with game results"""
        # Update choice displays
        self.player_choice_label.config(text=f"Your choice: {player_choice}")
        self.computer_choice_label.config(text=f"Computer choice: {computer_choice}")
        
        # Update result display with color coding
        if result == "Win":
            self.result_label.config(text="You Win!", fg="green")
        elif result == "Lose":
            self.result_label.config(text="You Lose!", fg="red")
        else:
            self.result_label.config(text="It's a Draw!", fg="orange")
    
    def disable_choice_buttons(self):
        """Disable choice buttons to prevent rapid clicking"""
        self.rock_button.config(state="disabled")
        self.paper_button.config(state="disabled")
        self.scissors_button.config(state="disabled")
    
    def enable_choice_buttons(self):
        """Re-enable choice buttons after a brief delay"""
        self.rock_button.config(state="normal")
        self.paper_button.config(state="normal")
        self.scissors_button.config(state="normal")
    
    def handle_player_choice(self, player_choice):
        """
        Main game handler when player makes a choice
        
        Args:
            player_choice: The player's choice ("Rock", "Paper", or "Scissors")
        """
        # Disable buttons to prevent rapid clicking
        self.disable_choice_buttons()
        
        # Get computer's choice
        computer_choice = self.get_computer_choice()
        
        # Calculate result
        result = self.calculate_result(player_choice, computer_choice)
        
        # Update UI
        self.update_ui(player_choice, computer_choice, result)
        
        # Update scoreboard
        self.update_scoreboard(result)
        
        # Re-enable buttons after 1.2 seconds for smooth gameplay
        self.root.after(1200, self.enable_choice_buttons)
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Reset scores
        self.player_score = 0
        self.computer_score = 0
        self.draw_count = 0
        
        # Reset UI displays
        self.player_choice_label.config(text="Your choice: -")
        self.computer_choice_label.config(text="Computer choice: -")
        self.result_label.config(text="Make your choice!", fg="blue")
        
        # Reset scoreboard
        self.player_score_label.config(text="Player: 0")
        self.computer_score_label.config(text="Computer: 0")
        self.draw_count_label.config(text="Draws: 0")
        
        # Ensure buttons are enabled
        self.enable_choice_buttons()
    
    def toggle_maximize(self):
        """Toggle between maximized and normal window size"""
        if not self.is_maximized:
            # Store current position before maximizing
            self.root.update_idletasks()
            self.normal_geometry = self.root.geometry()
            
            # Maximize the window (cross-platform approach)
            try:
                # Try Windows method
                self.root.state('zoomed')
            except:
                try:
                    # Try Linux/Unix method
                    self.root.attributes('-zoomed', True)
                except:
                    # Fallback: set to screen size
                    screen_width = self.root.winfo_screenwidth()
                    screen_height = self.root.winfo_screenheight()
                    self.root.geometry(f"{screen_width}x{screen_height}+0+0")
            
            self.is_maximized = True
            self.maximize_button.config(text="Restore Window")
        else:
            # Restore to normal size
            try:
                # Try Windows method
                self.root.state('normal')
            except:
                try:
                    # Try Linux/Unix method
                    self.root.attributes('-zoomed', False)
                except:
                    pass  # Already normal size
            
            # Restore to original size and center
            self.root.geometry(f"{self.normal_width}x{self.normal_height}")
            self.center_window()
            
            self.is_maximized = False
            self.maximize_button.config(text="Maximize Window")


def main():
    """Main function to start the game"""
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()

