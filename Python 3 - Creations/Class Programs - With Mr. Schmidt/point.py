#!/usr/bin/python3
#Chris Huffman
#11/5/19

''' point.py is a program that will make a cartesian graph'''

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        msg = "(" + str(self.x) + " , "
        msg += str(self.y) + ")"
        return msg
        

if __name__ == "__main__":
    test_point = Point(4,6)
    print(test_point)
