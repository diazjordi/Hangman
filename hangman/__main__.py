import sys
from hangman import logic
from .player import Player


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    # Set up game
    player = Player()
    # Set Puzzle Word
    logic.game_setup()

    # Start Game Loop
    while True:
        # Print current Hangman state
        logic.draw_game_board(player)
        # logic.print_current_hangman(playe
        # Ask player for guess
        guess = input("      Enter guess: ")
        # Check Guess
        logic.check_guess(player, guess)
        # Check Game State
        logic.end_game(player)


if __name__ == '__main__':
    main()
