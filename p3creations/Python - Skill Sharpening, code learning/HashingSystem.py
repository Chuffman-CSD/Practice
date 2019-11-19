#!/usr/bin/python3
#Chris Huffman
#10/7/19

not_AllowedWords = ["Retarded","Stupid","Uneducated","Moron","Stupidhead","g1"]
NAW = not_AllowedWords

x = 0
while x == 0:
    tags = 0
    user_text = input("Message: ").capitalize()
    ut = user_text
    if ut in NAW:
        for i in ut:
            if i.isalpha():
                tags += 1
            elif i.isdigit():
                tags += 1
        print("#"*tags)
    else:
        print ("No banned words here")
