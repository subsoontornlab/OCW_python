# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SMALL_TIME = 0.00001
K = 1 # multiplier for timelimit

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print( "  " + str(len(wordlist)) +  "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    wordScore = 0
    for i in range(0, len(word)):
        i_char = word[i]
        wordScore += SCRABBLE_LETTER_VALUES[i_char]
    if len(word) == n:
        wordScore += 50
    return wordScore
        

def get_words_to_points(word_list):
    '''
    Return a dict that maps everyword in word_list to its point value
    ''' 
    points_dict = {}
    for word in word_list:
        points_dict[word] = get_word_score(word,0) 
        
    return points_dict


    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end = ' ')              # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3) # ** add int()
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    for i in range(0,len(word)):
        i_char = word[i]
        hand[i_char] -= 1
        if hand[i_char] < 1:
            hand.pop(i_char)
    return hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    #check if the word is entirely composed of letters in the hand
    inHand = True
    word_charFreq = get_frequency_dict(word)
    for k in word_charFreq.keys():
        if hand.get(k,0) < word_charFreq.get(k,0):
            inHand = False
    #check if the word is in the word_list
    inWordList = word in word_list
    return inHand & inWordList

def is_valid_wordFast(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    #check if the word is entirely composed of letters in the hand
    inHand = True
    word_charFreq = get_frequency_dict(word)
    for k in word_charFreq.keys():
        if hand.get(k,0) < word_charFreq.get(k,0):
            inHand = False
    #check if the word is in the points_dict
    wordpoint = points_dict.get(word, 0)
    inWordList = (wordpoint > 0)
    return inHand & inWordList

def pick_best_word(hand, points_dict):
    '''
    Return the highest scoring word from points dict that can be made
    with the given hand.
    
    Return '.' if no words can be made with the given hand. 

    This algorithm has complexity O(L) when L is the number of words
    in the dictionary

    '''
    bestWord = ''
    bestScore = 0
    for word in points_dict.keys():
        if is_valid_wordFast(word, hand, points_dict):
            if points_dict[word] > bestScore:
                bestScore = points_dict[word]
                bestWord = word
    if bestScore > 0:
        return bestWord
    else:
        return '.'
                    


def get_time_limit(points_dict, k):
    start_time = time.time()
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k

"""
 Return the time limit for the computer player as a function of the
multiplier k.
 points_dict should be the same dictionary that is created by
get_words_to_points.
"""
# Do some computation. The only purpose of the computation is so we can
# figure out how long your computer takes to perform a known task.



###########
def get_word_rearrangements(word_list):
    '''
Return dictionary mapping a string containing the letters of 
each word in sorted order to the word itself
    
    '''
    rearranged_word = {}
    for word in word_list:
        sortedWord = ''.join(sorted(word))
        rearranged_word[sortedWord] = word
    
    return rearranged_word

def handToString(hand):
    '''
Return a string from all letters in hand arranged alphabetically 
    '''
    stringA = ''
    for letter in hand.keys():
        stringA = stringA + letter*hand[letter]
        
    stringA  = ''.join(sorted(stringA))
    return stringA

    
def pick_best_word_faster(hand, points_dict, rearranged_word):
    
    '''
Return a word with the highest possible score from letters in hand

This algorith has complexity of O(n!) when n is the size of hand??

    '''
    # get all letters from hand, alphabetically arrange them and
    # check if it has any corresponding word in rearranged_word dictionary
    stringHand = handToString(hand)
    wordFound = rearranged_word.get(stringHand, '.')
    
    # base case: hand only has one letter left or we can use all letter
    if (len(stringHand) < 2) | (wordFound != '.') :
        return wordFound
    
    else:
        # recursive: try remove one letter and see if we can form a word
        # get the word with highest score
        maxScore = 0
        wordFound = '.'
        for letter in list(hand.keys()):
            handDel = hand.copy()
            handDel = update_hand(handDel, letter)
            wordd = pick_best_word_faster(handDel,points_dict,rearranged_word)
            pts = points_dict.get(wordd, 0)
            if pts > maxScore:
                maxScore = pts
                wordFound = wordd
        return wordFound
        
    
    
##########

#
# Problem #4: Playing a hand
#
def play_hand(hand, points_dict, arranged_word):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """# TO DO ...
    ##time_limit = float(input("Enter time limit, in seconds, for players: "))
    time_limit = get_time_limit(points_dict, K)
    print('Set time limit to %0.2f' % time_limit)
    
    time_left = time_limit
    totalScore = 0




    # loop until we run out of letter in hand
    while len(hand) > 0:
    
        print("Current Hand: ", end = ' ')
        display_hand(hand)
        print()
        start_time = time.time()

        #*** Choose between two algorithms: pick_best_word VS
        # pick_best_word_faster
        #word = pick_best_word(hand, points_dict)
        word = pick_best_word_faster(hand, points_dict, arranged_word)

        
        print('Enter: ' + word)
        
        end_time = time.time()
        total_time = end_time - start_time + SMALL_TIME
        time_left -= total_time

        # check if we have enough time life
        print('It took %0.2f seconds to provide an answer' % total_time)
        if time_left < 0:
            print('Total time exceeds %0.2f seconds. You scored %0.2f points' % (time_limit, totalScore))
            break
        else:
            print('You have %0.2f seconds remaining.' % time_left)

        # check if the word is correct and update the score    
        if word == '.':
            break   #stop playing if we cannot find any valid word
        if is_valid_wordFast(word, hand, points_dict):
            wordScore = round(get_word_score(word, HAND_SIZE)/total_time,3)
            totalScore += wordScore
            print(word + " earned " + str(wordScore) + " points. Total: " + str(totalScore) + " points")
            update_hand(hand, word)
        else:
            print("Invalid word! Please choose another word.")
    print("Total score: " + str(totalScore)  + " points.")
    
    


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    points_dict =  get_words_to_points(word_list)
    arranged_word = get_word_rearrangements(word_list)
    hand = deal_hand(HAND_SIZE) # random init
    while True:
         cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
         if cmd == 'n':
             hand = deal_hand(HAND_SIZE)
             play_hand(hand.copy(), points_dict, arranged_word)
             print()
         elif cmd == 'r':
             play_hand(hand.copy(), points_dict, arranged_word)
             print()
         elif cmd == 'e':
             break
         else:
             print("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

