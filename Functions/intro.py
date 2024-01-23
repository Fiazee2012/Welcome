def intro():
    print("This is a function, although you won't know it. Sorry.")
intro()

def add(num1, num2):
    sum = num1 + num2
    print("Answer => ", sum)

add(12, 12)

def square(num):
    multiply = num * num
    print("Square => ", num)
    return square

results = square(5)
print("The square => ", results)