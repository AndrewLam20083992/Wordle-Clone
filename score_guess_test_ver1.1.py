
g_dict = {}
tw_dict = {}

def score_guess(guess, target_word):
    for index, char in enumerate(guess):
        if char not in g_dict:
            g_dict[char] = str(index)
        else:
            multiple_index_g = g_dict.get(char) + " " + str(index)
            g_dict[char] = multiple_index_g

    for index, char in enumerate(target_word):
        if char not in tw_dict:
            tw_dict[char] = str(index)
        else:
            multiple_index_tw = tw_dict.get(char) + " " + str(index)
            tw_dict[char] = multiple_index_tw
    answer = ''
    for char in g_dict:
        if char not in tw_dict:
            answer = answer + '0'
        '''elif g_dict[char] == tw_dict[char]:
            index_check_tw = tw_dict.get(char)
            index_check_tw = index_check_tw.split(' ')

            index_check_g = g_dict.get(char)
            index_check_g = index_check_g.split(' ')
            
            if str(index) in index_check_tw:
                answer = answer + '2'
                '''
        elif char in tw_dict:
            if multiple_index_tw[0] = index_check_g[0]:
            answer = answer + '2'
    print(answer)
            
score_guess('drone', 'float')

