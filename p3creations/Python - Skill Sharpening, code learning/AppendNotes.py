def Notes():
    print("[1] - Way One")
    print("[2] - Way Two")
    user_input = input("Select an option: ")
    ui = user_input
    if ui == ("1"):
        print("\n |  Test = []                               |")

        print(" |  for i in range(5):                      |")
        print(" |   Test.append(input('Enter a number: ')  |")
        print(" |  print(Test)                             |")


if __name__ == "__main__":
    Notes()
