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
target_word = ""
guess = ""

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


def play():
    """Code that controls the interactive game play"""
    #Sets attempts amount to 1
    count = 1
    # select a word of the day:
    target_word = get_target_word()
    # build a list of valid words (words that can be entered in the UI):
    valid_words = get_valid_words()
    #cheat
    print (target_word)

    #welcome()
    while count < 7:
        print("in while", target_word)
        guess = ask_for_guess(valid_words)
        print(guess, target_word)
        score = score_guess()
        print(score)
        print("Here's what you got right!")
        print(format_score(score))
        if is_correct(score):
            print("Congratulations! You've won!")
        else:
            count += 1
        
            if count < 6:
                print("Tough luck. Try again!")
                print("You are on attempt number:", count)
            elif count == 6:
                print("This is your last attempt! Guess wisely!")
                
    if count == 7:
        print("Game over! You lose..")
        

def is_correct():
    """Checks if the player's guess is fully correct"""
    if score == (2,2,2,2,2):
        return True
    else: 
        return False


def get_valid_words():
    """Converts all_words.txt into a list"""
    filer = open('all_words.txt', 'r')
    valid_words = []

    for line in filer:
        
        line_strip = line.rstrip('\n')
        line_split = str(line_strip.split())
        valid_words.append(w)
        print(valid_words)
    return valid_words

def get_target_word():
    """Converts target_words.txt into a list"""
    file = open('target_words.txt', 'r')
    target_words = []

    for line in file:
        line_strip = line.strip()
        line_split = line_strip.split()
        target_words.append(line_split)
    
    target_word = target_words[random.randint(0, len(target_words))]
    return str(target_word)

def ask_for_guess(valid_words):
    """Asks the player for a guess and identifies whether it's valid or not"""
    
    #guess = input("Please enter a guess: ").lower()
    
    while True:
        guess = input("Please enter a guess: ").lower()
        print(guess)
        if guess not in valid_words:
            print("not found")
            
        else:
            return guess
        


def score_guess():
    print(guess, target_word)
    #Start of function
    score = [0,0,0,0,0]
    guess_dic = {}
    target_dic = {}
    
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


def format_score(score):
    """Formats the score to be clear for the player to understand"""
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
    

play()
