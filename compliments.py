percentage = int(input("Please enter the percentage: "))
percent = "%"

if percentage >= 65:
    print(percentage + percent)
    print("Excellent")
elif (percentage >= 55 and percentage < 65):
    print(percentage + percent)
    print("Good")
elif (percentage >= 40 and percentage < 55):
    print(percentage + percent)
    print("Fair")
else:
    print("Failed")