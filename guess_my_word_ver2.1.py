#!/usr/bin/env python3
"""Guess-My-Word is a game where the player has to guess a word.
<1. User has to guess the word of the day in 6 attempts or less
2. Only valid English words can be guessed (guesses should be words in the word bank)
3. If the letter and position is correct, it will output 'X'
4. If the letter is correct but the position is wrong, it will output 'O'
5. An incorrect letter will output '_'
6. Letters can be used multiple times for different guesses
7. The word of the day changes everyday. The user effectively has a 24h time limit> 
Author: <Andrew Lam>
Company: <TAFE>
Copyright: <2022>

"""
# Your code must use PEP8
# Your code must be compatible with Python 3.1x
# You cannot use any libraries outside the python standard library without the explicit permission of your lecturer.

# This code uses terms and symbols adopted from the following source:
# See https://github.com/3b1b/videos/blob/68ca9cfa8cf5a41c965b2015ec8aa5f2aa288f26/_2022/wordle/simulations.py#L104


MISS = 0  # _-.: letter not found ⬜
MISSPLACED = 1  # O, ?: letter in wrong place 🟨
EXACT = 2  # X, +: right letter, right place 🟩

MAX_ATTEMPTS = 6
WORD_LENGTH = 5

ALL_WORDS = 'file/path/of/all_words.txt'
TARGET_WORDS = 'file/path/of/target_words.txt'

valid_words = list()
target_word = list()
g_dict = {}
tw_dict = {}
answer = None
import random

def welcome():
    """Welcome function used to greet the player"""
    name = input("Please enter a name: ")
    print("Welcome to Wordle Clone, " + name + ". You have 6 attempts to guess the 5 letter word.")
    print("Only valid English words can be guessed")
    print("If the letter and position is correct, it will output 'X'")
    print("If the letter is correct but the position is wrong, it will output 'O'")
    print("An incorrect letter will output '_'")
    print("Good luck!")


INCOMPLETE def play():
    """Code that controls the interactive game play"""
    # select a word of the day:
    word_of_the_day = get_target_word()
    # build a list of valid words (words that can be entered in the UI):
    valid_words = get_valid_words()
    # do the following in an iteration construct
    guess = ask_for_guess(valid_words)
    score = score_guess(guess, word_of_the_day)
    print("Result of your guess:")  # Put some of your own personality into this!
    print(format_score(guess, score))
    if is_correct(score):
        print("Winner: You need to write code to exit out of this loop")
    # end iteration
    return True


INCOMPLETE def is_correct(score):
    """Checks if the score is entirely correct and returns True if it is
    Examples:
    >>> is_correct((1,1,1,1,1))
    False
    >>> is_correct((2,2,2,2,1))
    False
    >>> is_correct((0,0,0,0,0))
    False
    >>> is_correct((2,2,2,2,2))
    True"""
    return False


def get_valid_words():
    """Code that converts all_words.txt into a list"""
    file = open('all_words.txt', 'r')

    for line in file:
        line_strip = line.strip()
        line_split = line_strip.split()
        valid_words.append(line_split)

def get_target_word():
    """Code that converts target_words.txt into a list"""
    file = open('target_words.txt', 'r')

    for line in file:
        line_strip = line.strip()
        line_split = line_strip.split()
        target_word.append(line_split)
    
    target_word = target_word[random.randint(0, len(target_word))]
    return(target_word)

def ask_for_guess(valid_words):
    while True:
        guess = input("Please enter a guess: ").lower()
        if len(guess) != 5:
            print("Your word is not a valid word")
        else:
            break


INCOMPLETE def score_guess(guess, target_word):
    for index, char in enumerate(guess):
    if char not in g_dict:
        g_dict[char] = str(index)
    else:
        multiple_index = g_dict.get(char) + " " + str(index)
        g_dict[char] = (multiple_index)

    for index, char in enumerate(target_word):
    if char not in tw_dict:
        tw_dict[char] = str(index)
    else:
        multiple_index = tw_dict.get(char) + " " + str(index)
        tw_dict[char] = (multiple_index)

    for index, char in g_dict:
        if char not in tw_dict:
            answer = answer + '0'
        elif g_dict[char] = tw_dict[char]:
            if g_dict[index] == tw_dict[index]:
                answer = answer + '2'
        else:
            answer = answer + '1'
            
            

INCOMPLETE def help():
    #prints out comments about each function inside the game, the green text. in command prompt
    """Provides help for the game"""
    pass


INCOMPLETE def format_score(guess, score):
    """Formats a guess with a given score as output to the terminal.
    The following is an example output (you can change it to meet your own creative ideas, 
    but be sure to update these examples)
    >>> print(format_score('hello', (0,0,0,0,0)))
    H E L L O
    _ _ _ _ _
    >>> print(format_score('hello', (0,0,0,1,1)))
    H E L L O
    _ _ _ ? ?
    >>> print(format_score('hello', (1,0,0,2,1)))
    H E L L O
    ? _ _ + ?
    >>> print(format_score('hello', (2,2,2,2,2)))
    H E L L O
    + + + + +"""
    pass


INCOMPLETE def main(test=False):
    if test:
        #Don't worry about this part for now
        import doctest
        return doctest.testmod()
    play()


if __name__ == '__main__':
    print(main(test=True))

filepath = getfile()
print("get file successful")
