#!/usr/bin/python3
#Chris Huffman
#11-20-19

import random as rd
import time
end = ""
for i in range(50):
    time.sleep(0.2)
    num1 = rd.randint(1,25)
    num2 = rd.randint(1,50)
    if num1 == 25:
        print("="*num2)
        print("-"*num2)
    elif num1 < 25:
        print("="*num1)
        print("-"*num1)
