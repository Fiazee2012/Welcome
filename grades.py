print("Welcome to the Grade Calculator!")
Maths = int(input ("Enter your maths score: "))
Geography = int(input ("Enter your geography score: "))
Science = int(input ("Enter your science score: "))
English = int(input ("Enter your english score: "))
              
total = Maths+Geography+Science+English
print("Your total marks are " + str(total) + ".")
average = total//5

if (average >= 80 and average <= 100):
    print("Congrats, you passed your exam! your score: " +str(total))
    print("Congrats, you passed your exam! your average: " +str(average) + " plus you got an A")
elif (average >= 60 and average <= 79):
    print("Congrats, you passed your exam! your score: " +str(total))
    print("Congrats, you passed your exam! your average: " +str(average) + " plus you got an B")
elif (average >= 40 and average <= 59):
    print("V.good, you passed your exam! your score: " +str(total))
    print(", you passed your exam! your average: " +str(average) + " plus you got an C")
elif (average >= 30 and average <= 39):
    print("Poor, you passed your exam! your score: " +str(total))
    print("Poor, you passed your exam! your average: " +str(average) + " plus you got an D")
else: 
    print("Try harder next time, you got an F")