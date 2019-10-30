import turtle as t
d = t.Turtle()
width = 20
length = (width * 2)
for i in range(20):
    d.forward(length)
    d.left(90)
    length = length + width
wn = t.Screen()
wn.mainloop()
