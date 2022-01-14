import random


# Puzzle Word List
WORDS = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

# Hangman states
PHASES = ["                         +---+\n                         |   |\n                             |\n                             |\n                             |\n                             |\n                      =========",

          "                         +---+\n                         |   |\n                         O   |\n                             |\n                             |\n                             |\n                      =========",

          "                         +---+\n                         |   |\n                         O   |\n                         |   |\n                             |\n                             |\n                      =========",

          "                         +---+\n                         |   |\n                         O   |\n                        /|   |\n                             |\n                             |\n                      =========",

          "                         +---+\n                         |   |\n                         O   |\n                        /|\  |\n                             |\n                             |\n                      =========",

          "                         +---+\n                         |   |\n                         O   |\n                        /|\  |\n                        /    |\n                             |\n                      =========",

          "                         +---+\n                         |   |\n                         O   |\n                        /|\  |\n                        / \  |\n                             |\n                      ========="]

# Game Variables
WORD = ""
ANSWER = []
PROGRESS_BAR = []


def game_setup():
    """Sets up new game"""
    global WORDS, WORD, ANSWER, PROGRESS_BAR
    WORD = ""
    ANSWER = []
    PROGRESS_BAR = []
    # Print welcome
    print("\n\n|---------------------Welcome to Hangman!----------------------|")
    print("\nWhat ever happens to the person in the gallows is on your hands!\n")
    print("")
    # Set Puzzle Word
    WORD = WORDS[random.randint(0, len(WORDS)-1)]
    for char in WORD:
        ANSWER.append(char)
    # Create progress bar
    for x in range(len(ANSWER)):
        PROGRESS_BAR += "_"


def draw_game_board(player):
    """Prints current state of Hangman puzzle"""
    global PHASES
    # Draw current hangman
    print(PHASES[len(player.incorrect_guesses)])
    # Draw progress bar
    print("                    ", PROGRESS_BAR)
    # Draw guesses
    print("\n  Correct Guesses: ", player.correct_guesses)
    print("Incorrect Guesses: ", player.incorrect_guesses)


def check_guess(player, guess):
    """Checks guess against answer and stores in Player object"""
    global ANSWER
    global PROGRESS_BAR
    correct = False
    guess = guess.lower()
    for char in ANSWER:
        if guess == char:
            correct = True
            player.correct_guesses.append(guess)
            index = ANSWER.index(guess)
            PROGRESS_BAR.insert(index, guess)  # Insert guess at correct index
            PROGRESS_BAR.pop(index+1)  # Remove _ at correct index
            ANSWER.insert(index+1, "_")
            ANSWER.remove(guess)
            print("Correct Guess!")
            break
    if correct is False:
        print("Incorrect Guess!")
        player.incorrect_guesses.append(guess)


def end_game(player):
    # Check game state
    solve = "".join(PROGRESS_BAR)
    if solve == WORD:
        print("\n\n\n\n\n\n\n\n")
        print("Congratulations you saved the Hangman!")
        print("\n\n\n\n\n\n\n\n")
        print("Answer was: ", WORD)
        print("\n\n\n\n\n\n\n\n")
        play_again()
        player.reset_player()
    elif len(player.incorrect_guesses) == len(PHASES)-1:
        draw_game_board(player)
        print("\n\n\n\n\n\n\n\n")
        print("You have let the accused Hang!")
        print("\n\n\n\n\n\n\n\n")
        print("Answer was: ", WORD)
        print("\n\n\n\n\n\n\n\n")
        play_again()
        player.reset_player()


def play_again():
    play_again = input("Would you like to play again?(Y or N): ")
    if play_again == "Y" or play_again == "y":
        game_setup()
    else:
        exit()


def print_intro():
    title = """888\n                                                           
                888\n                                                           
                888\n                                                           
                88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.\n  
                888  88b     88b888  88bd88P 88b888  888  88b     88b888  88b\n
                888  888.d888888888  888888  888888  888  888.d888888888  888\n
                888  888888  888888  888Y88b 888888  888  888888  888888  888\n
                888  888 Y888888888  888  Y88888888  888  888 Y888888888  888\n
                                            888\n                              
                                        Y8b d88P\n                              
                                        Y88P"""
    hangman = """   |_______________``\
                     [/]           [  ]
                     [\]           | ||
                     [/]           |  |
                     [\]           |  |
                     [/]           || |
                    [---]          |  |
                    [---]          |@ |
                    [---]          |  |
                   oOOOOOo         |  |
                  oOO___OOo        | @|
                 oO/|||||\Oo       |  |
                 OO/|||||\OOo      |  |
                 *O\ x x /OO*      |  |
                 /*|  c  |O*\      |  |
                    \_O_/    \     |  |
                     \#/     |     |  |
                  |       |  |     | ||
                  |       |  |_____| ||__
                 _/_______\__|  \  ||||  \
                 /         \_|\  _ | ||\  \
                 |    V    |\  \//\  \  \  \
                 |    |    | __//  \  \  \  \
                 |    |    |\|//|\  \  \  \  \
                 ------------\--- \  \  \  \  \
                 \  \  \  \  \  \  \  \  \  \  \
                 _\__\__\__\__\__\__\__\__\__\__\
                __|__|__|__|__|__|__|__|__|__|__|
                |___| |___|
                |###/ \###|
                \##/   \##/
                 ``     ``"""

    print(title)
