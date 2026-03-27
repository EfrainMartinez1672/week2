import values as m

def add_product():
    name = input("enter product name: ")
    p = "e"
    while p == "e":
        try:
            price = float(input("enter product price: "))
            p = "r"
        except ValueError:
            print("enter only integers.")

    quantity = input("enter product quantity: ")
    while not quantity.isdigit():
        quantity = input("enter product quantity")

    quantity = int(quantity)

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    m.inventory.append(product)
    m.calculate.append(price * quantity)

def show_product():
    for data in m.inventory:
        print(f"product: {data["name"]} | price {data["price"]} | quantity {data["quantity"]}")

def calculate():
    total = sum(m.calculate)
    print(f"the total is: {total}")