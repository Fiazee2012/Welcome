age = int(input("Enter your age: "))
if age >= 18:
    print("You have been given permission by the Goverment to vote. Your age is: " + str(age))
else:
    print("You are not allowed to vote! Your age is: " + str(age))

print("Enter two numbers: ")
first_number = input("Enter the first number: ")
print(first_number)
second_number = input("Enter the second number: ")
print(second_number)

if first_number > second_number:
    print("The first number you entered is greater then the second number! The bigger number was..." + str(first_number))
else:
    print("The first number you entered is less then the second number! The smaller number was..." +str(second_number))