p = "e"

def add_product():
    inventory = {}
    product = input("enter product name: ")
    price = float("enter product price: ")
    quantity = int(input("enter product quantity: "))



while p == "e":
    print("\n1.add product")
    print("2.show inventory")
    print("3.calculate statistics")
    print("4.exit")
    option = input("enter option: ")

    if option == "1":
        print("hola")
    elif option == "2":
        print()
    elif option == "3":
        print()
    elif option == "4":
        p = "r"
    else:
        print("invalid option.")
