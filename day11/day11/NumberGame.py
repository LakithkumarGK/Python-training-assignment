import random

class GuessMyNumberGame:
    def __init__(self, min_value=1, max_value=100, max_attempts=10):
        # Initialize the game with a secret number, attempt count, and the range of numbers
        self.min_value = min_value
        self.max_value = max_value
        self.max_attempts = max_attempts
        self.secret_number = random.randint(self.min_value, self.max_value)
        self.attempts = 0

    def is_game_over(self):
        """Check if the game is over due to running out of attempts."""
        return self.attempts >= self.max_attempts

    def check_guess(self, guess):
        """Evaluate the player's guess and return appropriate feedback."""
        if self.is_game_over():
            return "Game Over! You've exceeded the maximum attempts."

        self.attempts += 1
        if guess < self.secret_number:
            return "Higher"
        elif guess > self.secret_number:
            return "Lower"
        else:
            return f"Correct!! You've guessed the number in {self.attempts}/{self.max_attempts} attempts.\nExcellent playing!"

    def reset_game(self):
        """Reset the game state for a new round."""
        self.secret_number = random.randint(self.min_value, self.max_value)
        self.attempts = 0
        print("Game has been reset. Ready for a new round!")

class Player:
    def __init__(self, name):
        self.name = name

    def make_guess(self, game):
        """Simulate a player making a guess."""
        guess = int(input(f"{self.name}, enter your guess: "))
        feedback = game.check_guess(guess)
        print(feedback)
        return feedback

class GameController:
    def __init__(self, game, player):
        self.game = game
        self.player = player

    def start_game(self):
        """Start and manage the game loop."""
        print(f"Computer has chosen a number between {self.game.min_value} and {self.game.max_value}. Can you guess it? Max attempts: {self.game.max_attempts}")
        
        while not self.game.is_game_over():
            feedback = self.player.make_guess(self.game)
            if "Correct" in feedback:
                break
        else:
            print(f"Sorry, you've run out of attempts. The secret number was {self.game.secret_number}.")

        print("Game Over!")
        self.ask_to_play_again()

    def ask_to_play_again(self):
        """Ask the player if they want to play again."""
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            self.game.reset_game()
            self.start_game()
        else:
            print("Thanks for playing!")

if __name__ == "__main__":
    # Create the objects for the game
    game = GuessMyNumberGame()
    player = Player("Player 1")
    controller = GameController(game, player)

    # Start the game
    controller.start_game()
    
    
