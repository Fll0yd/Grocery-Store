def enterproducts():
  buyingdata = {}
  enterdetails = True
  while enterdetails:
    details = input('Press A to add a product or Q to quit: ').strip().upper()
    if details == "A":
      try:
        product = input("Enter Product:").strip()
        quantity = int(input("Enter Quantity: "))
        buyingdata.update({product: quantity})
      except ValueError:
        print("Invalid quantity. Please enter a number.")
    elif details == "Q":
      enterdetails = False
    else:
      print('Please select either A to enter another product or Q to quit: ')
  return buyingdata


def getprice(product, quantity):
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
  print(product + ":$" + str(pricedata[product]) + "x" + str(quantity) + "=" +
        str(subtotal))
  return subtotal


def makebill(buyingdata, membership):
  billamount = 0
  for key, value in buyingdata.items():
    billamount += getprice(key, value)
  billamount = getdiscount(billamount, membership)
  print("The discounted amount is $" + str(billamount))


def getdiscount(billamount, membership):
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
    print(
      str(discount) + "% off for" + membership + " " +
      "membership on total amount: $" + str(billamount))
  else:
    print("No discount on amount less than $25")
  return int(billamount)


buyingdata = enterproducts()
while not buyingdata:
  print("No items entered. Please try again.")
  buyingdata = enterproducts()
membership = input("Enter customer membership: ")
while membership not in ["Gold", "Silver", "Bronze"]:
  print("Invalid membership type. Please enter Gold, Silver, or Bronze.")
  membership = input("Enter customer membership: ")
makebill(buyingdata, membership)