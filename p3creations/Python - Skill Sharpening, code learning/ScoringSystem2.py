import random as rd
import time
# - configuration
Score = 0
Total = 0
Level = 0
XpNeeded = 100
xp = 0

# - loop / gameplay
x = 0
while x == 0:
    num = rd.randint(1,50)
    if num % 2 == 0:
        Score += num / 2
        print("Score Added: ",Score,"\n")
        time.sleep(0.3)
        Total += Score + 1
        print("Total: ",Total,"\n")
        time.sleep(0.3)
        if xp == XpNeeded:
            level += 1
            xp -= xp
            print("\Level up!\n")
            print("New Level: ",Level,"\n")
        elif xp > XpNeeded:
            xp -= XpNeeded
            print("\nLevel up!\n")
            print("New Level: ",Level,"\n")
    elif num % 2 == 1:
        Score += num /1
        print("Score Added: ",Score,"\n")
        time.sleep(0.3)
        Total += Score + 2
        print("Total: ",Total,"\n")
        time.sleep(0.3)
        if xp == XpNeeded:
            level += 1
            xp -= xp
            print("\Level up!\n")
            print("New Level: ",Level,"\n")
        elif xp > XpNeeded:
            xp -= XpNeeded
            print("\nLevel up!\n")
            print("New Level: ",Level,"\n")
