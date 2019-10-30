#!/usr/bin/python3
#Chris Huffman
#9/20/19

import socket
import sys
from _thread import *

host = '127.0.0.1'
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host,port))
    print ("\nSuccessfully connected!","Host:",host,"Port:",port,"\n")
    #i = input("Enter a message: ")

    #s.send(i):
    disconnect = ["--Exit","--Logout","--Leave","--esc"]
    i = input("Send a message: ")
    i = "".encode()
    i = b""
except socket.error as e:
    print (str(e))

#i = input("Enter a message: ")

#s.send(i)
