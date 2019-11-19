import turtle as t

def add_key():
    sum=1+1
    print(sum)
    wn.onkeypress(add_key,"r")



wn = t.Screen()
wn.onkeypress(add_key,"r")
wn = t.mainloop()
