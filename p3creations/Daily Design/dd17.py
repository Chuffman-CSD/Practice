#!/usr/bin/python3
#Chris Huffman
#12/11/19

num1 = 0
num2 = 0

number = input("Enter your first number: ")
num1 = number

number = input("Enter your second number: ")
num2 = number

try:
    sum = int(num1) / int(num2)
    print("Result: ",sum)
except:
    print("\nError Cannot divide by zero: What a Terrible Fail\n")
    
