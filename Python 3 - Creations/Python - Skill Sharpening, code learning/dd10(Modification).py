#!/usr/bin/python3
#10/31/19
#Chris Huffman

names = []
nameIntValue = 0
namesNeeded = 5
print("\nFor each input, enter exactly one name. ")
while nameIntValue != 5 and namesNeeded != 0:
   print("\nYou need",namesNeeded,"more names.\n")
   askNames = input("Enter one name: ").capitalize()
   names.append(askNames)
   nameIntValue += 1
   namesNeeded -= 1
print ("\nNames in the list: ",names)
