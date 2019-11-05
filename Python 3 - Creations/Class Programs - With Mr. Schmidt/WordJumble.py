#!/usr/bin/python3\
#Chris Huffman
#11/4/19
import random as rd

'''Word Jumble

   This is a game that randomly selects a word from a word bank and
   scrambles it so that the user had to unscramble the word and guess
   the correct word.'''

def welcome():
    print("""                       ==========================
                      || Welcome to Word Jumble ||
                       ==========================
                         Guess the word in as
                        few moves as possible!
                        """)

def scrambler(word):
    temp = list(word)
    rd.shuffle(temp)
    return ''.join(temp)


if __name__ == "__main__":
    word_bank = ["yellow","bullseye","python","super","creeper","semiautomatically","schmidt","csd","apt","sudo","get","install","computer","pc","program","money","hunger"]
    word = word_bank[rd.randrange(len(word_bank))]
    jumble = scrambler(word)
    welcome()
    print("Here is your jumbled word:\n")
    print("Jumbled word:",scrambler(jumble))
    is_not_correct = True
    tries = 0
    while is_not_correct == True:
        print("\n")
        guess = input("Your guess: ")
        tries += 1
        if guess == word:
            print("You got it! It took you",tries,"guesses!")
            
            is_not_correct = False
        else:
            print("Nope!")
