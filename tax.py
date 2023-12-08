price = int(input("Enter the price: "))

if price > 100000:
     roadTax = 15/100 * price
     print("The tax to be paid is: " , roadTax, "Ksh")
elif  (price > 50000 and price <= 100000):
    roadTax = 10/100 * price
    print("The tax to be paid is: ", roadTax, "Ksh")
else:
    roadTax = 5/100 * price
    print("The tax to be paid is: " , roadTax, "Ksh")