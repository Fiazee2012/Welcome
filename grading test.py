print("Welcome to the Grade Calculator!")          
marks = int(input ("Enter your marks: "))

if (marks >= 90):
    print("Total: " +str(marks) + ", A")
elif (marks >= 80 and marks <= 89):
    print("Total: " +str(marks) + ", B")
elif (marks >= 60 and marks <= 79):
    print("Total: " +str(marks) + ", C")
else: 
    print("D")