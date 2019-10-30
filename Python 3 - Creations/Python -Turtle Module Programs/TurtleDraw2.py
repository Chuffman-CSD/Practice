import turtle as trtl

def Draw():
    x = 0
    while x == 0:
        d = trtl.Turtle()
        Colors = ["Black","Red","Grey","Purple","Green","Yellow","Orange","Pink","Brown","Blue"]
        d = trtl.Turtle()
        d.shape("triangle")
        print ("---------Commands---------- \n")
        print ("C - Commands \n")
        print ("W = Forward \n")
        print ("A = Left \n")
        print ("S = Back \n")
        print ("D = Right \n")
        print ("PU = PenUp \n")
        print ("PD = PenDown \n")
        print ("PC = PenColor 'ColorName' \n")
        print ("CL = Erase canvas \n")
        print ("     - - - Available Colors:")
        print ("           - Black")
        print ("           - Blue")
        print ("           - Red")
        print ("           - Grey")
        print ("           - Purple")
        print ("           - Green")
        print ("           - Yellow")
        print ("           - Orange")
        print ("           - Pink")
        print ("           - Brown \n")
        x = 0
        while x == 0:
            moveTurtle = input("Enter W,A,S or D: ").upper()
            if moveTurtle == ("W"):
                print ("\n")
                d.forward(20)
            elif moveTurtle == ("A"):
                print ("\n")
                d.left(10)
            elif moveTurtle == ("S"):
                print ("\n")
            elif moveTurtle == ("D"):
                print ("\n")
                d.right(10)
            elif moveTurtle == ("PU"):
                print ("\n")
                d.penup()
            elif moveTurtle == ("PD"):
                print ("\n")
                d.pendown()
            elif moveTurtle == ("PC"):
                print ("\n")
                TPC = input("Enter a color: ").capitalize()
                if TPC in Colors:
                    print("\n")
                    d.pencolor(TPC)
                else:
                    print ("\n Enter a valid color \n")
                    Draw()
            elif moveTurtle == ("B"):
                print ("\n")
                d.undo()
            elif moveTurtle == ("C"):
                print ("\n")
                print ("---------Commands---------- \n")
                print ("C - Commands \n")
                print ("W = Forward \n")
                print ("A = Left \n")
                print ("S = Back \n")
                print ("D = Right \n")
                print ("PU = PenUp \n")
                print ("PD = PenDown \n")
                print ("PC = PenColor 'ColorName' \n")
                print ("     - - - Available Colors:")
                print ("           - Black")
                print ("           - Blue")
                print ("           - Red")
                print ("           - Grey")
                print ("           - Purple")
                print ("           - Green")
                print ("           - Yellow")
                print ("           - Orange")
                print ("           - Pink")
                print ("           - Brown \n")
            elif moveTurtle == ("CL"):
                d.clear()
            else:
                print ("\n Enter a valid command \n")
      # - - - - - - - - - - 
    wn = trtl.Screen()
    wn.mainloop()
Draw()
