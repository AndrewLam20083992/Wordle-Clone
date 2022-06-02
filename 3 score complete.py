"""given two strings of equal length, returns a tuple of ints representing the score of the guess
against the target word (MISS, MISPLACED, or EXACT)
Here are some example (will run as doctest):

>>> score_guess('hello', 'hello')
(2, 2, 2, 2, 2)
>>> score_guess('drain', 'float')
(0, 0, 1, 0, 0)
>>> score_guess('hello', 'spams')
(0, 0, 0, 0, 0)

Try and pass the first few tests in the doctest before passing these tests.
>>> score_guess('gauge', 'range')
(0, 2, 0, 2, 2)
>>> score_guess('melee', 'erect')
(0, 1, 0, 1, 0)
>>> score_guess('array', 'spray')
(0, 0, 2, 2, 2)
>>> score_guess('train', 'tenor')
(2, 1, 0, 0, 1)
    """
guess = input("guess ")
target_word = input("target ")
guess_dic = {}
target_dic = {}
output = ()
multiple_guess = []
multiple_day = []

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
        target_dic[value]= str(count)
    else:
        num = target_dic.get(value) + " " + str(count)
        target_dic[value] = (num)

#Start testing
for value, letter in enumerate(guess):
    if letter in target_dic:
        
        #needs a list when multiple occurances of a specific letter.
        target = target_dic.get(letter)
        target = target.split(" ")

        source = guess_dic.get(letter)
        source = source.split(" ")

        if str(value) in target:
            output += (2, )

        else:
            if len(target) == 1 and len(source) == 1: 
               output += (1, )
            elif len(target) == 2 and len(source) == 2:
                output += (1, )
            elif len(target) == 1 and len(source) == 2 and source[0] == str(value) and target[0] == source[1] :
                output += (0, )
            elif len(target) == 1 and len(source) == 2 and source[0] == str(value):
                output += (1, )
            else:
                output += (0, )
    else:
        output += (0, )

print(output)        
    
