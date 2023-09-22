#A = 81 - 100
#B = 71 - 80
#C = 60 - 70
#D = 45 - 59
#E = 31 - 44
#F = 0 - 30

grade = int(input("What is your score?: "))
if grade > 80 and grade <= 100:
    print("You have an A...")
elif grade <= 80 and grade > 70:
    print("You have a B..")
elif grade >= 60 and grade <= 70:
    print("That's a C..")
elif grade >= 45 and grade < 60:
    print("You have a D...")
elif grade > 30 and grade < 45:
    print("You have an E...")
elif grade >= 0 and grade <= 30:
    print("You have an F...")
else:
    print("You didn't write the test")

    


    


    


