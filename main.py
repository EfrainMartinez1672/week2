from fuctions import add_product, show_product, calculate
p = "e"

while p == "e":
    print("\n1.add product")
    print("2.show inventory")
    print("3.calculate statistics")
    print("4.exit")
    option = input("enter option: ")

    if option == "1":
        add_product()
    elif option == "2":
        show_product()
    elif option == "3":
        calculate()
    elif option == "4":
        p = "r"
    else:
        print("invalid option.")
