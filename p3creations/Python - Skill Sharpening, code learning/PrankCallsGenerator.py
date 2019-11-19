#!/usr/bin/python3
#Chris Huffman
#11/13/19

import random as rd

def phone_number_generator():

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

    x = 0
    while x == 0:
        phone_numbers = input("How many phone numbers would you like generat?, 'q' to quit: ").upper()
        if phone_numbers == "Q":
            x = 1
        else:
            phone_numbers = int(phone_numbers)
            if phone_numbers <= 20:
                x = 1
                loop_again = 0
                print("Generating phone numbers...\n")
                for i in range(phone_numbers):
                    loop_again += 1
                    first_three = rd.randint(100,999)
                    last_four = rd.randint(1000,9999)
                    pick_places = rd.randint(0,53)
                    if pick_places == 1:
                        Alabama = rd.choice(alabama_area_codes)
                        print("\nAlabama")
                        print("(",Alabama,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 2:
                        Alaska = rd.choice(alaska_area_codes)
                        print("\nAlaska")
                        print("(",Alaska,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 3:
                        Arkansas = rd.choice(arkansas_area_codes)
                        print("\nArkansas")
                        print("(",Arkansas,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 4:
                        California = rd.choice(california_area_codes)
                        print("\nCalirofnia")
                        print("(",California,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 5:
                        Colorado = rd.choice(colorado_area_codes)
                        print("\nColorado")
                        print("(",Colorado,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 6:
                        Canada = rd.choice(canada_area_codes)
                        print("\nCanada")
                        print("(",Canada,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 7:
                        Connecticut = rd.choice(connecticut_area_codes)
                        print("\nConnecticut")
                        print("(",Connecticut,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 8:
                        Delaware = rd.choice(delaware_area_codes)
                        print("\nDelaware")
                        print("(",Delaware,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 9:
                        Florida = rd.choice(florida_area_codes)
                        print("\nFlorida")
                        print("(",Florida,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 10:
                        Georgia = rd.choice(georgia_area_codes)
                        print("\nGeordia")
                        print("(",Georgia,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 11:
                        Hawaii = rd.choice(hawaii_area_codes)
                        print("\nHawaii")
                        print("(",Hawaii,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 12:
                        Idaho = rd.choice(idaho_area_codes)
                        print("\nIdaho")
                        print("(",Idaho,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 13:
                        Illinois = rd.choice(illinois_area_codes)
                        print("\nIllinois")
                        print("(",Illinois,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 14:
                        Indiana = rd.choice(indiana_area_codes)
                        print("\nIndiana")
                        print("(",Indiana,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 15:
                        Iowa = rd.choice(iowa_area_codes)
                        print("\nIowa")
                        print("(",Iowa,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 16:
                        Kansas = rd.choice(kansas_area_codes)
                        print("\nKansas")
                        print("(",Kansas,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 17:
                        Kentucky = rd.choice(kentucky_area_codes)
                        print("\nKentucky")
                        print("(",Kentucky,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 18:
                        Louisiana = rd.choice(louisiana_area_codes)
                        print("\nLouisiana")
                        print("(",Louisiana,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 19:
                        Maine = rd.choice(maine_area_codes)
                        print("\nMaine")
                        print("(",Maine,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 20:
                        Maryland = rd.choice(maryland_area_codes)
                        print("\nMaryland")
                        print("(",Maryland,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 21:
                        Massachusetts = rd.choice(massachusetts_area_codes)
                        print("\nMassachusetts")
                        print("(",Massachusetts,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 22:
                        Michigan = rd.choice(michigan_area_codes)
                        print("\nMichigan")
                        print("(",Michigan,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 23:
                        Minnesota = rd.choice(minnesota_area_codes)
                        print("\nMinnesota")
                        print("\n",Minnesota," - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 24:
                        Mississippi = rd.choice(mississippi_area_codes)
                        print("\Mississippi")
                        print("(",Mississippi,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 25:
                        Missouri = rd.choice(missouri_area_codes)
                        print("\nMissouri")
                        print("(",Missouri,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 26:
                        Montana = rd.choice(montana_area_codes)
                        print("\nMontana")
                        print("(",Montana,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 27:
                        Nebraska = rd.choice(nebraska_area_codes)
                        print("\nNebraska")
                        print("(",Nebraska,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 28:
                        Nevada = rd.choice(nevada_area_codes)
                        print("\nNevada")
                        print("(",Nevada,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 29:
                        New_Hampshire = rd.choice(new_hampshire_area_codes)
                        print("\nNew Hampshire")
                        print("(",New_Hampshire,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 30:
                        New_Jersey = rd.choice(new_jersey_area_codes)
                        print("\nNew Jersey")
                        print("(",New_Jersey,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 31:
                        New_Mexico = rd.choice(new_mexico_area_codes)
                        print("\nNew Mexico")
                        print("(",New_Mexico,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 32:
                        North_Carolina = rd.choice(north_carolina_area_codes)
                        print("\nNorth Carolina\n")
                        print("(",North_Carolina,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 33:
                        South_Carolina = rd.choice(south_carolina_area_codes)
                        print("\nSouth Carolina")
                        print("(",South_Carolina,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 34:
                        Ohio = rd.choice(ohio_area_codes)
                        print("\nOhio")
                        print("(",Ohio,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 35:
                        Oklahoma = rd.choice(oklahoma_area_codes)
                        print("\nOklahoma")
                        print("(",Oklahoma,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 36:
                        Oregon = rd.choice(oregon_area_codes)
                        print("\nOregon")
                        print("(",Oregon,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 37:
                        Rhode_Island = rd.choice(rhode_island_area_codes)
                        print("\nRhode Island")
                        print("(",Rhode_Island,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 38:
                        South_Dakota = rd.choice(south_dakota_area_codes)
                        print("\nSouth Dakota")
                        print("(",South_Dakota,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 39:
                        Tennessee = rd.choice(tennessee_area_codes)
                        print("\nTennessee")
                        print("(",Tennessee,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 40:
                        Texas = rd.choice(texas_area_codes)
                        print("\nTexas")
                        print("(",Texas,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 41:
                        Utah = rd.choice(utah_area_codes)
                        print("\nUtah")
                        print("(",Utah,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 42:
                        Vermont = rd.choice(vermont_area_codes)
                        print("\nVermont")
                        print("\n",Vermont,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 43:
                        Virginia = rd.choice(virginia_area_codes)
                        print("\nVirginia")
                        print("(",Virginia,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 44:
                        Washington = rd.choice(washington_area_codes)
                        print("\nWashington")
                        print("(",Washington,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 45:
                        Washington_DC = rd.choice(washington_dc_area_codes)
                        print("\nWashington DC")
                        print("(",Washington_DC,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 45:
                        West_Virginia = rd.choice(west_virginia_area_codes)
                        print("\nWest Virginia")
                        print("(",West_Virginia,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 47:
                        Winsconsin = rd.choice(winsconsin_area_codes)
                        print("\nWinsconsin")
                        print("(",Winsconsin,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 48:
                        Wyoming = rd.choice(wyoming_area_codes)
                        print("\nWyoming")
                        print("(",Wyoming,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 49:
                        New_York = rd.choice(new_york_area_codes)
                        print("\nNew York")
                        print("(",New_York,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 50:
                        Pennsylvania = rd.choice(pennsylvania_area_codes)
                        print("\nPennsylvania")
                        print("(",Pennsylvania,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 51:
                        Arizona = rd.choice(arizona_area_codes)
                        print("\nArizona")
                        print("(",Arizona,") - ",first_three, " - ", last_four,"\n")
                    elif pick_places == 52:
                        North_Carolina = rd.choice(north_dakota_area_codes)
                        print("\nNorth Carolina")
                        print("(",North_Carolina,") - ",first_three, " - ", last_four,"\n")
                if loop_again == phone_numbers:
                            x = 0
                            while x == 0:
                                ask_user = input("Would you like to generate more numbers? [Y]/[N]: ").upper()
                                if ask_user == ("Y"):
                                    print("\n")
                                    phone_number_generator()
                                elif ask_user == ("N"):
                                    x = 1
                                    print("\nGoodbye!\n")
                           
            elif phone_numbers > 20:
                print("\nYou may not generate more than 20 phone numbers\n")
               
   
           
   

if __name__ == "__main__":
    phone_number_generator()
