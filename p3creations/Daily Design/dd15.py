#!/usr/bin/python3
#Chris Huffman
#12/5/19

'''This program is for the daily design, using a library to look through items and print out the items associated with them'''

phonebook = {'James':['555-1234'],'Courtney':['555-4398'],'Alvin':['555-9276'],'Kim':['555-7859']}

# -- debug using a while loop if I spell a name wrong
x = 0
while x == 0:
    name = input("Enter a name: ").capitalize()
    if name in phonebook:

        #If I spell a name right, the loop stops
        x = 1
        print(phonebook[name])
    elif name not in phonebook:
        print("\nThe name was not found\n")


''' Another Way to do it with .keys()

# -- debug using a while loop if I spell a name wrong
x = 0
while x == 0:
    name = input("Enter a name: ").capitalize()
    if name in phonebook.keys():

        #If I spell a name right, the loop stops
        x = 1
        print(phonebook[name])
    elif name not in phonebook.keys():
        print("\nThe name was not found\n")

'''
