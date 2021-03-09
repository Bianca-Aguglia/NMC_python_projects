#!usr/bin/python
#text game based on Al Sweigart's 'Invent with Python' ebook

import time
import random

def main():
    while True:
        display_intro()
        cave = choose_cave()
        check_cave(cave)
        play_again = input('Do you want to play again? (yes or no) ')
        if play_again != 'y' and play_again != 'yes':
            break
        print()
    print('\nThank you for playing.')        

def display_intro():
    print('''You're in a land full of dragons. In front of you there are two caves. In one cave, the dragon is friendly and will share his treasure with you. In the other cave, the dragon is greedy and hungry and will eat you on sight.''')
    
def choose_cave():
    cave = ''
    while cave != 1 and cave!= 2:
        print('Which cave will you go into? (1 or 2) ')
        cave = int(input())
    return cave
        
def check_cave(cave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps in front of you! He opens his jaws and...')
    time.sleep(2)
    is_friendly = random.randint(1,2)
    if cave == is_friendly:
        print('Gives you his treasure!')
    else:
        print('Gobbles you in one bite!')
        
if __name__ == '__main__':
    main()        
