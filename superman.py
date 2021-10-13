import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words.list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    # TODO loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    pass

def is_guess_in_word(guess, secret_word):
    # TODO: check if the letter guess is in the secret word
    pass

def spaceman(secret_word):
    #TODO: show the player information about the game according to the project spec
    #TODO: ask the player to guess one letter per round and check that it is only one letter
    #TODO: check if the guessed letter is in the secret or not and give the player feedback
    #TODO: show the guessed word so far
    #TODO: check if the game has been won or lost

secret_word = load_word()
spaceman(secret_word)
