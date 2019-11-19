#!/usr/bin/python3
#Chris Huffman
#10/4/19


import turtle as t
import random
colors = ["Blue","Black","Red","Green","Yellow","Purple"]
position = (0,0)
p = position
d = t.Turtle()
d.setpos(p)
d.speed("fastest")

def r_key():
    print ("\n")
    print ("lol")
    
x = 0
while x == 0:
    random_size = (1,0.5+10)
    d.pencolor(random.choice(colors))
    d.width(1+random.choice(random_size))
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
    d.right(210*5)
    d.right(210)
    d.right(210+5)
    d.setpos(p)
wn = t.Screen()
wn.onkeypress(r_key,"r")
wn.listen()
wn.mainloop()
