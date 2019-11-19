#!/usr/bin/python3
#Chris Huffman
#11/6/19

''' Class Critter, a virtual pet
    The critter has 3 attributes: fitness, happiness and sataitan (hunger).
    the values range from 120 to 0. playing. feeding, and excersising are
    all functions that raise the corresponding attributes by a random value.

    the purpose of the game is to keep the pet alive for as long
    as possible'''
import random as rd


from datetime import datetime 

class Critter(object):
    def __init__(self,name):
        self.name = name
        self.happiness = 120
        self.fitness = 120
        self.satiation = 120
        self.random_feed = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.birthday = datetime.now()
        

    def talk(self):
        msg = "Hi! I'm" + self.name +"!\n"
        msg += " I was born: " + str(self.birthday)
        return msg

    def feed(self):
        self.satiation += rd.randint(1,15)
        if satiation > 120:
            self.satiation = 120
        elif satiation == 120:
            msg = "No, I can't eat anymore i'm stuffed!"
        elif satiation <= 120:
            msg = "Yum! I was fed" + str(self.satiation)
        

if __name__ == "__main__":
    test_critter1 = Critter(" Clarence")
    test_critter2 = Critter(" Martha")
    print(test_critter1.talk())
    print(test_critter2.talk())
    print(test_critter1.feed())
        
