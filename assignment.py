#%%
#Program to swap two variables without using a temporary variable,and using temporary variable.

a=5
b=6
print(f"before swapping {a,b}:")
#Method 1: Using temporary variable
temp = a
a = b
b = temp
print(f"after swapping {a,b}")

#Method 2: Without using temporary variable
print(f"befor swapping again{a,b} :")
a,b=b,a
print(f"after swapping again{a,b} :",end=" ")



# %%
# Program to find the area of a rectangle given its length and width.
length=int(input("enter the length of the rectangle: "))
width=int(input("Enter the width of the rectangle: "))
print(f"the area of rectangle is {length*width}")


# %%
# Write a program that takes two numbers as input and prints their average.

num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))
avg=(num_1+num_2)/2
print(f"The average of {num_1} and {num_2} is {avg}")



# %%
# Create a program that converts temperature from Celsius to Fahrenheit.

temperature=float(input("Enter the temperature in celcius of your surrounding"))

fahern=(temperature *9/5)+32
print(f"the temepratur in fahrenheit is {fahern}")



# %%
#Program to calculate the sum, difference, product, and quotient(/) of two numbers entered by the user.
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
sum=num1+num2
diff=num1-num2  
product=num1*num2 
quotent=num1/num2
print(f"\nSum = {sum},\n Difference = {diff},\n Product = {product},\n Quotient = {quotent}")



# %%
#Program to check if a given number is even or odd without operator
def even_odd(number):
    if (number & 1) == 0 :
        return ("Even")
    else:
        return ("Odd")

number = int(input('Enter a number: '))
print(even_odd(number))




# %%
# Program to find the maximum and minimum numbers from given number [46,2,90,55,34,23,88].

numbers=[46,2,90,55,34,23,88]
max_no=numbers[0]
min_no=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i]>max_no:
        max_no=numbers[i]
    elif numbers[i]<min_no:
        min_no=numbers[i]
print(f'The Maximum Number Is {max_no} \n The Minimum Number Is {min_no}')


# %%
#Program to check if a student has passed or failed based on their exam score.
score=int(input("Enter Score:"))
if score>=50:
    print("Passed")
else:
    print("Failed")

# %%
