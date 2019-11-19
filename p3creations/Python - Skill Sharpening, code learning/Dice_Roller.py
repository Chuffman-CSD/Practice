import random
def Dice_Roller():
    x = 0
    while x == 0:
        Dice = [1,2,3,4]
        Random_Dice_Side = (random.choice(Dice))
        print ("\n")
        Enter = input("Enter any key: ")
        if Enter.isdigit or Enter.isalpha() or Enter.isalpha() and Enter.isdigit():
            print ("The side your dice gave you is:",Random_Dice_Side,"\n")
Dice_Roller()
