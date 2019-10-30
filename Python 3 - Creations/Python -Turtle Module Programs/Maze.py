#!/usr/bin/python3
# a124_template.py
# Chris Huffman / Matthew Buckmaster
# 9/30/19

""" Make a maze """

#-----import statements-----
import random as rd
import turtle as t
#-----game configuration----]
print ("\nPress 'R' to reset the maze!\n")
rd_pencolor = ["Black","Purple","Green","Red","Yellow","Orange","Blue","Pink"]
walls = 30
width = 20
length = (width * 2)
d = t.Turtle()
d.width(10)
d.hideturtle()
mr = t.Turtle()
mr.color("Red")
mr.pencolor("Red")
mr.up()
mr.setpos(width, width)
mr.down()
mr.color("Red")
#mr.hideturtle()
def up():
    mr.setheading(90)

def down():
    mr.setheading(270)

def left():
    mr.setheading(180)

def right():
    mr.setheading(0)
def fd():
    mr.fd(width)

def r_key():
    walls = 30
    width = 20
    length = (width * 2)
    print ("\nThe maze is resetting!\n")
    for i in range(1000):
        d.undo()
        mr.undo()
    for i in range(walls):
        mr.penup()
        mr.setpos(width,width)
        mr.pendown()
        mr.color("Red")
        mr.pencolor("Red")
        d.hideturtle()
        d.width(10)
        length = length + width
        if i < 4:
            d.speed("fastest")
            d.penup()
            d.forward(length)
            d.left(90)
        else:
            dw = width *2
            door_spot = rd.randrange(dw,length-(dw)+ 1,dw)
            barrier_spot = rd.randrange(dw,length-(dw)+ 1,dw)
            
            if door_spot > barrier_spot:
                d.forward(barrier_spot)
                d.left(90)
                d.fd(width*2)
                d.back(width*2)
                d.right(90)
                d.forward(door_spot - barrier_spot)
                d.penup()
                d.forward(width*2)
                d.pendown()
                d.forward(length - door_spot -(width * 2))
                d.left(90)
            elif barrier_spot > door_spot:
                d.forward(door_spot)
                d.penup()
                d.forward(width*2)
                d.pendown()
                d.forward(barrier_spot - door_spot - dw)
                d.left(90)
                d.fd(width*2)
                d.back(width*2)
                d.right(90)
                d.forward(length - barrier_spot)
                d.left(90)

#-----initialize turtle-----
print ("Welcome to the maze!")
print ("[1] - Random colored maze\n")
print ("[2] - Black Colored Maze\n")
user_sel = input("Select an option: ")
if user_sel == ("1"):
    for i in range(walls):
        mr.color("Red")
        mr.pencolor("Red")
        d.pencolor(rd.choice(rd_pencolor))
        length = length + width
        if i < 4:
            d.speed("fastest")
            d.penup()
            d.forward(length)
            d.left(90)
        else:
            dw = width *2
            door_spot = rd.randrange(dw,length-(dw)+ 1,dw)
            barrier_spot = rd.randrange(dw,length-(dw)+ 1,dw)
                
            if door_spot > barrier_spot:
                d.forward(barrier_spot)
                d.left(90)
                d.fd(width*2)
                d.back(width*2)
                d.right(90)
                d.forward(door_spot - barrier_spot)
                d.penup()
                d.forward(width*2)
                d.pendown()
                d.forward(length - door_spot -(width * 2))
                d.left(90)
            elif barrier_spot > door_spot:
                d.forward(door_spot)
                d.penup()
                d.forward(width*2)
                d.pendown()
                d.forward(barrier_spot - door_spot - dw)
                d.left(90)
                d.fd(width*2)
                d.back(width*2)
                d.right(90)
                d.forward(length - barrier_spot)
                d.left(90)
elif user_sel == ("2"):
    for i in range(walls):
        mr.color("Red")
        mr.pencolor("Red")
        length = length + width
        if i < 4:
            d.speed("fastest")
            d.penup()
            d.forward(length)
            d.left(90)
        else:
            dw = width *2
            door_spot = rd.randrange(dw,length-(dw)+ 1,dw)
            barrier_spot = rd.randrange(dw,length-(dw)+ 1,dw)
          
            if door_spot > barrier_spot:
                d.forward(barrier_spot)
                d.left(90)
                d.fd(width*2)
                d.back(width*2)
                d.right(90)
                d.forward(door_spot - barrier_spot)
                d.penup()
                d.forward(width*2)
                d.pendown()
                d.forward(length - door_spot -(width * 2))
                d.left(90)
            elif barrier_spot > door_spot:
                d.forward(door_spot)
                d.penup()
                d.forward(width*2)
                d.pendown()
                d.forward(barrier_spot - door_spot - dw)
                d.left(90)
                d.fd(width*2)
                d.back(width*2)
                d.right(90)
                d.forward(length - barrier_spot)
                d.left(90)
    else:
        print("\nThat is not an option\n")
            


#-----events-----
wn = t.Screen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(fd,"space")
wn.onkeypress(r_key,"r")
wn.listen()
wn.mainloop()

