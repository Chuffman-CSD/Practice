print ("                  -                  -  o       o       ")
print ("                  -                  -    o   o         ")
print ("                  -                  -      O           ")
print ("                  -                  -    o   o         ")
print ("                  -                  -  o       o       ")
print ("--------------------------------------------------------")
print ("                  -    o       o     -                  ")
print ("                  -      o   o       -                  ")
print ("                  -        O         -                  ")
print ("                  -      o   o       -                  ")
print ("                  -    o       o     -                  ")
print ("--------------------------------------------------------")
print ("     oooooo       -                  -                  ")
print ("    o      o      -                  -                  ")
print ("   o        o     -                  -                  ")
print ("    o      o      -                  -                  ")
print ("     oooooo       -                  -                  ")
def Tic_Tac():
    print ("\n")
    print ("Welcome to the Tic-Tac-Toe texted based game!")
    print ("\n")
    x = 0
    while x == 0:
        User_Selection = input("Would you like to be X's or O's [X]/[O]: ").upper()
        if User_Selection == ("X"):
            print ("\n")
            def X_Game():
                x = 1
                Player = ("X")
                Computer = ("O")
                if Player == ("X") and Computer == ("O"):
                    print ("Welcome to the game, your symbol is now set to [X] and the computer is [O]")
                    print ("\n")
                else:
                    x = 1
                    print ("There was an error with the code, please contact the creator")
            X_Game()
        elif User_Selection == ("O"):
            x = 1
            print ("\n")
            def O_Game():
                Player = ("O")
                Computer = ("X")
                if Player == ("O") and Computer == ("X"):
                    print ("Welcome to the game, your symbol is now set to [X] and the computer is [O]")
                    print ("\n")
                else:
                    x = 1
                    print ("There was an error with the code, please contact the creator")
            O_Game()
        else:
            print ("\n")
            print ("Please enter eithr letters [X] or [O].")
            print ("\n")
Tic_Tac()
