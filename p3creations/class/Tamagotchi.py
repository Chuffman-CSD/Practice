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
from Faces2 import *


from datetime import datetime 

class Critter(object):
    def __init__(self,name):
        self.name = name
        self.happiness = 120
        self.fitness = 120
        self.satiation = 120
        self.birthday = datetime.now()
        

    def talk(self):
        msg = " Hi! I'm" + self.name +"!\n"
        msg += " I was born: " + str(self.birthday.date()) + "\n"
        msg += " Happiness Score: " + str(self.happiness) + "\n"
        msg += " Fitness Score: " + str(self.fitness) + "\n"
        msg += " Satiation Score: " + str(self.fitness) +"\n"
        print(msg)


    def feed(self):
        self.satiation += rd.randint(1,15)
        msg = ""
        if self.satiation > 120:
            self.satiation = 120
            msg = """\nNo, I can't eat anymore i'm stuffed!"""
        elif self.satiation == 120:
            msg = "No, I can't eat anymore i'm stuffed!"
        elif self.satiation <= 120:
            msg = "Yum! I was fed" + str(self.satiation)
        print(msg)


    def exercise(self):
        self.fitness += rd.randint(1,15)
        print("Let's get this bread")
        if self.fitness > 120:
            self.fitness = 120
            msg = """\nNo, i'm exausted!"""

            
    def play(self):
        self.happiness += rd.randint(1,15)
        msg = "Come on, Donkehy"
        if self.happiness > 120:
            self.happiness = 120
        print(msg)

        
    def slow_death(self):
        '''randomly lower's each attribute from (1,5) inclusive'''

        self.happiness -= rd.randint(1,5)
        self.satiation -= rd.randint(1,5)
        self.fitness -= rd.randint(1,5)
        
if __name__ == "__main__":
    critter_happy()
    test_critter = Critter(" Shrek")
    test_critter.talk()
    test_critter.slow_death()
    test_critter.play()
    test_critter.talk()
