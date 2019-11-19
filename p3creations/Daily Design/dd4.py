#!/usr/bin/python3
#Chris Huffman
#9/26/19

'''This is a program that prints a number 1-50 until a certain condition is met
    I sort of went overboard on this'''

def dice_d4():
    num_count = 50
    num = 0
    print ("\nPrinting numbers 1-50\n")
    x = 0
    while x == 0:
        if num_count == 50:
            for i in range(50):
                num_count = num_count -1
                num = num + 1
                print ("\n",num,"\n")
        elif num_count == 0:
            x = 1
            print ("\nGoodbye!\n")
if __name__ == "__main__":
    dice_d4()
