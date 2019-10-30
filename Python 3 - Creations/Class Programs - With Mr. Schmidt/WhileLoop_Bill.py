#!/usr/bin/python3
#Chris Huffman
#10/8/19

#Get amounts for a bill from the user

bill_items = []
total_bill = 0
#i = 0

amount = input("Enter in the item amount, 0 to quit: ")
amount = float(amount)
while amount != 0.0:
    bill_items.append(amount)
    # - - - My own added print statement (show's what's happening) - - - 
    print(amount,"added!")
    # - - - My own added print statement (show's what's happening) - - -
    amount = input("Enter in the item amount, 0 to quit: ")
    amount = float(amount)
print(bill_items)

'''
while i < len(bill_items):
    total_bill += bill_items[i]
    i += 1
'''

for i in range(len(bill_items)):
    total_bill += bill_items[i]
    print(1+i,"\t",bill_items[i])

for item in bill_items:
    total_bill += item
    
print("Total Bill:",total_bill)
