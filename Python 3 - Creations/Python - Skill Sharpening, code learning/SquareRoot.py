#!/usr/bin/python3
#Chris Huffman
#9/23/19

''' Demonstarte Square Root '''
def sqr_root(num):
    return num ** 0.5

#Main Section

number = input("Enter a positive number: ")
number = int(number)

square_root = sqr_root(number)
print(square_root)
