#enterproducts(): This function allows the user to enter details about the products they wish to buy. It does this by using a while loop to repeatedly prompt the user to add a product and its quantity until they choose to quit. It then stores the product and quantity information in a dictionary called buyingdata and returns this dictionary.

def enterproducts(): # Function 1
    buyingdata = {}
    enterdetails = True

    while enterdetails:
        details = input("Press A to add an additional product or Q to quit")

        if details == "A":
            product = input("Enter Product:")
            quantity = int(input("Enter Quantity: "))
            buyingdata.update({product: quantity})
        elif details == "Q":
            enterdetails = False
        else:
            print("Please select either A to enter another product or Q to quit.")

    return buyingdata

#getprice(product, quantity): This function takes in the name of a product and its quantity, and returns the subtotal cost of that product. It does this by using a dictionary called pricedata to look up the price of the product, and then multiplying it by the quantity. It also prints out a message showing the calculation and returns the subtotal.

def getprice(product, quantity): # Function 2
    pricedata = {
        "Biscuit": 3,
        "Chicken": 5,
        "Egg": 1,
        "Fish": 3,
        "Coke": 2,
        "Bread": 2,
        "Apple": 3,
        "Onion": 3,
    }

    subtotal = pricedata[product] * quantity
    print(product + ": $" + str(pricedata[product]) + " x " + str(quantity) + " = $" + str(subtotal))

    return subtotal

#getdiscount(billamount, membership): This function takes in the total bill amount and a membership level, and returns the discounted bill amount based on the membership level. If the bill amount is at least 25, the function calculates the discount based on the membership level and applies it to the bill amount. It then prints a message showing the discount percentage and new total amount. Finally, it returns the discounted bill amount.

def getdiscount(billamount, membership): # Function 3
    discount = 0

    if billamount >= 25:
        if membership == "Gold":
            billamount = billamount * 0.80
            discount = 20
        elif membership == "Silver":
            billamount = billamount * 0.90
            discount = 10
        elif membership == "Bronze":
            billamount = billamount * 0.95
            discount = 5

        print(str(discount) + "% off for " + membership + " membership on total amount: $" + str(billamount))

    return billamount - (billamount * (discount/100))