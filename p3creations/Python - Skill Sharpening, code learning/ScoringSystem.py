import random
def Main():
    x = 0
    while x == 0:
        User_Input = input("Press Enter to generate a random score / 2: ")
        if User_Input.isalpha() or User_Input.isdigit() or User_Input.isdigit() and User_Input.isalpha() or User_Input == (""):
            x = 1
            print ("\n")
            Score = 0
            Random_Point_Giver = [2,6,8,10,12,14,16]
            Added_Bonus = [2,4,6,8,10,12]
            Point = (random.choice(Random_Point_Giver))
            print ("Example points:",Point)
            print ("\n")
            Total_Bonus = (random.choice(Added_Bonus))
            print ("Example Bonus Points:",Total_Bonus)
            print ("\n")
            print ("Example Points + Bonus Points divided by 2 \n")
            Score = Score + Point + Total_Bonus * 1 / 2
            print (Score)
            print ("\n")
            Main()
        else:
            print ("\n")
            print ("Please select an available option.")
            print ("\n")
Main()
