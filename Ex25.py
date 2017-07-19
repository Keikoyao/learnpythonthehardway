# -- coding: utf-8 --
def break_words(stuff):
    """ This function will break up words for us. """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print (word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)  
    print (word) 

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_words(words)

# code in the PowerShell 
#Notice: for any change you made in the scripts, you have to quit python in the shell and import the script again. 
#To import all the functions in your script use : from ex1 import * 
'''
#under python interactive mode
import ex1
sentence = "All good things come to those who wait."
words = ex1.break_words(sentence)
sorted_words = ex1.sort_words(words)
ex1.print_first_word(words)
ex1.print_last_word(words)
ex1.print_first_and_last(sentence)
ex1.print_first_and_last_sorted(sentence)
'''
#If use (from ex1 import *) then don't need to use ex1.function. 
