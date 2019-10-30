#!/usr/bin/python3
#Chris Huffman
#9/26/19

def TextUpgrade():
    #Is the goal you have to beat
    Goal = 10000000
    #Are your total Point(s)
    Points = 10000
    #Is your total Score
    Score = 0
    #For every set number of messages, add +1 Point
    Message_Counter = 0
    #Holds the upgrades for: Points
    Upgrade_Points = 0
    #Holds the upgrades for: Score
    Upgrade_Score = 0
    #Holds the upgrades for: Message_Counter
    UMC = 0
    x = 0
    while x == 0:
        usrsel_g = input("Enter a command:").upper()
        if usrsel_g == ("") and Message_Counter < 30 and Upgrade_Points == 0 and Upgrade_Score == 0 and UMC == 0:
            Score += 1
            Message_Counter += +1
            print("\nScore: + 1\n")
        elif usrsel_g == ("") and Message_Counter == 30 and Upgrade_Points == 0 and Upgrade_Score == 0 and UMC == 0:
            Message_Counter = Message_Counter * 0
            Points += 1
            Score += 1
            print("\nScore: + 1\n")
            print("\nPoints: + 1\n")
        elif usrsel_g == ("") and Message_Counter < 30 and Upgrade_Points == 0 and Upgrade_Score == 1 and UMC == 0:
            print ("\n")
            Score += 5
            print("\nScore: + 5\n")
        elif usrsel_g == ("") and Message_Counter < 30 and Upgrade_Points == 0 and Upgrade_Score == 2 and UMC == 0:
            print ("\n")
            Score += 15
            Message_Counter +=1
            print("\nScore: + 15\n")
        elif usrsel_g == ("") and Message_Counter == 30 and Upgrade_Points == 0 and Upgrade_Score == 2 and UMC == 0:
            print ("\n")
            Message_Counter = Message_Counter * 0
            Score += 15
            Points += +1
            print("\nScore: + 15\n")
            print ("\nPoints: +1\n")
        elif usrsel_g == ("") and Message_Counter < 30 and Upgrade_Points == 0 and Upgrade_Score == 3 and UMC == 0:
            print ("\n")
            Score += 15
            print("\nScore: + 25\n")
        elif usrsel_g == ("") and Message_Counter == 30 and Upgrade_Points == 0 and Upgrade_Score == 3 and UMC == 0:
            print ("\n")
            Message_Counter = Message_Counter * 0
            Score += 15
            Points += +1
            print("\nScore: + 25\n")
            print ("\nPoints: +1\n")
        elif usrsel_g == ("C"):
            CMDS()
        elif usrsel_g == ("P"):
            print("\nTotal Points:",Points,"\n")
        elif usrsel_g == ("G"):
            print ("\nTotal Progress:",Score,"/",Goal,"\n")
        elif usrsel_g == ("SU") and Upgrade_Score == 0:
            SU1()
            usrsel_su = input("Select an upgrade: ")
            if usrsel_su == ("1") and Upgrade_Score == 0 and Points >= 25:
                Upgrade_Score +=1
                Points -= 25
                print ("\nGiven the ability to +5 score\n")
                print("\n",Upgrade_Score,"\n")
            elif usrsel_su == ("1") and Upgrade_Score == 0 and Points < 25:
                print ("\nYou need 25 points, you currently have",Points,"!\n")
            elif usrsel_su == ("1") and Upgrade_Score == 1:
                print ("\n")
            else:
                print("\nThat is not a valid command!\n")
        elif usrsel_g == ("SU") and Upgrade_Score == 1:
            SU2()
            usrsel_su = input("Select an upgrade: ")
            if usrsel_su == ("1") and Upgrade_Score == 1 and Points >= 50:
                # - - - When you buy something it deducts 50 points - - -
                Upgrade_Score +=1
                Points -=50
                print ("\nGiven the ability to +15 score\n")
                print("\n",Upgrade_Score,"\n")
            else:
                print ("\nThat is not a valid command!\n")
            #elif usrsel_su == ("1") and Upgrade_Score == 0 and Points < 50:
                #print ("\nYou need 50 points, you currently have",Points,"!\n")
            #elif usrsel_su == ("1") and Upgrade_Score == 1:
                # - - - Does nothing - - -
                #print ("\n")
            #else:
                #print("\nThat is not a valid command!\n")
        elif usrsel_g == ("SU") and Upgrade_Score == 3:
             SU3()
            usrsel_su = input("Select an upgrade: ")
            if usrsel_su == ("1") and Upgrade_Score == 0 and Points >= 25:
                Upgrade_Score +=1
                Points -= 25
                print ("\nGiven the ability to +5 score\n")
                print("\n",Upgrade_Score,"\n")
            elif usrsel_su == ("1") and Upgrade_Score == 0 and Points < 25:
                print ("\nYou need 25 points, you currently have",Points,"!\n")
            elif usrsel_su == ("1") and Upgrade_Score == 1:
                print ("\n")
            else:
                print("\nThat is not a valid command!\n")

def CMDS():
    print ("\n| -------- GAME COMMANDS --------  |")
    print ("| [C] - Commands                   |")
    print ("| [P] - Points                     |")
    print ("| [G] - Show's progress            |")
    print ("| [EmptySpace]  - Add Points/Score |")
    print ("| [SU] - Score upgrade            |\n")

def SU1():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 5 / Cost: 25 Points \n")

def SU2():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 15 / Cost: 50 Points \n")

def SU3():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 25 / Cost: 75 Points \n")

def SU4():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 40 / Cost: 90 Points \n")

def SU5():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 65 / Cost: 105 Points \n")

def SU6():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 80 / Cost: 130 Points \n")

def SU7():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 100 / Cost: 160 Points \n")

def SU8():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 120 / Cost: 190 Points \n")

def SU9():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 150 / Cost: 220 Points \n")

def SU10():
    print ("\n | -------- Score Upgrade -------- | \n")
    print (" | [1] - Effect: Score + 200 / Cost: 260 Points \n")

def PU():
    print ("Test")
if __name__ == "__main__":
    CMDS()
    TextUpgrade()
