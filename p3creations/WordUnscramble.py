#!/busr/bin/python3
#10/30/19
#Chris Huffman


import random as rd

def Unscrambler():
    Score = 0
    Words = ["Bad","Dad","Mad","Funny","Help","Anger","Computer","Key","Keyboard","Phone"]
    Selected_Word = rd.choice(Words)
    SL = Selected_Word
    print (SL)
    print (SL[1])
    print (SL[2])
    print (SL[3])
    print (SL[4])
    
        







if __name__ == "__main__":
    print("|| Python Word Unscramble ||")
    Unscrambler()
