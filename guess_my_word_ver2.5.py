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
    count = 1
    
    guess = ask_for_guess(valid_words)
    score = score_guess(guess, word_of_the_day)
    print("Result of your guess:")  # Put some of your own personality into this!
    print(format_score(guess, score))
    if is_correct(score):
        print("Winner: You need to write code to exit out of this loop")
    # end iteration
    return True


def is_correct(main_score):
    if main_score == (2,2,2,2,2):
        return True
    else: 
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


def score_guess(guess, target_word):
    #for testing purposes
    guess = input("Guess:")
    target_word = input("target:")
    #Start of function
    score = [0,0,0,0,0]

    #Guess: build dictionary of letter and index
    for count, value in enumerate(guess):
        if value not in guess_dic:
            guess_dic[value] = str(count)
        else:
            num = guess_dic.get(value) + " " + str(count)
            guess_dic[value] = (num)

    #Secret: build dictionary of letter and index
    for count, value in enumerate(target_word):
        if value not in target_dic:
            target_dic[value] = str(count)
        else:
            num = target_dic.get(value) + " " + str(count)
            target_dic[value] = (num)

    #Start testing
    for value, letter in enumerate(guess):
        if letter in target_dic:

            #needs a list when multiple occurances of a specific letter
            target = target_dic.get(letter)
            target = target.split(" ")

            source = guess_dic.get(letter)
            source = source.split(" ")

            if str(value) in target:
                score[value] = 2

            else:
                if (
                    (len(target) == 1 and len(source) == 1)
                    or (len(target) == 2 and len(source) == 2 )
                    or (len(target) == 2 and len(source) > 2 and source[0] == str(value))
                    or (len(target) == 2 and len(source) > 2 and source[1] == str(value))
                ):
                    score[value] = 1
                elif len(target) == 1 and len(source) == 2 and source[0] == str(value) and target[0] == source[1]:
                    score[value] = 0
                elif len(target) == 1 and len(source) == 2 and source[0] == str(value):
                    score[value] = 1
        score = (tuple(score))
        return (score)


def format_score(guess, score):
    all_caps = guess.upper()
    print(all_caps[0] + " " +
          all_caps[1] + " " +
          all_caps[2] + " " +
          all_caps[3] + " " +
          all_caps[4])

    for i in score:
        if i == 0:
            print("_ ", end = "")
        elif i == 1:
            print("O ", end = "")
        else:
            print("X ", end = "")
    print()



play()
