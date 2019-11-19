#!/usr/bin/python3
#Chris Huffman / Gentry Cross
#9/18/19

'''The purpose of this program is for class'''

pn = input("Enter a positive number: ")
number = int(pn)
print ("Your number is", number)
doubled = number ** 2
print ("Your number doubled is", doubled)
negative = number * -1
print ("Your number as a negative is", negative)
squared = doubled ** 2
print ("Your number squared is", squared)
triple = doubled ** 3
print ("Your number tripled is", triple)
total = number + doubled + negative + squared + triple
print ("Your total is", total)
