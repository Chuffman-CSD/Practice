#!/usr/bin/python3
#Chris Huffman
#10/7/19

""" This progam will keep a score in the python turtle module """
import turtle as t
#Position of the turtle that draws the score
position_1 = (500,0)
p1 = position_1

position_2 = (-500,0)
p2 = position_2

#Draws the actual score
d = t.Turtle()
d.penup()
d.setpos(p1)
d.left(90)
#d.hideturtle()

#Draws the scoring label
sd = t.Turtle()
sd.penup()
sd.setpos(p2)
sd.left(90)
#sd.hideturtle()



wn = t.Screen()
wn = t.mainloop()
