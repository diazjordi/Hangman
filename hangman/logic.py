import random
from types import NoneType
from . import drawings
from resources import word_processing

# import ASCII drawings
hangman_logo = drawings.HANGMAN_LOGO
hangman_phases = drawings.PHASES
hangman_win = drawings.HANGMAN_WIN
hangman_loss = drawings.HANGMAN_LOSS

# Game Variables
puzzle_word = ""
answer = []
progress_bar = []

def game_setup():
    """Sets up new game"""
    global puzzle_word, answer, progress_bar, hangman_logo
    # Print welcome
    print_intro()
    # Ask player for difficulty
    difficulty = select_puzzle_difficulty()
    # Generate Word Lists and set puzzle word
    puzzle_word = generate_puzzle_word(difficulty)
    answer = [x for x in list(puzzle_word)]
    progress_bar = ["_" for x in range(len(answer))]

def select_puzzle_difficulty():
    difficulty = None
    while True:
        try:
            difficulty = int(input("Choose your difficulty\n|--1 for Easy\n|--2 for Moderdate\n|--3 for Difficult\nEnter Choice: "))
        except:
            continue
        else:
            if difficulty > 3:
                continue
            else:
                break
    
    return difficulty

def generate_puzzle_word(difficulty: int):
    words = word_processing.create_word_lists(None)
    word = None
    words_easy = words['easy']
    words_moderate = words['moderate']
    words_difficult = words['difficult']

    if difficulty == 1:
        word = words_easy[random.randint(0, len(words_easy)-1)]
    elif difficulty == 2:
        word = words_moderate[random.randint(0, len(words_moderate)-1)]
    else:
        word = words_difficult[random.randint(0, len(words_difficult)-1)]

    return word

def draw_game_board(player):
    """Prints current state of Hangman puzzle"""
    global hangman_phases
    # Draw current hangman
    print(hangman_phases[len(player.incorrect_guesses)])
    # Draw progress bar
    print("                    ", progress_bar)
    # Draw guesses
    print("\n  Correct Guesses: ", player.correct_guesses)
    print("Incorrect Guesses: ", player.incorrect_guesses)

def check_player_guess(player, guess):
    """Checks guess against answer and stores in Player object"""
    global answer
    global progress_bar
    correct = False
    guess = guess.lower()
    # if len(guess) == 1:

    #elif len(guess) > 1:
    for char in answer:
        if guess == char:
            correct = True
            player.correct_guesses.append(guess)
            index = answer.index(guess)
            progress_bar.insert(answer.index(guess), guess)  # Insert guess at correct index
            progress_bar.pop(index+1)  # Remove _ at correct index
            answer.insert(index+1, "_")
            answer.remove(guess)
            print("Correct Guess!")
            break
    if correct is False:
        print("Incorrect Guess!")
        player.incorrect_guesses.append(guess)

def end_game(player):
    # Check game state
    solve = "".join(progress_bar)
    if solve == puzzle_word:
        print("\n\n\n\n\n\n\n\n")
        print("Congratulations you saved the Hangman!")
        print("\n\n\n\n\n\n\n\n")
        print("Answer was: ", puzzle_word)
        print("\n\n\n\n\n\n\n\n")
        print_outro_win()
        play_again()
        player.reset_player()
    elif len(player.incorrect_guesses) == len(hangman_phases)-1:
        draw_game_board(player)
        """ print("\n\n\n\n\n\n\n\n")
        print("You have let the accused Hang!")
        print("\n\n\n\n\n\n\n\n")
        print("Answer was: ", WORD)
        print("\n\n\n\n\n\n\n\n") """
        print_outro_loss()
        play_again()
        player.reset_player()

def print_intro():
    # Print welcome
    welcome = "Welcome to Hangman!".center(65,"-")
    print(welcome)
    print(hangman_logo)
    print("\nWhat ever happens to the person in the gallows is on your hands!\n")
    print("")

def print_outro_win():
    print("\n" + hangman_win)

def print_outro_loss():
    print("")
    print("GAME LOST".center(65," "))
    print("")
    print("The accused was hung, you failed them!".center(65,"-"))
    print("\n" + hangman_loss)

def play_again():
    play_again = input("Would you like to play again?(Y or N): ")
    if play_again == "Y" or play_again == "y":
        game_setup()
    else:
        exit()