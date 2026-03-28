import values as m  # import a module named 'values' and give it alias 'm' to store inventory and calculation lists

def add_product():
    # get product name from user
    name = input("enter product name: ")
    
    # loop to get valid price
    p = "e"
    while p == "e":
        try:
            price = float(input("enter product price: "))  # convert input to float
            if price < 0:
                print("just put positive numbers.")  # error if price is negative
            else:
                p = "r"  # exit loop if price is valid
        except ValueError:
            print("enter only integers.")  # error if input is not a number

    # loop to get valid quantity
    quantity = input("enter product quantity: ")
    while not quantity.isdigit():
        quantity = input("enter product quantity")  # repeat until input is a digit

    quantity = int(quantity)  # convert quantity to integer

    # create product dictionary
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    # add product to inventory list
    m.inventory.append(product)
    # add product total value to calculation list
    m.calculate.append(price * quantity)

def show_product():
    # check if inventory has products
    if m.inventory: 
        for data in m.inventory:
            # print each product info
            print(f"product: {data['name']} | price {data['price']} | quantity {data['quantity']}")
    else:
        # if inventory empty
        print("there is nothing.")

def calculate():
    # check if there are any calculated values
    if m.calculate:
        total = sum(m.calculate)  # sum all product totals
        print(f"the total is: {total}")  # show total value
    else:
        # if no products
        print("there is nothing.")