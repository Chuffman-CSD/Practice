values = []
x = 0
while x == 0:
    print("\n[0] - Imports a pre-made list\n")
    print("[1] - Adds a value to a list\n")
    print ("[2] - Prints the current list\n")
    print("[3] - Saves the list to a text file\n")
    #ui is the user_input
    ui1 = input("Select a choice: ")
    print("\n")
    if ui1 == ("0"):
        with open("List_File.txt") as f:
            f=f.read()
            f=open("List_File.txt")
            print("\nThe data saved on the file contains:",f.read())
    elif ui1 == ("1"):
        ui2 = input("Enter something: ")
        values.append(ui2)
    if ui1 == ("2"):
        print("The current list of values contain:",values)
    elif ui1 == ("3"):
        with open("List_File.txt","w") as output:
            output.write(str(values))
    else:
        print("\nThe only options are [1] and [2]!\n")
