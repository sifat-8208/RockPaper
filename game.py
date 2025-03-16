import random

class Player:
    """Represents a player in the game, either user or computer."""
    
    def __init__(self, name):
        self.name = name
        self.choice = None

    def make_choice(self, choice=None):
        """Set the player's choice. For the computer, it will be random."""
        if self.name.lower() == "computer" and choice is None:
            self.choice = random.choice(['rock', 'paper', 'scissors'])
        elif self.name.lower() == "user" and choice is not None:
            self.choice = choice
        else:
            raise ValueError("Invalid choice provided.")

class Game:
    """The Rock, Paper, Scissors game logic."""
    
    def __init__(self):
        self.user = Player("user")
        self.computer = Player("computer")
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if user_choice in ['rock', 'paper', 'scissors']:
                self.user.make_choice(user_choice)
                break
            else:
                print("Invalid input. Please enter one of the following: rock, paper, or scissors.")

    def determine_winner(self):
        user_choice = self.user.choice
        computer_choice = self.computer.choice

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

    def play_round(self):
        self.get_user_choice()
        self.computer.make_choice()
        result = self.determine_winner()
        self.update_score(result)
        print(result)
        print(f"Score -> You: {self.user_score} | Computer: {self.computer_score}")

    def play_game(self):
        try:
            while True:
                print("\n--- Rock, Paper, Scissors Game ---")
                self.play_round()
                
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again != 'yes':
                    print(f"Final Score -> You: {self.user_score} | Computer: {self.computer_score}")
                    print("Thanks for playing!")
                    break
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    game = Game()
    game.play_game()
