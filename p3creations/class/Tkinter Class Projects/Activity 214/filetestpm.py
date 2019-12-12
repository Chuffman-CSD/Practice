#!/usr/bin/python3
#Chris Huffman
#12/9/19
import pickle

save_path = "./pmsaves/"
save_file = open(save_path + "file1.txt", "w")
fullname = save_file.readlines()

contents = "Here is some stuff to save."
save_file.write(contents)
save_file.write("\n")
save_file.close()


more_contents = "Hey! it's another line!"
save_file = open(save_path + "file1.txt", "a+")
stuff = save_file.read()
print(stuff)
save_file.write(more_contents)
save_file.close()
