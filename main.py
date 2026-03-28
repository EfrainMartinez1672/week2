from fuctions import add_product, show_product, calculate  # import the three main functions

p = "e"  # variable to control the menu loop

while p == "e":
    # print menu options
    print("\n1.add product")
    print("2.show inventory")
    print("3.calculate statistics")
    print("4.exit")
    
    option = input("enter option: ")  # get user choice

    if option == "1":
        add_product()  # call function to add a product
    elif option == "2":
        show_product()  # call function to show all products
    elif option == "3":
        calculate()  # call function to calculate total value
    elif option == "4":
        p = "r"  # exit loop and program
    else:
        print("invalid option.")  # invalid menu input
