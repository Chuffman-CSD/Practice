#!/usr/bin/python3
#Chris Huffman
#12/5/19
import random as rd

import tkinter as tk

debug = 0

#aon is amount of numbers
aon = 0

#Counts by 1 if the number is in the thousands
counter = 0

app_proceed = 0

#1
alabama_area_codes = [205, 251, 256, 334, 938]

#2
alaska_area_codes = [907]

#3
arizona_area_codes = [480, 520, 602, 623, 928]

#4
arkansas_area_codes = [479, 501, 870]

#5
california_area_codes = [209, 213, 279, 310, 323, 408, 415, 424, 442, 510, 530, 559, 562, 619, 626, 628, 650, 657, 661, 669, 707, 714, 747, 760, 805, 818, 820, 831, 858, 909, 916, 925, 949, 951]

#6
canada_area_codes = [204, 226, 236, 249, 250, 289, 306, 343, 365, 367, 403, 416, 418, 431, 437, 438, 450, 506, 514, 519, 548, 579, 581, 587, 604, 613, 639, 647, 705, 709, 778, 780, 782, 807, 819, 825, 867, 873, 902, 905]

#7
colorado_area_codes = [303, 719, 720, 970]

#8
connecticut_area_codes = [203, 475, 860, 959]

#9
delaware_area_codes = [302]

#10
florida_area_codes = [239, 305, 321, 352, 386, 407, 561, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954]

#11
georgia_area_codes = [229, 404, 470, 478, 678, 706, 762, 770, 912]

#12
hawaii_area_codes = [808]

#13
idaho_area_codes = [208, 986]

#14                                
illinois_area_codes = [217, 224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847, 872]

#15
indiana_area_codes = [219, 260, 317, 463, 574, 765, 812, 930]

#16
iowa_area_codes = [319, 515, 563, 641, 712]

#17
kansas_area_codes = [316, 620, 785, 913]

#18
kentucky_area_codes = [270, 364, 502, 606, 859]                                                                                        

#19
louisiana_area_codes = [225, 318, 337, 504, 985]

#20
maine_area_codes = [207]

#1
maryland_area_codes = [240, 301, 410, 443, 667]

#22
massachusetts_area_codes = [339, 351, 413, 508, 617, 774, 781, 857, 978]

#23
michigan_area_codes = [231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989]

#24
minnesota_area_codes = [218, 320, 507, 612, 651, 763, 952]

#_25
mississippi_area_codes = [228, 601, 662, 769]

#26
missouri_area_codes = [314, 417, 573, 636, 660, 816]

#27
montana_area_codes = [406]

#28
nebraska_area_codes = [308, 402, 531]

#29
nevada_area_codes = [702, 725, 775]

#30
new_hampshire_area_codes = [603]

#31
new_jersey_area_codes = [201, 551, 609, 640, 732, 848, 856, 862, 908, 973]

#32
new_mexico_area_codes = [505, 575]

#33
new_york_area_codes = [212, 315, 332, 347, 516, 518, 585, 607, 631, 646, 680, 716, 718, 838, 845, 914, 917, 929, 934]

#34
north_carolina_area_codes = [252, 336, 704, 743, 828, 910, 919, 980, 984]

#35
south_carolina_area_codes = [803, 843, 854, 864]

#36
north_dakota_area_codes = [701]

#37
ohio_area_codes = [216, 220, 234, 330, 380, 419, 440, 513, 567, 614, 740, 937]

#38
oklahoma_area_codes = [405, 539, 580, 918]

#39
oregon_area_codes = [458, 503, 541, 971]

#40
pennsylvania_area_codes = [215, 223, 267, 272, 412, 445, 484, 570, 610, 717, 724, 814, 878]

#41
rhode_island_area_codes = [401]

#42
south_dakota_area_codes = [605]

#43
tennessee_area_codes = [423, 615, 629, 731, 865, 901, 931]

#44
texas_area_codes = [210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682, 713, 726, 737, 806, 817, 830, 832, 903, 915, 936, 940, 956, 972, 979]

#45
utah_area_codes = [385, 435, 801]

#46
vermont_area_codes = [802]

#47
virginia_area_codes = [276, 434, 540, 571, 703, 757, 804]

#48
washington_area_codes = [206, 253, 360, 425, 509, 564]

#49
washington_dc_area_codes = [202]

#51
west_virginia_area_codes = [304, 681]

#51
winsconsin_area_codes = [262, 414, 534, 608, 715, 920]

#52
wyoming_area_codes = [307]

def Start():
    global lbl_num_generated
    global ent_state
    global ent_number
    global lbl_info
    proceed.destroy()
    lbl_info.configure(text="\nEnjoy the application!\n", fg = "white")
    root.geometry("307x200")
    #State Label
    ent_state = tk.Entry(text="State: None", font = DEFAULT, width = 30)
    ent_state.configure(fg = "black", background = "white")
    ent_state.grid(column = 0, row = 1)

    #Phone Number Label
    ent_number = tk.Entry(text="Number: None", font = DEFAULT, width = 30)
    ent_number.configure(fg = "black", background = "white")
    ent_number.grid(column = 0, row = 2)

    #Button Generator
    btn_gen_number = tk.Button(text="Random", bg = "green",font = DEFAULT,command = random_numbers)
    btn_gen_number.grid(column = 0, row = 3)

    #Info Label
    lbl_num_generated = tk.Label(text="Numbers Generated: x0", font = DEFAULT)
    lbl_num_generated.configure(background = "black", fg = "white")
    lbl_num_generated.grid(column = 0, row = 4)


def random_numbers():
    global alabama_area_codes
    global debug
    global aon
    aon += 1
    if aon > 1000:
        lbl_num_generated.configure(text="Numbers Generated: x 1k+")
    elif aon < 1000:
        lbl_num_generated.configure(text="Numbers Generated: x" + str(aon))
    #stateStr = "State: Test"
    #lbl_state.insert(0, str(stateStr))
    numGen = rd.randint(1,49)
    debug += 1
    print("Debugging: ","[Random Number: ",numGen,"] Debug Attemps","x",debug,"\n")
    if numGen == 1:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Alabama"
        rdAreaCodes = rd.choice(alabama_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 2:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Alaska"
        rdAreaCodes = rd.choice(alaska_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 3:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Arizona"
        rdAreaCodes = rd.choice(arizona_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 4:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Arkansas"
        rdAreaCodes = rd.choice(arkansas_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 5:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: California"
        rdAreaCodes = rd.choice(california_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 6:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Canada"
        rdAreaCodes = rd.choice(canada_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 7:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Colorado"
        rdAreaCodes = rd.choice(colorado_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 8:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Connecticut"
        rdAreaCodes = rd.choice(connecticut_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 9:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Delaware"
        rdAreaCodes = rd.choice(delaware_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 10:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Florida"
        rdAreaCodes = rd.choice(florida_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 11:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Georgia"
        rdAreaCodes = rd.choice(georgia_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 12:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Hawaii"
        rdAreaCodes = rd.choice(hawaii_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 13:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Idaho"
        rdAreaCodes = rd.choice(idaho_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 14:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Illinois"
        rdAreaCodes = rd.choice(illinois_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 15:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Indiana"
        rdAreaCodes = rd.choice(indiana_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 16:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Iowa"
        rdAreaCodes = rd.choice(iowa_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 17:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Kansas"
        rdAreaCodes = rd.choice(kansas_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 18:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Kentucky"
        rdAreaCodes = rd.choice(kentucky_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 19:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Louisiana"
        rdAreaCodes = rd.choice(louisiana_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 20:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Maine"
        rdAreaCodes = rd.choice(maine_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 21:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Maryland"
        rdAreaCodes = rd.choice(maryland_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 22:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Massachusetts"
        rdAreaCodes = rd.choice(massachusetts_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 23:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Michigan"
        rdAreaCodes = rd.choice(michigan_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 24:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Minnestoa"
        rdAreaCodes = rd.choice(minnesota_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 25:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Mississippi"
        rdAreaCodes = rd.choice(mississippi_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 26:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Missouri"
        rdAreaCodes = rd.choice(missouri_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 27:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Montana"
        rdAreaCodes = rd.choice(montana_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 28:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Nebraska"
        rdAreaCodes = rd.choice(nebraska_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 29:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Nevada"
        rdAreaCodes = rd.choice(nevada_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 30:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: New Hampshire"
        rdAreaCodes = rd.choice(new_hampshire_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 31:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: New Jersey"
        rdAreaCodes = rd.choice(new_jersey_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 32:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: New Mexico"
        rdAreaCodes = rd.choice(new_mexico_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 33:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: New York"
        rdAreaCodes = rd.choice(new_york_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 34:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: North Carolina"
        rdAreaCodes = rd.choice(north_carolina_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 35:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: South Carolina"
        rdAreaCodes = rd.choice(south_carolina_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 36:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: North Dakota"
        rdAreaCodes = rd.choice(north_dakota_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 37:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Ohio"
        rdAreaCodes = rd.choice(ohio_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 38:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Oklahoma"
        rdAreaCodes = rd.choice(oklahoma_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 39:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Oregon"
        rdAreaCodes = rd.choice(oregon_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 40:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Pennsylvania"
        rdAreaCodes = rd.choice(pennsylvania_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 41:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Rhode Island"
        rdAreaCodes = rd.choice(rhode_island_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 42:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: South Dakota"
        rdAreaCodes = rd.choice(south_dakota_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 43:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Tennessee"
        rdAreaCodes = rd.choice(tennessee_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 44:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Texas"
        rdAreaCodes = rd.choice(texas_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 45:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Utah"
        rdAreaCodes = rd.choice(utah_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 46:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Vermont"
        rdAreaCodes = rd.choice(vermont_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 47:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Virginia"
        rdAreaCodes = rd.choice(virginia_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 48:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Washington"
        rdAreaCodes = rd.choice(washington_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 49:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Washington D.C"
        rdAreaCodes = rd.choice(washington_dc_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 50:
        e#Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: West Virginia"
        rdAreaCodes = rd.choice(west_virginia_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 51:
        e#Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Winconsin"
        rdAreaCodes = rd.choice(winconsin_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        
    elif numGen == 52:
        #Confirguartion
        ent_state.delete(0, "end")
        ent_number.delete(0, "end")
        stateStr = "State: Wyoming"
        rdAreaCodes = rd.choice(wyoming_area_codes)
        openParentesis = "("
        closeParenthesis = ")"
        chosenCode = str(openParentesis) + str(rdAreaCodes) + str(closeParenthesis)
        
        rd_FirstThree = rd.randint(111,999)
        str(rd_FirstThree)
        
        rd_LastFour = rd.randint(1000,9999)
        str(rd_LastFour)

        phoneNumber = "Number: " + str(chosenCode) + " - " + str(rd_FirstThree) + " - " + str(rd_LastFour)

        ent_state.insert(0, str(stateStr))
        ent_number.insert(0, str(phoneNumber))
        

DEFAULT = ("Times New Roman", 15)

root = tk.Tk()

root.title("Phone Number Generator")
#root.geometry("315x270")
root.configure(background = "black")

if app_proceed == 0:
    root.geometry("285x210")
    #spacer lbl
    lbl_info = tk.Label(text="\nATTENTION: This application \n is for educational and research \n development use only! If there is \n any abuse of this application we \n are not to be held responsible. \n", font = DEFAULT)
    lbl_info.grid(column = 0, row = 0)
    lbl_info.configure(background = "black", fg = "white")
    proceed = tk.Button(text="Proceed", font = DEFAULT, bg = "green",command = Start)
    proceed.grid(column = 0, row = 1)


root.mainloop()

