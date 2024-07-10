#wap to print the prime number using for statement
num=int(input("Enter a Prime Number: "))
if num==1:
    print("The given number is not a prime number")
if num>1:
   for i in range(2,num):
       if (num%i)==0:
           print("The given number is not a prime number")
           break
   else:
       print("The given number is a prime number")
 
 
