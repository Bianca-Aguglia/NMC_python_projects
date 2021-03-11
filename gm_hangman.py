#!usr/bin/python
# hangman game based on Al Sweigart't tutorial
# word dictionary based on dataset from http://www.mit.edu/~ecprice/wordlist.10000

import time
import random
import pickle

def main():
    print('Welcome to Hangman!')
    print('-------------------')
    played_words = []
    word_list = load_word_list()
    play_game
    
def load_word_list():
    with open('word_list.pkl', 'rb') as infile:
        word_list = pickle.load(infile)
        return word_list
    
def is_valid_length(word_length):
    lengths = ['3', '4', '5', '6', '7', '8', '9', '10+']
    return word_length in lengths

def choose_word(word_length):
    word = None
    while word in played_words:
        word = random.choice(words[word_length])
        return word

def make_picture(guess_number):
    picture_stages = {0: {'head': 0, 'body': 0, 'left_arm': 0, 'right_arm': 0, 'left_leg': 0, 'right_leg': 0},
                      1: {'head': 1, 'body': 0, 'left_arm': 0, 'right_arm': 0, 'left_leg': 0, 'right_leg': 0},
                      2: {'head': 1, 'body': 1, 'left_arm': 0, 'right_arm': 0, 'left_leg': 0, 'right_leg': 0},
                      3: {'head': 1, 'body': 1, 'left_arm': 1, 'right_arm': 0, 'left_leg': 0, 'right_leg': 0},
                      4: {'head': 1, 'body': 1, 'left_arm': 1, 'right_arm': 1, 'left_leg': 0, 'right_leg': 0},
                      5: {'head': 1, 'body': 1, 'left_arm': 1, 'right_arm': 1, 'left_leg': 1, 'right_leg': 0},
                      6: {'head': 1, 'body': 1, 'left_arm': 1, 'right_arm': 1, 'left_leg': 1, 'right_leg': 1}}
    
    head = 'o'
    la = ll = '/' # left_arm and left_leg
    body = '|'
    ra = rl = '\\' # right_arm and right_leg

    stage = picture_stages[picture_stage]
    # make picture string
    drawing = f'''     +-----+
     {head * stage['head']:^1}     |
    {la * stage['left_arm']:1}{body * stage['body']:1}{ra * stage['right_arm']:1}    |
    {ll * stage['left_leg']:1} {rl * stage['right_leg']:1}    |
         -----'''
    return drawing
    

def play_game():
    word_length = input('Choose a word length (3, 4, 5, 6, 7, 8, 9, or 10+): ')
    while not is_valid_length(word_length):
        word_length = input('Please choose a valid length (3, 4, 5, 6, 7, 8, 9, or 10+): ')
    word = choose_word(word_length)
    played_words.append(word)
    guess_number = 0
    while guess_number < 7:
        
    