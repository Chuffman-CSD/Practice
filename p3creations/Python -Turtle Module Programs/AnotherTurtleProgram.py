import turtle as t
d = t.Turtle()
width = 1
d.up()
position = (0,0)
p = position
d.setpos(p)


def Star():
    x = 0
    while x == 0:
        if p != (0,0):
            for i in range(130):
                d.undo()
        else:
            d.width(10)
            x = 1
            d.pendown()
            d.left(60)
            d.forward(450)
            d.right(120)
            d.forward(450)
            d.right(150)
            d.forward(520)
            d.right(150)
            d.forward(450)
            d.right(150)
            d.forward(520)

def Square():
    x = 0
    while x == 0:
        if p != (0,0):
            for i in range(130):
                d.undo()
        else:
            d.width(10)
            x = 1
            d.pendown()
            d.forward(250)
            d.left(90)
            d.forward(250)
            d.left(90)
            d.forward(250)
            d.left(90)
            d.forward(250)
            print ("> > > 'A square has been printed!'\n")

def Rectangle():
    x = 0
    while x == 0:
        if p != (0,0):
            for i in range(20):
                d.undo()
        else:
            d.width(10)
            x = 1
            d.pendown()
            d.forward(750)
            d.left(90)
            d.forward(300)
            d.left(90)
            d.forward(750)
            d.left(90)
            d.forward(300)
            print ("> > > 'A rectangle has been printed!'\n")

def Circle():
    print ("\n")
    def circle_draw():
        print ("\n")
        for i in range(300):
            d.undo()
def cmds():
    x = 0
    while x == 0:
        print ("\n|- - - - COMMANDS - - - - -|\n")
        print ("[1] - 'Say's hi!'\n")
        print ("[2] - 'Draws a 'star'!'\n")
        print ("[3] - 'Draws a 'Square'!'\n")
        print ("[4] - Draws a 'Rectangle'!\n")
        print ("[5] - Draws a 'Circle'!\n")
        print ("[R] - Erases the shape(s) you drew\n")
        usr_sel = input("Select a  shape to make: ").upper()
        if usr_sel == ("1"):
            print ("\n")
            print ("Hi!")
        elif usr_sel == ("2"):
            print ("\n")
            Star()
        elif usr_sel == ("3"):
            print ("\n")
            Square()
        elif usr_sel == ("4"):
            print ("\n")
            d.undo()
            Rectangle()
        elif usr_sel == ("R"):
            print ("\n")
            R()
        else:
            print ("Error")

def R():
    for i in range(500):
        d.undo()


if __name__ == "__main__":
    d.width(10)
    cmds()
wn = t.Screen()
wn.onkeypress(R,"r")
wn = t.mainloop()
