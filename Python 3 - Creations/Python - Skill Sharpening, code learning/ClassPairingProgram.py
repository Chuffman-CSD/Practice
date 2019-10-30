#!/usr/bin/python3
#Chris Huffman
#10/15/19

def ClassPairing():
    pass
    numberOfStudents = 0
    listOfStudents = [""]
    #ui is the user_input
    ui = input("Enter a name: ").capitalize()
    listOfStudents.append(ui)
    print("\n")
    print(ui,"was just added!\n")
    while ui != ("Done"):
        ui = input("Enter a name: ").capitalize()
        if ui in listOfStudents:
            print("\n")
            print(ui,"is already in the list\n")
        else:
            print(ui,"was just added!\n")
    print ("Test")

if __name__ == "__main__":
    ClassPairing()
