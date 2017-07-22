# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

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
    print("  " +  str(len(wordlist)) +  " words loaded.")
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


# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.

# TO DO: your code begins here!
def prefCheck(wordFrag, word):
    #check if word  begins with wordFrag
    if len(word) < len(wordFrag):
        return False
    else:
        return word[0:len(wordFrag)] == wordFrag
    
def prefCheckList(wordFrag, wordList):
    prefResult = [prefCheck(wordFrag, x) for x in wordList]
    return True in prefResult
    

def play_ghost(wordlist):
    print("Welcome to Ghost!")
    wordFrag = ''
    while True:
        print("Player 1's turn.")
        print("Current word fragment: " + wordFrag)
        p1input = input("Player 1 says letter: ")
        while (p1input in string.ascii_letters) == False:
            print("invalid input!!")
            p1input = input("Player 1 says letter: ")
        wordFrag = wordFrag + p1input
        wordFrag = wordFrag.lower()

        if (wordFrag in wordlist) & (len(wordFrag) > 3):
            print("Player 1 loses because " + wordFrag + " is a word!")
            print("Player 2 wins!")
            break
        if prefCheckList(wordFrag, wordlist) == False:
            print("Player 1 loses because no word begins with " + wordFrag)
            print("Player 2 wins!")
            break
        print()
        
        print("Player 2's turn.")
        print("Current word fragment: " + wordFrag)
        p2input = input("Player 2 says letter: ")
        while (p1input in string.ascii_letters) == False:
            print("invalid input!!")
            p1input = input("Player 2 says letter: ")
        wordFrag = wordFrag + p2input
        wordFrag = wordFrag.lower()
        if (wordFrag in wordlist) & (len(wordFrag) > 3) :
            print("Player 2 loses because " + wordFrag + " is a word!")
            print("Player 1 wins!")
            break
        if prefCheckList(wordFrag, wordlist) == False:
            print("Player 2 loses because no word begins with " + wordFrag)
            print("Player 1 wins!")
            break
        print()            
        
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_ghost(word_list)
