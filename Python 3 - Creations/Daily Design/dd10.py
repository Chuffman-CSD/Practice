#!/usr/bin/python3
#10/31/19
#Chris Huffman

names = []
while len(names) != 5:
    askNames = input("Enter one name: ").capitalize()
    names.append(askNames)
print(names)
