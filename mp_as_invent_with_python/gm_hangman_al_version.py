#!usr/bin/python
# Hangman game - Al Sweigart's version (copied for better understanding his programming style)

import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()

def get_random_word(word_list):
    return random.choice(word_list)

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    
    print('Missed letters: ', end='')
    for letter in missed_letters:
        print(letter, end=' ')
    print()
    
    blanks = '_' * len(secret_word)
    
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    
    for letter in blanks:
        print(letter, end=' ')
    print()
        
def get_guess(already_guessed):
    while True:
        letter = input('Guess a letter: ')
        letter = letter.lower()
        if len(letter) != 1:
            print('Please enter a single letter.')
        elif letter in already_guessed:
            print('You have already guessed that letter.')
        elif not 'a' <= letter <= 'z':
            print('Please enter a letter.')
        else:
            return letter
        
def play_again():
    choice = input('Do you want to play again? (yes or no): ')
    return choice.lower().startswith('y')


print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
is_game_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)
    guess = get_guess(missed_letters + correct_letters)
    
    if guess in secret_word:
        correct_letters += guess
    
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(f'Yes! The secret word is {secret_word}. You have won!.')
            is_game_done = True
            
    else:
        missed_letters += guess
        
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print(f'You have run out of guesses.\nAfter {len(missed_letters)} missed letters and {len(correct_letters)} correct letters, the secret word was {secret_word}')
            is_game_done = True
            
    if is_game_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            secret_word = get_random_word(words)
            is_game_done = False
        else:
            break
            
                                                                                                  
                                                                                                 
                                                                                                 
                                                                                                 
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    