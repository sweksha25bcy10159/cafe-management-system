# MODULE 1: LOAD ITEMS FROM FILE
def load_items(filepath):
    itemAvailable = {}

    try:
        with open(filepath, "r") as my_file:
            itemsAvailable = my_file.readlines()
    except FileNotFoundError:
        print(" ERROR: Menu file not found!")
        return {}

    print("****************** CAFE HIDEOUT *********************")
    print("--------------- MENU -----------------")

    for item in itemsAvailable:
        item = item.strip()   # remove spaces / newline

        if item == "":        # skip empty rows
            continue

        parts = item.split()

        if len(parts) < 2:
            continue

        # Last part = price
        try:
            item_price = float(parts[-1])
        except ValueError:
            continue

        # Item name = everything except last word
        item_name = " ".join(parts[:-1])

        print(f"{item_name}: {item_price}")
        itemAvailable[item_name.title()] = item_price

    print("*" * 20)
    return itemAvailable

# MODULE 2: TAKE ORDER
def take_order(itemAvailable):
    shoppingDict = {}

    customerorder = input("WOULD YOU LIKE TO ORDER SOMETHING? (yes/no): ")

    while customerorder.lower() == "yes":
        item_added = input("Add an item name: ").title()

        if item_added in itemAvailable:
            item_qty = int(input("Add item quantity: "))

            subtotal = itemAvailable[item_added] * item_qty

            shoppingDict[item_added] = {
                "quantity": item_qty,
                "SubTotal": subtotal
            }

            print("Current order:", shoppingDict)

        else:
            print(" Item not found! TRY SOMETHING ELSE")

        customerorder = input("Do you wish to order more items? (yes/no): ")

    return shoppingDict

# MODULE 3: GENERATE BILL
def generate_bill(shoppingDict):
    print("\n********* BILL SUMMARY ************\n")
    print("Item            Quantity      SubTotal")

    total = 0

    for item in shoppingDict:
        qty = shoppingDict[item]['quantity']
        st = shoppingDict[item]['SubTotal']

        print(f"{item:15} {qty:5}        {st}")
        total += st

    print("\n-----------------------------------")
    print(f"TOTAL BILL: {total}")
    print("********** THANK YOU **********")
    print("----- HOPE YOU ENJOYED OUR FOOD AND SERVICE! -----")
    print("----- Hope to see you back soon! -----")

# MAIN PROGRAM
itemAvailable = {}
shoppingDict = {}

# Welcome user
userName = input("Please enter your name: ")
user_Name = userName.upper()
WelcomeMessage = f"WELCOME TO CAFE HIDEOUT {user_Name}"
print("*" * len(WelcomeMessage))
print(WelcomeMessage)
print("*" * len(WelcomeMessage))

# Load menu file
filepath = r"C:\Users\sweksha kakkar\Downloads\cafehideout.txt"
itemAvailable = load_items(filepath)

# Take order
shoppingDict = take_order(itemAvailable)

# Generate bill
generate_bill(shoppingDict)