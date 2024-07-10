
first_number=int(input("Enter the first Number: "))
operator=input("Enter the operator you want(+, -, *, /): ")
second_number=int(input("Enter the second number: "))

def addition(a ,b):
    return a+b
def subraction(a, b):
    return a-b
def multiplication(a, b):
    return a*b
def division(a,b):
    return a/b


        
if operator=='+':
    print(f"addition is : {addition(first_number,second_number)}")
elif operator=='-':
    print(f"subraction is: {subraction(first_number-second_number)}")
elif operator=='*':
    print(f"multiplication is:{multiplication(first_number*second_number)}")
elif operator=='/':
    print(f"division is :{division(first_number/second_number)}")
else:
    print("Invalid operator")









