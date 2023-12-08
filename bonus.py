time = int(input("How many years have you worked in our company? : "))
salary = int(input("What is your salary right now? : "))

if time >= 10:
    print("Wow! we appreciate you and give you a 10% bonus.")
    bonus = 10 / 100 * salary
    netBonus = salary + bonus
    print(netBonus, "is is what you are getting now.")
elif (time >= 6 and time <= 10):
    print("Wow! we appreciate you and give you a 8% bonus.")
    bonus = 8 / 100 * salary
    netBonus = salary + bonus
    print(netBonus,  "is what you are getting right now.")
else: 
    time <= 6
    print("Wow! we appreciate you and give you a 5% bonus.")
    bonus = 5 / 100 * salary
    netBonus = salary + bonus
    print(netBonus, "is what you are getting right now.")