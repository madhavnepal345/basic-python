class person:
   def __init__(self,name):
     self.name=z

   def reading(self):
        print(f"{name} is reading") 
   def working(self):
        print(f"{name} is working")

p1= person("Mohana")

p1.reading()

#%%
#wap to crete a class named "Area and method calculate rectangle and calculate square"\

class Area:
     def __init__(self,length,breadth):
          self.lenght=length
          self.breadth=breadth
     def Rectangle(self):
          return self.lenght * self.breadth
     def Square(self,side):
          return side**2

a=Area(4,5)
result=a.Rectangle()
print(f"The area of the rectangle is {result}")
side=3
result1=a.Square(side)
print(f"The area of the square with    {result1}")



# %%

#find out the odd and even number using  oops

class  Math:
     def __init__(self,num):
          self.num=num
     def odd_number(self):
          if (user_input!=0):
               print(self.num, " is odd number")
     def even_number(self):
          if user_input==0:
               print(self.num,"is an even")
user_input("Enter the number from user")
oddobj=Math(user_input)
evenobj=Math(user_input)
oddnumber=oddobj(odd_number)
evendnumber=evenobj(even_number)



# %%
