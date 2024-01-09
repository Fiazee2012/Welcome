money = float(input("Please enter the price of what you're buying: "))

if money >= 10000:
    discount = 20 / 100 * money
    netBonus = money - discount
    print("You will have to pay",  netBonus, "for the item you bought.")
elif (money > 7000 and money <= 10000):
    discount = 15 / 100 * money
    netBonus = money - discount
    print("You will have to pay",  netBonus, "for the item you bought.")
else: 
    discount = 10 / 100 * money
    netBonus = money - discount
    print("You will have to pay",  netBonus, "for the item you bought.")