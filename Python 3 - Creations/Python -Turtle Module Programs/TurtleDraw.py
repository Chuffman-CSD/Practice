import turtle as trtl
import random

d = trtl.Turtle()
random_turn = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
random_forward = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,20,50]
random_CrazyTurn = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-25,1,2,3,4,5,6,7,8,9,10,20,25] * 2
random_CrazyForward = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-25,1,2,3,4,5,6,7,8,9,10,15,25] * 2
x = 0
while x == 0:
    d.shape("triangle")
    d.forward(0.1 + 0.1)
    d.left(0.9 + 0.1)
    d.forward(0.1 + 0.1)
    d.left(0.2 + 0.1)
    d.forward(0.1 + 0.1)
    d.left(0.2 + 0.1)
    d.forward(0.1 + 0.1)
    d.pencolor("purple")
    d.left(random.choice(random_turn))
    d.forward(random.choice(random_forward))
    d.left(random.choice(random_CrazyTurn))
    d.forward(random.choice(random_CrazyForward))
  # - - - - - - - - - - 
wn = trtl.Screen()
wn.mainloop()
