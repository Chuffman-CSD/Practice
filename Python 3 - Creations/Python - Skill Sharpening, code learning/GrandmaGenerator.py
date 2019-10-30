#!/usr/bin/python3
#Chris Huffman
#10/7/19

import random as rd
""" This program generates you a grandma and her age """
def gen_grandma_name():
    grandma_Names = ["Edna","Caroline","Sophie","Liz","Emilia","Gma","Gran","Gigi","Big-G"]
    g_Name = (rd.choice(grandma_Names))
    print ("\nYour grandma will be called:",g_Name,"\n")
def gen_grandma_age():
    pass

if __name__ == "__main__":
    gen_grandma_name()
