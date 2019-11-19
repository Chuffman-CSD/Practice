#!/usr/bin/python3
#Chris Huffman
#9/26/19


def LearnPy():
    print("\nWelcome, here you will learn coding in Python!\n")
    print("\n[1] - Table of Contents\n")
    print("\n[2] - Begin Learning!\n\n")
    x = 0
    while x == 0:
        StartIn = input("Enter a numeric response: ")
        if StartIn.isalpha():
            print("\n")
        elif StartIn.isdigit():
            print("\n")
        else:
            print("\nEnter a valid command\n")

def TOC():
    print("\n[1] - Starting Out")



#Main Section
if __name__ == "__main__":
    LearnPy()
