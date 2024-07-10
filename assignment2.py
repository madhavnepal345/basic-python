#WAP to print below format ,(take age from user input)
    # <12 :"you are child hood"
    # >12-<20 "you are teen agers"
    # >20-<50 "you are adult"
    # >50 print "you are old"

age=int(input("Enter the age of people: "))
if age<=12:
    print("You are Child")
elif(20<=age and age<=50):
    print("You are Adult")
elif(13<=age and age<20):
    print("You are Teenager")

else:
    print("You are Old")