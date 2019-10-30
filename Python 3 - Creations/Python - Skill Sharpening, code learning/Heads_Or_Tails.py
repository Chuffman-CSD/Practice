#!/usr/nim/python3
#Chris Huffman
#9/19/19


import random
def hor():
    '''This program finds the side of a quarter with heads or tails'''
    x = 0
    while x == 0:
        sides = [1,0]
        picked_side = (random.choice(sides))
        T = 1
        H = 0
        Enter = input("Enter any numeric key or letter to proceed: ")
        if Enter.isalpha() or Enter.isdigit() or Enter.isalpha() and Enter.isdigit():
            print ("\n")
            if picked_side == (1):
                print ("It was tails! \n")
            elif picked_side == (0):
                print ("It was heads! \n")
hor()
