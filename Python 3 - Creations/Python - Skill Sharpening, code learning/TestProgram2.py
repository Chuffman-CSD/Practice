#1/usr/bin/python3
#Chris Huffman
#9/10/19


import random
def d_R():
    dice1 = [1,2,3,4,5,6]
    random_Dice1 = (random.choice(dice1))
    print ("\n welcome to dice roller! \n")
    roll_Dice = input("Enter the amount of times you wish to roll: ")
    if roll_Dice.isalpha():
        print (" ")
    elif roll_Dice.isDigit() and len(roll_Dice) <= 4 and roll_Dice <= 4:
        int(roll_Dice)
        for i in (roll_Dice):
            print (random_Dice1)
            
d_R()
