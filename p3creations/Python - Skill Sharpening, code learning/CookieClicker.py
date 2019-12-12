#!/usr/bin/python3
#Chris Huffman
#11/26/19

import tkinter as tk

score = 0

def score_adder():
    global score
    score += 1
    print(score)

root = tk.Tk()

frame = tk.Frame()

default = ('Times New Roman',16)

root.title("Cookie Clicker v-1.0")
root.geometry("350x350")

cookie_frame = tk.Frame(root)
cookie_frame.grid(row = 0, column = 0, sticky = "news")

lbl_test = tk.Label(cookie_frame,text="Cookie Clicker", font = default)
lbl_test.grid(row = 0, column = 0)

btn_test = tk.Button(cookie_frame, text="Click Me!",bg = "green", font = default,command=score_adder)
btn_test.grid(row = 1, column = 0)


root.mainloop()
