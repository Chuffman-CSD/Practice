#!/usr/bin/python3
#Chris Huffman
#10/14/19

import random as rd
number = rd.randint(1,30)
print("The number is:",number)
while number != 12:
    number = rd.randint(1,30)
    print("The number is:",number)
