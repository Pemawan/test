age=int(input("Enter you age : "))
yn=input("Are you a student (yes/no): ")
if age<=12:
    print("You are eligible for discount")
elif ((age>=13 and age<=18)and yn=='yes'):
    print ("You are eligible for the discount")
else:
    print("You are not eligible for the discount ")