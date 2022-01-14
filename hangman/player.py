class Player:
    """Player object for Hangman game, keeps track of guesses and score"""

    def __init__(self):
        self.guesses = []
        self.correct_guesses = []
        self.incorrect_guesses = []
        self.score = 0

    def print_player_details(self):
        """Prints player detals"""
        print(self.correct_guesses)
        print(self.incorrect_guesses)
        print(self.score)

    def reset_player(self):
        """Resets player to start new Hangman puzzle, retains score"""
        self.guesses = []
        self.correct_guesses = []
        self.incorrect_guesses = []
