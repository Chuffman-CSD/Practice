import turtle as t
d = t.Turtle()
def up_arrow():
    d.setheading(90)
def down_arrow():
    d.setheading(270)
def left_arrow():
    d.setheading(180)
def right_arrow():
    d.setheading(0)
def space_button():
    d.forward(10)
def erase_all():
    for i in range(1000):
        d.undo()

if __name__ == "__main__":
    d.forward(1)
wn = t.Screen()
wn.onkeypress(up_arrow,"Up")
wn.onkeypress(down_arrow,"Down")
wn.onkeypress(left_arrow,"Left")
wn.onkeypress(right_arrow,"Right")
wn.onkeypress(space_button,"space")
wn.onkeypress(erase_all,"r")
wn.listen()
wn = t.mainloop()
