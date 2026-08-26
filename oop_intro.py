# class Temperature:

#     def __init__(self, celsius):
#         self.celsius = celsius

#     def to_fahrenheit(self):
#         fahrenheit = (self.celsius * 9 / 5) + 32
#         print(fahrenheit)


# temp1 = Temperature(0)
# temp2 = Temperature(25)
# temp3 = Temperature(100)

# temp1.to_fahrenheit()
# temp2.to_fahrenheit()
# temp3.to_fahrenheit()

# class student:
#     def __init__(self,name):
#         self.name=name
#     def show_name(self):
#         print(self.name)
# student=student("Vaishnavi")
# student.show_name()

#ACCESSING MULTIPLE VARIABLES
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show_details(self):
#         print("Name:",self.name)
#         print("Salary:",self.salary)
# emp=employee("Aman",50000)
# emp.show_details()

# class rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print(self.length*self.width)
# rect1=rectangle(8,5)
# rect1.area()

#USING ONE INSTANCE VARIABLE WITH ANOTHER
# class student:
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name 
#         self.last_name=last_name
#     def full_name(self):
#         print(self.first_name+" "+self.last_name)
# student=student("Vaishnavi","Gupta")
# student.full_name()

# class student:
#     def __init__(self,maths_marks,physics_marks,chemistry_marks):
#         self.maths_marks=maths_marks
#         self.physics_marks=physics_marks
#         self.chemistry_marks=chemistry_marks
#     def average(self):
#         avg=(self.maths_marks+self.physics_marks+self.chemistry_marks)
#         print(avg)
# student1=student(80,90,70)
# student2=student(95,85,75)
# student1.average()
# student2.average()

# class shoppingcart:
#     def __init__(self,item_name,price,quantity):
#         self.item_name=item_name
#         self.price=price
#         self.quantity=quantity
#     def bill(self):
#         total=self.price*self.quantity
#         print("Item:",self.item_name)
#         print("Total Bill:",total)
# cart1=shoppingcart("Laptop",50000,2)
# cart2=shoppingcart("Headphnes",3000,3)
# cart1.bill()
# cart2.bill()        

#MODIFYING INSTANCE VARIABLES INSIDE INSTANCE METHODS
# class Student:
#     def __init__(self,name):
#       self.name=name
#     def change_name(self,new_name):
#       self.name=new_name
# student=Student("Rahul")
# print(student.name)
# student.change_name("Vaishnavi")
# print(student.name)

#incrementing an instance variable
# class Counter:
#     def __init__(self):
#         self.count=0
#     def increment(self):
#         self.count+=1
#     def display(self):
#         print(self.count)
# counter=Counter()
# counter.increment()
# counter.increment()
# counter.increment()
# counter.display()

#decrementing an instance variable
# class Player:
#     def __init__(self):
#         self.health=100
#     def damage(self):
#         self.health-=20
#     def display(self):
#         print(self.health)
# player=Player()
# player.damage()
# player.damage()
# player.display()

#updating multiple instance variables
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def promote(self):
#         self.name="Senior "+self.name
#         self.salary+=10000
#     def display(self):
#         print(self.name)
#         print(self.salary)
# emp=Employee("vaishnavi",50000)
# emp.promote()
# emp.display()

# class Bankaccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#     def display(self):
#         print("Balance",self.balance)
# account=Bankaccount(5000)
# account.display()
# account.deposit(2000)
# account.display()

# class Car:
#     def __init__(self,speed):
#         self.speed=speed
#     def accelerate(self):
#         self.speed+=10
#     def brake(self):
#         self.speed-=10
#     def display_speed(self):
#         print("Speed:",self.speed)
# car=Car(50)
# car.display_speed()
# car.accelerate()
# car.accelerate()
# car.display_speed()
# car.brake()
# car.display_speed()

# class Book:
#     def __init__(self,title,copies):
#         self.title=title
#         self.copies=copies
#     def borrow(self):
#         self.copies-=1
#     def return_book(self):
#         self.copies+=1
#     def display(self):
#         print("Book:",self.title)
# book1=Book("Python",5)
# book2=Book("Java",3)
# book1.borrow()
# book2.borrow()
# book2.return_book()
# book1.return_book()
# book1.display()
# book2.display()

# class Wallet:
#     def __init__(self,money):
#         self.money=money
#     def add_money(self,amount):
#         self.money+=amount
#     def spend_money(self,amount):
#         self.money-=amount
#     def display_money(self):
#         print("Money:",self.money)
# wallet1=Wallet(1000)
# wallet2=Wallet(500)
# wallet1.add_money(500)
# wallet1.spend_money(200)
# wallet2.spend_money(100)
# wallet2.add_money(300)
# wallet1.display_money()
# wallet2.display_money()

#CREATING INSTANCE VARIABLES INSIDE INSTANCE METHODS

# class Student:
#     def add_age(self):
#         self.age=20
# student=Student()
# student.add_age()
# print(student.age)

# class Car:
#     def set_detail(self):
#         self.brand="Toyoto"
#         self.price=1500000
# car=Car()
# car.set_detail()
# print(car.brand)
# print(car.price)

# class Mobile:
#     def insert_sim(self):
#         self.sim_name="Jio"
#         self.mobile_number="7303515249"
# mobile1=Mobile()
# mobile2=Mobile()
# mobile1.insert_sim()
# print(mobile1.sim_name)
# print(mobile2.mobile_number)

#ACCESSING INSTANCE VARIABLES CREATED INSIDE INSTANCE METHODS
# class Student:
#     def set_name(self):
#         self.name="Vaishnavi"
#         print(self.name)
# student=Student()
# student.set_name()

#accessing in another method
# class Student:
#     def set_name(self):
#         self.name="Vaishnavi"
#     def show_name(self):
#         print(self.name)
# student=Student()
# student.set_name()
# student.show_name()

# class Game:
#     def start(self):
#         self.level=1
#     def play(self):
#         print("Current Level:",self.level)
# game=Game()
# game.start()
# game.play()

# class Movie:
#     def set_movie(self):
#         self.title="Evil Dead Burn"
#     def show_movie(self):
#         print(self.title)
# movie=Movie()
# movie.set_movie()
# movie.show_movie()
# print(movie.title)
        
#checking whether an instance variable exists
# class Student:
#     def __init__(self):
#         self.name="Vaishnavi"
# student=Student()
# print(hasattr(student,"name"))


# class Student:
#     pass
# student=Student()
# print(hasattr(student,"name"))

#using hasattr() before accessing
# class Student:
#     def set_name(self):
#         self.name="Vaishnavi"
#     def show_name(self):
#         if hasattr(self,"name"):
#             print(self.name)
#         else:
#             print("Name not Found")
# student=Student()
# student.show_name()
# student.set_name()
# student.show_name()

# class Player:
#     def set_score(self):
#         self.score=100
#     def show_score(self):
#         if hasattr(self,"score"):
#             print("Score:",self.score)
#         else:
#             print("Score is not available")
# player=Player()
# player.show_score()
# player.set_score()
# player.show_score()

#DELETING INSTANCE VARIABLE
# class Student:
#     def __init__(self):
#         self.name="Vaishnavi"
#         self.age=20
#     def delete_age(self):
#         del self.age
# student=Student()
# student.delete_age()
# print(student.name)

#using hasattr after deletion
# class Student:
#     def __init__(self):
#         self.name="vaishnavi"
#     def delete_name(self):
#         del self.name
# student=Student()
# print(hasattr(student,"name"))
#student.delete_name()
# print(hasattr(student,"name"))

#deleting more than one variable
# class Laptop:
#     def __init__(self):
#         self.brand="Dell"
#         self.price=70000
#         self.ram=16
#     def delete_details(self):
#         del self.price
#         del self.ram
# laptop=Laptop()
# laptop.delete_details()
# print(laptop.brand)

# class Librarybook:
#     def __init__(self):
#         self.title="Python Programming"
#         self.author="Guido"
#         self.price=599
#     def remove_price(self):
#         del self.price
#     def display(self):
#         print("Title:",self.title)
#         print("Author:",self.author)
        
#         if hasattr(self,"price"):
#             print("Price:",self.price)
# book=Librarybook()
# book.display()
# book.remove_price()
# book.display()

 
#deleting instance variables from outside the class
# class Student:
#     def __init__(self):
#         self.name="Vaishnavi"
#         self.age=20
# student=Student()
# del student.age
# print(student.name)

#using hasattr() after outside deletion
# class Student:
#     def __init__(self):
#         self.name="vaishnavi"
# student=Student()
# print(hasattr(student,"name"))
# del student.name
# print(hasattr(student,"name"))

#multiple objects
# class Student:
#     def __init__(self):
#         self.name="Vaishnavi"
# student1=Student()
# student2=Student()
# del student1.name
# print(hasattr(student1,"name"))
# print(hasattr(student2,"name")) 

# class User:
#     def __init__(self):
#         self.name="Vaishnavi"
#         self.email="vaishnavi@gmail.com"
#         self.phone="7303515249"
# user=User()
# del user.email
# print(user.name)
# print(user.phone)
# print(hasattr(user,"email"))

#DIFFERENCE BETWEEN INSTANCE VARIABLES AND LOCAL VARIABLES
# class Calculator:
#     def add(self):
#         num1=10
#         num2=20
#         total=num1+num2
#         print(total)
# calc=Calculator()
# calc.add()

#Accessing local variables outside the method
# class Demo:
#     def show(self):
#         number=50
#         print(number)
# obj=Demo()
# obj.show()
# print(number) 

#instance variables vs local variables
# class Student:
#     def __init__(self):
#         self.name="Vaishnavi"
#     def display(self):
#         message="Welcome"
#         print(self.name)
#         print(message)
# student=Student()
# student.display()

# class Laptop:
#     def __init__(self):
#         self.brand="Dell"
#     def calculate_discount(self):
#         discount=5000
#         print("Discount:",discount)
#     def show_details(self):
#         print("Brand:",self.brand)
#         print("Discount:",self.discount)
# laptop=Laptop()
# laptop.calculate_discount()
# laptop.show_details()

# class Rectangle:
#     def __init__(self):
#         self.length=10
#         self.width=5
#     def find_area(self):
#         area=self.length*self.width
#         print("Area:",area)
#     def show_area(self):
#         print(area)
# rect=Rectangle()
# rect.find_area()
# rect.show_area()

#CONVVERTING A LOCAL VARIABLE INTO AN INSTANCE VARIABLE
# class Student:
#     def calculate_marks(self):
#         total=450
#         print("Total:",self.total)
#     def show_marks(self):
#         print("Stored Total:",self.total)
# student=Student()
# student.calculate_marks()
# student.show_marks()

# class Exam:
#     def calculate_percentage(self):
#         self.percentage=92
#     def result(self):
#         print("Percentage:",self.percentage)
# exam=Exam()
# exam.calculate_percentage()
# exam.result()

# class Circle:
#     def __init__(self):
#         self.radius=2
#     def calculate_area(self):
#         self.area=3.14*self.radius*self.radius
#         print("Area:",self.area)
#     def show_area(self):
#         print("Stored Area:",self.area)
# circle=Circle()
# circle.calculate_area()
# circle.show_area()

# class Employee:
#     def __init__(self):
#         self.name="Vaishnavi"
#         self.working_days=30
#     def calculate_salary(self):
#         self.salary=self.working_days*1000
#         print("Salary:",self.salary)
#     def print_salary(self):
#         print("Stored Salary:",self.salary)
# emp=Employee()
# emp.calculate_salary()
# emp.print_salary()

# class Bankaccount:
#     def __init__(self):
#         self.account_holder="Vaishnavi"
#         self.balance=100000
#     def calculate_interest(self):
#         self.interest=self.balance*0.05
#         print("Interest:",self.interest)
#     def show_interest(self):
#         print("Stored Interest:",self.interest)
# account=Bankaccount()
# account.calculate_interest()
# account.show_interest()


#and give me 2 to 3 medium to hard problems that tests number thoery , mathematical algorithmsincluded the expected input/output but do not provide the full solution , 1 to 2 leetcode style important problems , one mini project to clear the whole topic and concepts and kuch bhi skip mat karna