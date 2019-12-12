#!/usr/bin/python3
#Chris Huffman
#11-19-19

import random as rd

def code_lock():
    combination = rd.randint(0000,9999)
    print("\nGuess the four digit combination!\n")
    combination = str(combination)
    combination.split()
    print("----")
    sequence = [0,0,0,0]
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    x = 0
    while x == 0:
        guess = input("\nGuess the number: ")
        if guess == "":
            print("\nThat is obviously wrong...\n")
        elif guess == combination:
            x = 1
            print("\nCode Discovered:",sequence,"\n")
            print("You guessed it!\n")
        elif combination[0] in guess:
            print("\nTest complete - is number 1\n")
            print("----\n")
            #print(sequence[0],sequence[1],sequence[2],sequence[3])
            sequence[0] = combination[0]
            print("Code Undiscovered:",sequence)
        elif combination[1] in guess:
            print("\nTest complete - is number 2\n")
            print("----\n")
            #print(sequence[0],sequence[1],sequence[2],sequence[3])
            sequence[1] = combination[1]
            print("Code Undiscovered:",sequence)
        elif combination[2] in guess:
            print("\nTest complete - is number 3\n")
            print("----\n")
            #print(sequence[0],sequence[1],sequence[2],sequence[3])
            sequence[2] = combination[2]
            print("Code Undiscovered:",sequence)
        elif combination[3] in guess:
            print("\nTest complete - is number 4\n")
            print("----\n")
            #print(sequence[0],sequence[1],sequence[2],sequence[3])
            sequence[3] = combination[3]
            print("Code Undiscovered:",sequence)
        else:
            print("\nSorry, that number is not in the combination!\n")
    x = 0
    while x == 0:
        replay = input("Would you like to play again? [Y]/[N]: ").upper()
        if replay == ("Y"):
            x = 1
            print("\nOkay!\n")
            print("\n- - - - - Scrambling numbers - - - - -\n")
            code_lock()
        elif replay == ("N"):
            x = 1
            print("\nGoodbye!\n")
        else:
            print("\nEnter Yes or No\n")

if __name__ == "__main__":
    code_lock()
