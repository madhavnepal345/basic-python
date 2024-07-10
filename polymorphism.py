#class=animal def make sound()  print this is animal 
#%%
class Animal():
    def make_sound(self):
        print("This is animalsound")

class Dog(Animal):
    def make_sound(self):
        print("This is bho bho bho")
class Cat(Animal):
    def make_sound(self):
        print("this is meo meo")
class Ant(Animal):
    pass

d1=Dog()
d1.make_sound()


a1=Ant()
a1.make_sound() 


#%%

#Give an example of method overiding in polymorphism 


class Vehicles:
    def start_engine(self):
        print("Engine started")

class Bike(Vehicles):
    def start_engine(self):
        print("Bike engine started")
class Car(Vehicles):
    def start_engine(self):
        print("Car engine started")
class mopad(Vehicles):
    pass

b1=Bike()
b1.start_engine()
m1=mopad()
m1.start_engine()
    
#%%
 #method overloading example

def Sum(a,b,c,d=0):
    return a+b+c
    
output=Sum(3,4,4)
print(output)

# %%


#abstraction  in python 
#abstraction means hiding the complexcity of the code 

from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def noofside(self):
        pass
class Triangle(Polygon):
    def noofside(self):
        print("Triangle has 3 sides")
    def area(self):
        print("Calculating area of triangle")

class Pentagon(Polygon):
    def noofside(self):
        print("I am pentagon")
    def area(self):
        print("calculating area of pentagon")
t=Triangle()
t.area()



# %%

from abc import ABC,abstractmethod
class Car(ABC):
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    @abstractmethod
    def price(self):
        pass

class BMW(Car):
    def price(self):
        print("Brand:", self.brand); 
        print("Model:", self.model); 
        print("Year:", self.year); 
    def Sunroof(self): 
        print("Not having this feature") 

class Suv(Car): 
    def price(self): 

        print("Brand:", self.brand); 
        print("Model:", self.model); 
        print("Year:", self.year); 
    def Sunroof(self): 
        print("Available") 



ca=Suv("Maruti","Alto","2020")
ca.price()
ca.Sunroof()

# %%
