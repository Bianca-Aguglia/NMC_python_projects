#!usr/bin/python
# hangman game based on Al Sweigart't tutorial
# word dictionary based on dataset from http://www.mit.edu/~ecprice/wordlist.10000

import time
import random
import pickle

def main():
    print('\n\nWelcome to H A N G M A N!')
    print('-------------------')
    play_game()
    
def load_word_list():
    with open('word_list.pkl', 'rb') as infile:
        word_list = pickle.load(infile)
        return word_list
    
def is_valid_length(word_length):
    lengths = ['3', '4', '5', '6', '7', '8', '9', '10+']
    return word_length in lengths

def choose_word(word_length):
    word = None
    while word is None or word in played_words:
        word = random.choice(word_list[word_length])
    return word

def draw_picture(wrong_guess):
    picture_stages = {0: {'head': 0, 'body': 0, 'left_arm': 0, 'right_arm': 0, 'left_leg': 0, 'right_leg': 0},
                      1: {'head': 1, 'body': 0, 'left_arm': 0, 'right_arm': 0, 'left_leg': 0, 'right_leg': 0},
                      2: {'head': 1, 'body': 1, 'left_arm': 0, 'right_arm': 0, 'left_leg': 0, 'right_leg': 0},
                      3: {'head': 1, 'body': 1, 'left_arm': 1, 'right_arm': 0, 'left_leg': 0, 'right_leg': 0},
                      4: {'head': 1, 'body': 1, 'left_arm': 1, 'right_arm': 1, 'left_leg': 0, 'right_leg': 0},
                      5: {'head': 1, 'body': 1, 'left_arm': 1, 'right_arm': 1, 'left_leg': 1, 'right_leg': 0},
                      6: {'head': 1, 'body': 1, 'left_arm': 1, 'right_arm': 1, 'left_leg': 1, 'right_leg': 1},
                      7: {'head': 1, 'body': 1, 'left_arm': 1, 'right_arm': 1, 'left_leg': 1, 'right_leg': 1}}
    
    head = 'o'
    la = ll = '/' # left_arm and left_leg
    body = '|'
    ra = rl = '\\' # right_arm and right_leg

    stage = picture_stages[wrong_guess]
    # make picture string
    drawing = f'''     +-----+
     {head * stage['head']:^1}     |
    {la * stage['left_arm']:1}{body * stage['body']:1}{ra * stage['right_arm']:1}    |
    {ll * stage['left_leg']:1} {rl * stage['right_leg']:1}    |
         -----'''
    return drawing

def draw_word(word_length, guessed_letters, target_word):
    word = ['  '] * word_length
    dash = '-'
    dashes = f'{dash:<2}' * word_length
    for letter in guessed_letters:
        indices = [i for i, _ in enumerate(target_word) if _ == letter]
        for idx in indices:
            word[idx] = f'{letter:<2}'
    word = ''.join(word)
    word_and_dashes = f'{word}\n{dashes}'
    return word_and_dashes

def draw_all(wrong_guesses, word, guessed_letters, all_guesses):
    print(draw_picture(wrong_guesses))
    print(draw_word(len(word), guessed_letters, word))
    print()
    print(f'Guesses left: {7 - wrong_guesses}')
    print(f'Letters tried so far: ', end='')
    print(' '.join(sorted(all_guesses))) 
    

def play_game():
    word_length = input('Choose a word length (3, 4, 5, 6, 7, 8, 9, or 10+): ')
    while not is_valid_length(word_length):
        word_length = input('Please choose a valid length (3, 4, 5, 6, 7, 8, 9, or 10+): ')
    print()
    word = choose_word(word_length)
    played_words.append(word)
    wrong_guesses = 0
    all_guesses = set()
    guessed_letters = set()
    correct_letters = set(word)
    while wrong_guesses < 7 and guessed_letters != correct_letters:
        draw_all(wrong_guesses, word, guessed_letters, all_guesses)            
        guessed_letter = input('Guess a letter: ')
        print()
        all_guesses.add(guessed_letter)
        if guessed_letter in correct_letters:
            guessed_letters.add(guessed_letter)
        else:
            wrong_guesses += 1 
    draw_all(wrong_guesses, word, guessed_letters, all_guesses)
    print()
    if wrong_guesses == 7:
        print(f'The correct word was: {word}')
    else:
        print(f'Great job! Your guessed the correct word!')
    
if __name__ == '__main__':
    played_words = []
    word_list = load_word_list()
    main()
              
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    