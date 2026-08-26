# name = "Vaishnavi"
# balance = 10000

# def deposit(amount):
#     global balance
#     balance += amount

# def withdraw(amount):
#     global balance
#     balance -= amount

# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def show_balance(self):
#         print(self.balance)


# account = BankAccount(1000)

# account.deposit(500)

# account.show_balance()

# class Car:
#     def __init__(self,fuel,speed):
#         self.fuel=fuel
#         self.speed=speed
#     def start(self):
#         print("Car Started")
#     def accelerate(self):
#         if self.fuel>0:
#             self.speed+=20
#             self.fuel-=2
#             print("Car Accelerated")
#         else:
#             print("No Fuel")
#     def brake(self):
#         if self.speed>=20:
#             self.speed-=20
#         else:
#             self.speed=0
#     def refuel(self,amount):
#         self.fuel+=amount
#     def display(self):
#         print("Fuel:",self.fuel)
#         print("Speed:",self.speed)
# car=Car(20,0)
# car.display()
# car.start()
# car.accelerate()
# car.display()
# car.brake()
# car.display()
# car.refuel(10)
# car.display()

# class HotelRoom:
#     def __init__(self,room_number,price):
#         self.room_number=room_number
#         self.price=price
#         self.available=True
#     def book_room(self):
#         if self.available:
#             self.available=False
#             print("Room booked successfully.")
#         else:
#             print("Room is already booked")
#     def cancel_booking(self):
#         if not self.available:
#             self.available=True
#             print("Booking cancelled successully.")
#         else:
#             print("Room is already available.")
#     def display_details(self):
#         print("Room Number:",self.room_number)
#         print("Price:",self.price)
#         print("Available:",self.available)
# room1=HotelRoom(101,2500)
# room1.display_details()
# print()
# room1.book_room()
# print()
# room1.display_details()
# print()
# room1.cancel_booking()
# print()
# room1.display_details()

#ENCAPSULATION VS DATA HIDING
#data hiding 
# class Bank:
#     def __init__(self):
#         self.__balance=10000
# Bank.__balance

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def show_balance(self):
#         print("Balance:",self.__balance)
# account=BankAccount(10000)
# account.show_balance()

# class Phone:
#     def __init__(self):
#         self.__battery=100
#     def use_phone(self):
#         self.__battery-=10
#     def show_battery(self):
#         print(self.__battery)
# phone=Phone()
# phone.show_battery()
# phone.use_phone()
# phone.show_battery()

#access modifiers
#PUBLIC MEMBERS
# class Student:
#     def __init__(self):
#         self.name="Vaishnavi"
# student=Student()
# print(student.name)

#PROTECTED MEMBERS
# class Student:
#     def __init__(self):
#         self._marks=95

#PRIVATE MEMBERS
# class Student:
#     def __init__(self):
#         self.__salary=50000
# Student.__salary

# class Student:
#     def __init__(self):
#         self.name="Vaishnavi"
#         self._marks=95
#         self.__password="Python123"

#     def show_details(self):
#         print("Name:",self.name)
#         print("Marks:",self._marks)
#         print("Password:",self.__password)
# student=Student()
# print("Public Member")
# print(student.name)
# print()
# print("Protected Member")
# print(student._marks)
# print()
# print("Accessing Private Member Inside Class")
# student.show_details()

# class PrimeChecker:
#     def __init__(self,number):
#         self.number=number
#         self._factor_count=0
#     def is_prime(self):
#         self._factor_count=0
#         for i in range(1,self.number+1):
#             if self.number%i==0:
#                 self._factor_count+=1
#         return self._factor_count==2
#     def display_result(self):
#         if self.is_prime():
#             print(f"{self.number} is Prime")
#         else:
#             print(f"{self.number} is Not Prime")
# checker=PrimeChecker(29)
# checker.display_result()

# class GCDCalculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         self._steps=[]
#     def find_gcd(self):
#         a=self.num1
#         b=self.num2
#         self._steps.clear()
#         while b!=0:
#             remainder=a%b
#             self._steps.append(
#                 f"{a}%{b}={remainder}"
#             )
#             a=b
#             b=remainder
#         return a
#     def display_steps(self):
#         gcd=self.find_gcd()
#         print("Euclidean algorithm steps")
#         for step in self._steps:
#             print(step)
#         print()
#         print("GCD=",gcd)
# calculator=GCDCalculator(48,18)
# calculator.display_steps()


#PUBLIC MEMBERS
#Public Instance Variable
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("Name:",self.name)
#         print("Marks:",self.marks)
# student=Student("Vaishnavi",95)
# student.display()


#Accessing Public Variables Outside the class
# class Student:
#     def __init__(self):
#         self.name="Vaishnavi"
# student=Student()
# print(student.name)


#Modifying Public Variables
# class Student:
#     def __init__(self):
#         self.name="Vaishnavi"
# student=Student()
# print(student.name)
# student.name="Gupta"
# print(student.name)


#Public Methods
# class Calculator:
#     def add(self,a,b):
#         return a+b
# obj=Calculator()
# print(obj.add(10,20))


#Public Class Variables
# class Student:
#     college="ABC college"
# print(Student.college)


#Public Constructor
# class Student:
#     def __init__(self):
#         print("Object Created")
# student=Student()


# class ArmstrongChecker:
#     def __init__(self,number):
#         self.number=number
#     def is_armstrong(self):
#         original_number=self.number
#         temp=self.number
#         digits=len(str(self.number))
#         total=0
#         while temp>0:
#             digit=temp%10
#             total=total+digit**digits
#             temp=temp//10
#         return total==original_number
#     def display_result(self):
#         if self.is_armstrong():
#             print(self.number,"is an Armstrong Number")
#         else:
#             print(self.number,"is an Armstrong Number")
# checker=ArmstrongChecker(153)
# checker.display_result()


# class LCMCalculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num1=num1
#         self.num2=num2
#     def find_lcm(self):
#         a=self.num1
#         b=self.num2
#         while b!=0:
#             remainder=a%b
#             a=b
#             b=remainder
#         gcd=a
#         lcm=(self.num1*self.num2)//gcd
#         return lcm
#     def display_result(self):
#         print("LCM=",self.find_lcm())
# calculator=LCMCalculator(12,18)
# calculator.display_result()


# class PalindromeNumber:
#     def __init__(self,number):
#         self.number=number
#     def check_palindrome(self):
#         original_number=self.number
#         temp=self.number
#         reverse=0
#         while temp>0:
#             digit=temp%10
#             reverse=reverse*10+digit
#             temp=temp//10
#         return reverse==original_number
#     def display_result(self):
#         if self.check_palindrome():
#             print(self.number,"is Palindrome")
#         else:
#             print(self.number,"is Not Palindrome")
# checker=PalindromeNumber(12321)
# checker.display_result()


#PROTECTED MEMBERS
# class Student:
#     def __init__(self):
#         self._marks=90
# student=Student()
# print(student._marks)

#Protected Instance Variables
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self._marks=marks
# student=Student("Vaishnavi",95)
# print(student.name)
# print(student._marks)

#Accessing Protected Members Outside Class
# class Student:
#     def __init__(self):
#         self._marks=90
# student=Student()
# print(student._marks)

#Protected Methods
# class Bank:
#     def _calculate_interest(self):
#         print("Calculating Interest")
# bank=Bank()
# bank._calculate_interest()

#Protected Members with Inheritance
#Parent Class
# class Animal:
#     def __init__(self):
#         self._sound="Bark"
# #Child Class
# class Dog(Animal):
#     def show_sound(self):
#         print(self._sound)
# dog=Dog()
# dog.show_sound()


#PRIVATE MEMBERS
# class BankAccount:
#     def __init__(self):
#         self.__balance=5000
#     def show_balance(self):
#         print("Balance=",self.__balance)
# account=BankAccount()
# account.show_balance()


# class PrimeCounter:
#     def __init__(self,number):
#         self.number=number
#         self.__factor_count=0
#     def count_factors(self):
#         self.__factor_count=0
#         for i in range(1,self.number+1):
#             if self.number%i==0:
#                 self.__factor_count+=1
#         return self.__factor_count
#     def display_result(self):
#         total=self.count_factors()
#         print(self.number,"has",total,"factors")
# obj=PrimeCounter(28)
# obj.display_result()


# class DigitalLocker:
#     def __init__(self,owner_name,pin):
#         self.owner_name=owner_name
#         self.__locker_pin=pin
#         self.__documents=[]
#     def verify_pin(self,entered_pin):
#         if entered_pin==self.__locker_pin:
#             return True
#     def add_document(self,entered_pin,document):
#         if self.verify_pin(entered_pin):
#             self.__documents.append(document)
#             print("Document Added Successfully")
#         else:
#             print("Incorrect PIN")
#     def view_documents(self,entered_pin):
#         if self.verify_pin(entered_pin):
#             print("Documents:")
#             if len(self.__documents)==0:
#                 print("No Documents Found")
#             else:
#                 for document in self.__documents:
#                     print(document)
#         else:
#             print("Incorrect PIN")
# locker=DigitalLocker("Vaishnavi",4582)
# locker.add_document(4582,"Adhar.pdf")
# locker.add_document(4582,"PAN.pdf")
# locker.add_document(4582,"Marksheet.pdf")
# locker.view_documents(4582)

#PRIVATE METHODS
# class ATM:
#     def __init__(self):
#         self.__balance=5000
#     def __show_balance(self):
#         print("Current Balance=",self.__balance)
#     def display(self):
#         self.__show_balance()
# atm=ATM()
# atm.display()

#Private Method Accessing a Private Variable
# class Student:
#     def __init__(self):
#         self.__marks=95
#     def __show_marks(self):
#         print("Marks=",self.__marks)
#     def display(self):
#         self.__show_marks()
# student=Student()
# student.display()


#One Private Method Calling Another Private Method
# class Calculator:
#     def __add(self):
#         print("Addition")
#     def __subtract(self):
#         print("Subtraction")
#     def calculate(self):
#         self.__add()
#         self.__subtract()
# obj=Calculator()
# obj.calculate()


# class TemperatureConverter:
#     def __init__(self,celsius):
#         self.__celsius=celsius
#     def __convert_to_fahrenheit(self):
#         fahrenheit=(9/5)*self.__celsius+32
#         return fahrenheit
#     def display_temperature(self):
#         fahrenheit=self.__convert_to_fahrenheit()
#         print(f"{self.__celsius}={fahrenheit}")
# converter=TemperatureConverter(25)
# converter.display_temperature()


#ACCESSING PRIVATE MEMBERS INSIDE THE CLASS
# class Student:
#     def __init__(self):
#         self.__marks=95
#     def display_marks(self):
#         print("Marks=",self.__marks)
# student=Student()
# student.display_marks()

#Accessing a Private Method Inside a Public Method
# class Student:
#     def __show_message(self):
#         print("Private Method Called")
#     def display(self):
#         self.__show_message()
# student=Student()
# student.display()

#Accessing a Private Method From The Constructor
# class Greeting:
#     def __init__(self):
#         self.__welcome()
#     def __welcome(self):
#         print("Welcome to Python OOP")
# obj=Greeting()
    

#One Public Method Calling Another Public Method That uses a Private Variable
# class Student:
#     def __init__(self):
#         self.__marks=88
#     def display_marks(self):
#         print("Marks=",self.__marks)
#     def result(self):
#         print("Student Result")
#         self.display_marks()
# student=Student()
# student.result()

#Multiple Methods Sharing One Private Variable
# class Counter:
#     def __init__(self):
#         self.__count=0
#     def increase(self):
#         self.__count+=1
#     def decrease(self):
#         self.__count-=1
#     def show(self):
#         print("Count=",self.__count)
# obj=Counter()
# obj.increase()
# obj.decrease()
# obj.show()


# class Rectangle:
#     def __init__(self):
#         self.__length=int(input("Enter Length:"))
#         self.__width=int(input("Enter Width:"))
#     def __calculate_area(self):
#         area=self.__length*self.__width
#         return area
#     def display_area(self):
#         area=self.__calculate_area()
#         print("Area=",area)
# rectangle=Rectangle()
# rectangle.display_area()


#NAME MANGLING 
# class Bank:
#     def __init__(self):
#         self.__balance=5000
#     def display(self):
#         print(self.__balance)
# account=Bank()
# account.display()

#Looking Inside the Object (__dict__)
# class Bank:
#     def __init__(self):
#         self.__balance=5000
# account=Bank()
# print(account.__dict__)      

#Accessing the Mangled Name
# class Bank:
#     def __init__(self):
#         self.__balance=5000
# account=Bank()
# print(account._Bank__balance)

#Name Mangling for Private Methods
# class Demo:
#     def __hello(self):
#         print("Hello")
#     def show(self):
#         self.__hello()
# obj=Demo()
# obj.show()

#Inspecting Methods
# print(dir(obj))


# class PrimeAnalyzer:
#     def __init__(self):
#         self.__number=int(input("Enter a number:"))
#         self.__factor_count=0
#     def __count_factors(self):
#         self.__factor_count=0
#         for i in range(1,self.__number+1):
#             if self.__number%i==0:
#                 self.__factor_count+=1
#     def show_result(self):
#         self.__count_factors()
#         print("Number=",self.__number)
#         print("Factors=",self.__factor_count)
#         if self.__factor_count==2:
#             print("Prime Number")
#         else:
#             print("Not a Prime Number")
# obj=PrimeAnalyzer()
# obj.show_result()


# class AuthenticationManager:
#     def __init__(self,password):
#         self.__password=password
#         self.__login_attempts=3
#     def login(self,entered_password):
#         if self.__login_attempts==0:
#             print("Account Locked")
#             return
#         if entered_password==self.__password:
#             print("Login Successful")
#             self.__login_attempts=3
#         else:
#             self.__login_attempts-=1
#             print("Incorrect Password")
#             print("Remaining Attempts=",self.__login_attempts)
#             if self.__login_attempts==0:
#                 print("Account Locked")
#     def change_password(self,old_password,new_password):
#         if old_password==self.__password:
#             self.__password=new_password
#             print("Password Changed Succesfully")
#         else:
#             print("Old Password Incorrect")
#     def remaining_attempts(self):
#         print("Remaining Attempts=",self.__login_attempts)
# auth=AuthenticationManager("Python123")
# auth.login("Hello")
# auth.login("Python")
# auth.login("Python123")
# auth.change_password("Python123","NewPass")
# auth.login("NewPass")
# auth.remaining_attempts()    


#NAME MANGLING WITH INHERITANCE
#variable Collision Problem
# class Parent:
#     def __init__(self):
#         self.__value = 100
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__value = 200

# class Parent:
#     def __init__(self):
#         self.__value=100
#     def show_parent(self):
#         print("Parent Value=",self.__value)
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__value=200
#     def show_child(self):
#         print("Child Value=",self.__value)
# obj=Child()
# obj.show_parent()
# obj.show_child()


#Checking with __dict__
# class Parent:
#     def __init__(self):
#         self.__value=100
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__value=200
# obj=Child()
# print(obj.__dict__)


#Name Mangling with Private Methods
# class Parent:
#     def __hello(self):
#         print("Hello from Parent")
#     def parent_show(self):
#         self.__hello()
# class Child(Parent):
#     def __hello(self):
#         print("Hello from Child")
#     def child_show(self):


# class Parent:
#     def __init__(self):
#         self.__a=int(input("Enter Parent Number:"))
#     def show_parent(self):
#         print("Parent Number=",self.__a)
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__a=int(input("Enter Child Number:"))
#     def show_child(self):
#         print("Child Number=",self.__a)
# obj=Child()
# obj.show_parent()
# obj.show_child()
# print("\nobject Dictionary:")
# print(obj.__dict__)        


# class Parent:
#     def __init__(self):
#         self.__account_number="ACC101"
#         self.__balance=5000
#     def show_account(self):
#         print("Account Number=",self.__account_number)
#     def show_parent_balance(self):
#         print("Parent Balance=",self.__balance)

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__balance=1000
#         self.reward_points=250
#     def show_child_balance(self):
#         print("Child Balance=",self.__balance)
#     def show_rewards(self):
#         print("Reward Points=",self.__reward_points)
# obj=Child()
# obj.show_account()
# obj.show_parent_balance()
# obj.show_child_balance()
# obj.show_rewards()
# print("\nobject Dictionary:")
# print(obj.__dict__)


#METHOD OVERRIDING
# class Parent:
#     def show(self):
#         print("Parent")
# class Child(Parent):
#     def show(self):
#         def show(self):
#             print("Child")
# obj=Child()
# obj.show()

#Does This Work for Private Methods
# class Parent:
#     def __hello(self):
#         print("Parent Hello")
#     def parent_show(self):
#         self.__hello()
# class Child(Parent):
#     def __hello(self):
#         print("Child Hello")
#     def child_show(self):
#         self.__hello()
# obj=Child()
# obj.parent_show()
# obj.child_show()


#MULTIPLE INHERITANCE
# class ParentA:
#     def __init__(self):
#         self.__value=100
#     def show_a(self):
#         print("ParentA=",self.__value)
# class ParentB:
#     def __init__(self):
#         self.__value=200
#     def show_b(self):
#         print("ParentB=",self.__value)
# class Child(ParentA,ParentB):
#     def __init__(self):
#         ParentA.__init__(self)
#         ParentB.__init__(self)
# obj=Child()
# obj.show_a()
# obj.show_b()
# print(obj.__dict__)


# class Parent:
#     def __init__(self):
#         self.a=int(input("Enter First Number:"))
#         self.b=int(input("Enter Second Number:"))
#     def __gcd(self):
#         smaller=min(self.a,self.b)
#         gcd=1
#         for i in range(1,smaller+1):
#             if self.a%i==0 and self.b%i==0:
#                 gcd=i
#         return gcd
#     def show_gcd(self):
#         print("GCD=",self.__gcd())
# class Child(Parent):
#     def __lcm(self):
#         smaller=min(self.a,self.b)
#         gcd=1
#         for i in range(1,smaller+1):
#             if self.a%i==0 and self.b%i==0:
#                 gcd=i
#         lcm=(self.a*self.b)//gcd
#         return lcm
#     def show_lcm(self):
#         print("LCM=",self.__lcm())
# obj=Child()
# obj.show_gcd()
# obj.show_lcm()
# print("\nObject Dictionary:")
# print(obj.__dict__)


# class ParentA:
#     def __turn_on_lights(self):
#         print("Lights Turned ON")
#     def activate_lights(self):
#         self.__turn_on_lights()
# class ParentB:
#     def __turn_on_security(self):
#         print("Security System Activated")
#     def activate_security(self):
#         self.__turn_on_security()
# class Child(ParentA,ParentB):
#     def activate_home(self):
#         print("Starting Smart Home.....\n")
#         self.activate_lights()
#         self.activate_security()
# home=Child()
# home.activate_home()
# print("\nMethods Inside CHild Object:")
# for item in dir(home):
#     if "turn_on" in item:
#         print(item)


# class User:
#     def __init__(self):
#         self.__user_id=input("Enter User ID:")
#     def __login(self):
#         print("Login Successful")
#     def login(self):
#         self.__login()
#     def show_user(self):
#         print("User ID :",self.__user_id)
# class Exam:
#     def __init__(self):
#         self.__score=0
#     def __calculate_score(self):
#         print("\nAnswer The Following Quetions")
#         score=0
#         if input("Python is Interpreted language? (yes/no):").lower()=="yes":
#             score+=1
#         if input("5+5= ").strip()=="10":
#             score+=1
#         if input("Keyword to create a class?").lower()=="class":
#             score+=1
#         self.__score=score
#     def submit_exam(self):
#         self.__calculate_score()
#         print("\nFinal Score=",self.__score,"/3")
# class OnlineExam(User,Exam):
#     def __init__(self):
#         User.__init__(self)
#         Exam.__init__(self)
#     def start_exam(self):
#         print("\n===== Online Examination =====")
#         self.login()
#         self.show_user()
#         print("\nExam Started.....\n")
#         self.submit_exam()
# obj = OnlineExam()
# obj.start_exam()
# print("\nObject Dictionary:")
# print(obj.__dict__)
# print("\nPrivate Methods Available:")
# for item in dir(obj):
#     if "login" in item or "calculate" in item:
#         print(item)


#GETTER METHOD
# class ClassName:
#     def __init__(self):
#         self.__Variable=Value 
#     def get_variable(self):
#         return self.__value

# class Student:
#     def __init__(self):
#         self.__marks=95
#     def get_marks(self):
#         return self.__marks
# obj=Student()
# print("Marks=",obj.get_marks())

#Gatter with User Input
# class Student:
#     def __init__(self):
#         self.__name=input("Enter Name:")
#     def get_name(self):
#         return self.__name
# obj=Student()
# print("Student Name=",obj.get_name())

#Multiple Getter Methods
# class Employee:
#     def __init__(self):
#         self.__name="Rahul"
#         self.__salary=50000
#     def get_name(self):
#         return self.__name
#     def get_salary(self):
#         return self.__salary
# emp=Employee()
# print(emp.get_name())
# print(emp.get_salary())


# class NumberInfo:
#     def __init__(self):
#         self.__number=int(input("Enter Number:"))
#         self.__factor_count=self.__count_factors()
#     def __count_factors(self):
#         count=0
#         for i in range(1,self.__number+1):
#             if self.__number%i==0:
#                 count+=1
#         return count
#     def get_number(self):
#         return self.__number
#     def get_factor_count(self):
#         return self.__factor_count
# obj=NumberInfo()
# print("\nNumber=",obj.get_number())
# print("Factor Count=",obj.get_factor_count())         

# class Circle:
#     def __init__(self):
#         self.__radius=float(input("Enter Radius:"))
#     def get_radius(self):
#         return self.__radius
# circle=Circle()
# radius=circle.get_radius()
# area=3.14159*radius*radius
# print("\nRadius=",radius)
# print("Area=",area)


#SETTER METHOD
# class Classmate:
#     def __init__(self):
#         self.__variable=Value 
#     def set_variable(self,new_value):
#         self.__variable=new_value

# class Student:
#     def __init__(self):
#         self.__marks=85
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,new_marks):
#         self.__marks=new_marks
# obj=Student()
# print("Before Update=",obj.get_marks())
# obj.set_marks(95)
# print("After Update=",obj.get_marks())


#Setter With User Input
# class Employee:
#     def __init__(self):
#         self.__salary=30000
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self,salary):
#         self.__salary=salary
# emp=Employee()
# print("Old Salary=",emp.get_salary())
# new_salary=int(input("Enter New Salary:"))
# emp.set_salary(new_salary)
# print("Updated Salary=",emp.get_salary())

#Multiple Setter Methods
# class Student:
#     def __init__(self):
#         self.__name="Rahul"
#         self.__marks=80
#     def get_name(self):
#         return self.__name
#     def get_marks(self):
#         return self.__marks
#     def set_name(self,name):
#         self.__name=name
#     def set_marks(self,marks):
#         self.__marks=marks
# student=Student()
# student.set_name("Vaishnavi")
# student.set_marks(95)
# print(student.get_name())
# print(student.get_marks())

# class BankAccount():
#     def __init__(self,account_number,balance):
#         self.__account_number=account_number
#         self.__balance=balance
#     def get_account_number(self):
#         return self.__account_number
#     def get_balance(self):
#         return self.__balance
#     def set_account_number(self,account_number):
#         self.__account_number=account_number
#     def set_balance(self,balance):
#         self.__balance=balance
# account=BankAccount("ACC1001",5000)
# print("Initial Details")
# print("Account Number:",account.get_account_number())
# print("Blance:",account.get_balance())
# print("\nUpdating Blance....")
# account.set_balance(7500)
# print("\nUpdated details")
# print("Account Number:",account.get_account_number())
# print("Balance:",account.get_balance())


#VALIDATION INSIDE SETTER METHODS
# class Student:
#     def __init__(self):
#         self.__marks=0
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks
#             print("Marks Updated Successfully")
#         else:
#             print("Invalid Marks")
# student=Student()
# student.set_marks(85)
# print("Marks=",student.get_marks())
# student.set_marks(150)
# print("Marks=",student.get_marks())


#Number Range Validation
# class Age:
#     def __init__(self):
#         self.__age=0
#     def set_age(self,age):
#         if 0<=age<=120:
#             self.__age=age
#             print("Age Updated")
#         else:
#             print("Invalid Age")
#     def get_age(self):
#         return self.__age
# obj=Age()
# obj.set_age(25)
# print(obj.get_age())
# obj.set_age(-4)
# print(obj.get_age())

#String Valiadtion
# class Student:
#     def __init__(self):
#         self.__name=""
#     def set_name(self,name):
#         if name.isalpha():
#             self.__name=name
#             print("Name Updated")
#         else:
#             print("Invalid Name")
#     def get_name(self):
#         return self.__name
# student=Student()
# student.set_name("Vaishnavi")
# print(student.get_name())
# student.set_name("Vaishnavi123")
# print(student.get_name())


#Length Validation
# class Phone:
#     def __init__(self):
#         self.__phne=""
#     def set_phone(self,phone):
#         if len(phone)==10 and phone.isdigit():
#             self.__phone=phone
#             print("Phone Saved")
#         else:
#             print("Invalid Phone")
#     def get_phone(self):
#         return self.__phone
# obj=Phone()
# obj.set_phone("9876543218")
# print(obj.get_phone())
# obj.set_phone("1234")
# print(obj.get_phone())


#Choice Validation
# class Student:
#     def __init__(self):
#         self.__branch=""
#     def set_branch(self,branch):
#         if branch in ["CSE","ECE","ME","CE"]:
#             self.__branch=branch
#             print("Branch Updated")
#         else:
#             print("Invalid Branch")
#     def get_branch(self):
#         return self.__branch
# student=Student()
# student.set_branch("ECE")
# print(student.get_branch())
# student.set_branch("MBA")
# print(student.get_branch())  


#@PROPERTY
# class Student:
#     def __init__(self):
#         self.__marks=95
#     @property
#     def marks(self):
#         return self.__marks
# student=Student()
# print(student.marks)


#@property with setter
# class Student:
#     def __init__(self):
#         self.__marks=0
#     @property
#     def marks(self):
#         return self.__marks
#     @marks.setter
#     def marks(self,value):
#         self.__marks=value
# student=Student()
# student.marks=85
# print(student.marks)


#Validation with @property
# class Student:
#     def __init__(self):
#         self.__marks=0
#     @property
#     def marks(self):
#         return self.__marks
#     @marks.setter
#     def marks(self,value):
#         if 0<=value<=100:
#             self.__marks=value
#         else:
#             print("Invalid Marks")
# student=Student()
# student.marks=90
# print(student.marks)
# student.marks=150
# print(student.marks)


#Multiple Properties
# class Employee:
#     def __init__(self):
#         self.__name=""
#         self.__salary=0
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self,value):
#         self.__salary=value
# emp=Employee()
# emp.name="Vaishnavi"
# emp.salary=50000
# print(emp.name)
# print(emp.salary)    


#READ ONLY OBJECTS
# class Student:
#     def __init__(self,roll):
#         self.__roll=roll
#     @property
#     def roll(self):
#         return self.__roll
# student=Student(101)
# print("Roll Number=",student.roll)

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.__account_number=account_number
#         self.__balance=balance
#     @property
#     def account_number(self):
#         return self.__account_number
#     @property 
#     def balance(self):
#         return self.__balance
#     @balance.setter
#     def balance(self,amount):
#         if amount>=0:
#             self.__balance=amount
#         else:
#             print("Invalid Balance")
# account=BankAccount("ACC1001",5000)
# print("Account Number=",account.account_number)
# print("Balance=",account.balance)
# account.balance=8000
# print("Updated Balance=",account.balance)

#Multiple REad Only Properties
# class Employee:
#     def __init__(self,emp_id,joining_year):
#         self.__emp_id=emp_id
#         self.__joining_year=joining_year
#     @property
#     def emp_id(self):
#         return self.__emp_id
#     @property
#     def joining_year(self):
#         return self.__joining_year
# emp=Employee("EMP101",2025)
# print(emp.emp_id)
# print(emp.joining_year)


#WRITE ONLY OBJECTS
# class ATM:
#     def __init__(self):
#         self.__pin=""
#     @property
#     def pin(self):
#         raise AttributeError("PIN is write-only.")
#     @pin.setter
#     def pin(self,value):
#         self.__pin=value
#         print("PIN Updated Successfully")
# atm=ATM()
# atm.pin="1234"

#Password Example
# class User:
#     def __init__(self):
#         self.__password=""
#     @property
#     def password(self):
#         raise AttributeError("Password cannot be viewed")
#     @password.setter
#     def password(self,value):
#         self.__password=value
#         print("Password Changed")
# user=User()
# user.password="Python@123"

#API Key
# class API:
#     def __init__(self):
#         self.__secret=""
#     @property
#     def secret(self):
#         raise AttributeError("Secret key is Write-Only.")
#     @secret.setter
#     def secret(self,key):
#         self.__secret=key

#OTP
# class Otp:
#     def __init__(self):
#         self.__otp=""
#     @property
#     def otp(self):
#         raise AttributeError("OTP cannot be read.")
#     @otp.setter
#     def otp(self,value):
#         self.__otp=value

# class Vault:
#     def __init__(self,vault_number):
#         self.__vault_number=vault_number
#         self.__unlock_key=None
#     @property
#     def vault_number(self):
#         return self.__vault_number
#     @property
#     def unlock_key(self):
#         raise AttributeError("Unlock key is write-only.")
#     @unlock_key.setter
#     def unlock_key(self,key):
#         if self.__is_prime(key) and 1000<=key<=9999:
#             self.__unlock_key=key
#             print("Unlock Key Saved Succesfuly")
#         else:
#             print("Invalid Unlock Key")
#     def __is_prime(self,number):
#         if number<2:
#             return False
#         for i in range(2,int(number**0.5)+1):
#             if number%i==0:
#                 return False
#         return True
#     def unlock(self,entered_key):
#         if entered_key==self.__unlock_key:
#             print("Vault Opened")
#         else:
#             print("Access Denied")
# vault=Vault("V101")
# print("Vault Number=",vault.vault_number)
# key=int(input("Create Unlock Key:"))
# vault.unlock_key=key
# entered=int(input("Enter Unlock Key:"))
# vault.unlock(entered)

# class AuthenticationManager:
#     def __init__(self,user_id):
#         self.__user_id=user_id
#         self.__password=""
#     @property
#     def user_id(self):
#         return self.__user_id
#     @property
#     def password(self):
#         raise AttributeError("Password is write-only.")
#     @password.setter
#     def password(self,value):
#         self.__password=value
#         print("Password Saved Successfully")
#     def login(self,entered_password):
#         return entered_password==self.__password
# auth=AuthenticationManager("USER101")
# print("User ID:",auth.user_id)
# password=input("Create Password:")
# auth.password=password
# print()
# login_password=input("Enter Password to Login:")
# if auth.login(login_password):
#     print("Login Successful")
# else:
#     print("Invalid Password")


#READ-WRITE OBJECTS
# class Employee:
#     def __init__(self):
#         self.__value=0
#     @property
#     def value(self):
#         return self.__value
#     @value.setter
#     def value(self,new_value):
#         self.__value=new_value

# class Student:
#     def __init__(self):
#         self.__cgpa=8.0
#     @property
#     def cgpa(self):
#         return self.__cgpa
#     @cgpa.setter
#     def cgpa(self,value):
#         if 0<=value<=10:
#             self.__cgpa=value
#             print("CGPA UPdated Sucessfully")
#         else:
#             print("Invalid CGPA")
# student=Student()
# print("Current CGPA:",student.cgpa)
# student.cgpa=8.7
# print("Updated CGPA:",student.cgpa)


# class Employee:
#     def __init__(self):
#         self.__salary=40000
#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self,amount):
#         if amount>=0:
#             self.__salary=amount
#         else:
#             print("Invalid Salary")
# emp=Employee()
# print(emp.salary)
# emp.salary=55000
# print(emp.salary)

# class Product:
#     def __init__(self):
#         self.__price=100
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self,value):
#         if value>0:
#             self.__price=value
#         else:
#             print("Invalid Price")
# item=Product()
# print(item.price)
# item.price=150
# print(item.price)

# class Temperature:
#     def __init__(self):
#         self.__celsius=25
#     @property
#     def celsius(self):
#         return self.__celsius
#     @celsius.setter
#     def celsius(self,value):
#         if value>=-273.15:
#             self.__celsius=value
#         else:
#             print("Temperature belw absolute zero is not possible")
# temp=Temperature()
# print(temp.celsius)
# temp.celsius=35
# print(temp.celsius)


# class WarehouseItem:
#     def __init__(self,item_id,quantity):
#         self.__item_id=item_id
#         self.__quantity=0
#         self.quantity=quantity
#     @property
#     def item_id(self):
#         return self.__item_id
#     @property
#     def quantity(self):
#         return self.__quantity
#     @quantity.setter
#     def quantity(self,value):
#         if value>=0:
#             self.__quantity=value
#         else:
#             print("Invalid quantity")
#     def add_stock(self,amount):
#         if amount>0:
#             self.quantity=self.quantity+amount
#             print("Stock Added Successfully")
#         else:
#             print("Invalid Amount")
#     def remove_stock(self,amount):
#         if amount>0 and amount<=self.quantity:
#             self.quantity=self.quantity-amount
#             print("Stock Removed Successfully")
#         else:
#             print("Invalid Amount or Insufficient Stock")
# item=WarehouseItem("ITEM101",50)
# print("Item ID:",item.item_id)
# print("Initial Quantity:",item.quantity)
# item.add_stock(30)
# print("Quantity:",item.quantity)
# item.remove_stock(20)
# print("Quantity:",item.quantity)
# print("Final Quantity:",item.quantity)


# class GameCharacter:
#     def __init__(self,character_id,health):
#         self.__character_id=character_id
#         self.__health=health
#     @property
#     def character_id(self):
#         return self.__character_id
#     @property
#     def character_id(self):
#         return self.__character_id
#     @property
#     def health(self,value):
#         if 0<=value<=100:
#             self.__health=value
#         else:
#             print("Invalid Health")
#     def heal(self,points):
#         if points>0:
#             new_health=self.health+points
#             if new_health<=100:
#                 self.health=new_health
#                 print("Character Healed")
#             else:
#                 self.health=100
#                 print("Health Capped at 100")
#         else:
#             print("Invalid Heal Amount")
#     def take_damage(self,points):
#         if points>0:
#             new_health=self.health-points
#             if new_health>=0:
#                 self.health=new_health


#PROPERTY IN INHERITANCE
# class Person:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return self.__name
# class Student(Person):
#     pass
# student=Student("Vaishnavi")
# print(student.name)

#Inherited Setter
# class Person:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
# class Student(Person):
#     pass
# student=Student("Vaishnavi")
# print(student.name)
# student.name="Rahul"
# print(student.name)

#REad Only Property in Parent
# class Person:
#     def __init__(self,person_id):
#         self.__person_id=person_id
#     @property
#     def person_id(self):
#         return self.__person_id
# class Student(Person):
#     pass
# student=Student(101)
# print(student.person_id)

#Child Can Override the Property
# class Person:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return self.__name
# class Student(Person):
#     @property
#     def name(self):
#         return "Student:" + self._Person__name
# student=Student("Vaishnavi")
# print(student.name)

#Getter Overriding
# class Person:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return self.__name
# class Student(Person):
#     @property
#     def name(self):
#         return "Student-" + self._Person__name
# student=Student("Vaishnavi")
# print(student.name)

#Better Design Using super()
# class Person:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return self.__name
# class Student(Person):
#     @property
#     def name(self):
#         return "Student:"+super().name
# student=Student("Vaishnavi")
# print(student.name)

#Overriding the Setter
# class Person:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
# class Student:
#     @property
#     def name(self):
#         return super().name
#     @name.setter
#     def name(self,value):
#         if value.replace(" "," ").isalpha():
#             super(Student,Student).name.__set__(self,value)
#         else:
#             print("Invalid Name")

#Getter+Setter Both Overridden
class Person:
    def __init__(self,age):
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age=value
class Student(Person):
    @property
    def age(self):
        return "Student Age:"+str(self._Person__age)
    @age.setter
    def age(self,value):
        if value>=5:
            self._Person__age=value
        else:
            print("Invalid Age")