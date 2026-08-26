#ACCESSING CLASS VARIABLES INSIDE DIFFERENT TYPES OF METHODS
# class Student:
#     school="ABC school"
#     def __init__(self,name):
#         self.name=name
#     def sow(self):
#         print(self.school)

# #accessing inside class method
# class Student:
#     school="ABC school"
#     @classmethod
#     def show_school(cls):
#         print(cls.school)
# Student.show_school()

#accessing inside a static method
# class Student:
#     school="ABC school"
#     @staticmethod
#     def show_school():
#         print(Student.school)
# Student.show_school()

#CLASS METHOD
#SYNTAX
# class Classmate:
#     @classmethod #decorator
#     def method_name(cls): #current class
        #code

# class Student:
#     school="ABC school"
#     @classmethod
#     def show_school(cls):
#         print(cls.school)
# Student.show_school()

#can a class method access class variable
# class Company:
#     company_name="OpenAI"
#     @classmethod
#     def show_company(cls):
#         print(cls.company_name)
# Company.show_company()

# class Game:
#     game_name="chess"
#     @classmethod
#     def show_game(cls):
#         print(cls.game_name)
# Game.show_game()

#ACCESSING CLASS VARIABLES INSIDE CLASS METHODS
# class Student:
#     school="ABC school"
#     @classmethod
#     def show_school(cls):
#         print("School:",cls.school)
# Student.show_school()

#accessing more than one class variables
# class Company:
#     company_name="OpenAI"
#     country="USA"
#     @classmethod
#     def show_details(cls):
#         print("Company:",cls.company_name)
#         print("Country:",cls.country)
# Company.show_details()

#MODIYING CLASS VARIABLES INSIDE CLASS METHODS
# class Student:
#     school="ABC school"
#     @classmethod
#     def change_school(cls):
#         cls.school="XYZ school"
# s1=Student()
# s2=Student()
# Student.change_school()
# print(s1.school)
# print(s2.school)
# print(Student.school) 

#modifying multiple class variables
# class Company:
#     company_name="OpenAI"
#     country="USA"
#     @classmethod
#     def update_details(cls):
#         cls.company_name="OpenAI India"
#         cls.company="India"

# Company.update_details()
# print(Company.company_name)
# print(Company.country)

# class University:
#     university_name="Delhi University"
#     city="Delhi"
#     @classmethod
#     def update_details(cls):
#         cls.university_name="IIT Delhi"
#         cls.city="hauz khas"
# University.update_details()
# print(University.university_name)
# print(University.city)

#USING CLASS METHODS AS ALTERNATIVE CONSTRUCTORS
#syntax
# @classmethod
# def from_something(cls,data):
#     .....
#     return cls(....)

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def from_string(cls,data):
#         name,age=data.split("-")
#         return cls(name,int(age))

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     @classmethod
#     def from_square(cls,side):
#         return cls(side,side)    
# square=Rectangle.from_square(5)
# print(square.length)
# print(square.width)

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def from_string(cls,data):
#         name,salary=data.split("-")
#         return cls(name,int(salary))
# emp=Employee.from_string("Rahul-50000")    

# class Student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     @classmethod
#     def from_string(cls,data):
#         name,age,course=data.split("-")
#         return cls(name,int(age),course)
# Student.from_string("Vaishnavi-20-electronic and communication")

#MULTIPLE ALTERNATIVE CONSTRUCTORS IN ONE CLASS
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def from_string(cls,data):
#         name,age=data.split("-")
#         return cls(name,int(age))
#     @classmethod
#     def from_list(cls,data):
#         return cls(data[0],data[1])
#     @classmethod
#     def default_student(cls):
#         return cls("Unknown",18)
# s1=Student("Vaishnavi",20)
# s2=Student.from_string("Rahul-21")
# s3=Student.from_list(
#     ["Priya",19]
# )
# s4=Student.default_student()

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     @classmethod
#     def from_square(cls,side):
#         return cls(side,side)
#     @classmethod
#     def default_rectangle(cls):
#         return cls(1,1)
# r1=Rectangle(10,5)
# r2=Rectangle.from_square(8)
# r3=Rectangle.default_rectangle()
# print(r1.length,r1.width)


# class Product:
#     def __init__(self,name,price,quality):
#         self.name=name
#         self.price=price
#         self.quality=quality
#     @classmethod
#     def from_string(cls,data):
#         name,price,quality=data.split("-")
#         return cls(name,int(price),int(quality))
#     @classmethod
#     def from_list(cls,data):
#         return cls(data[0],data[1],data[2])
#     @classmethod
#     def from_dictionary(cls,data):
#         return cls(
#             data["name"],
#             data["price"],
#             data["quality"]
#         )
#     @classmethod
#     def default_product(cls):
#         return cls("Unknown",0,0)
    
#     def display(self):
#         print("Name     :",self.name)
#         print("Price    :",self.price)
#         print("Quality   :",self.quality)

# p1=Product("Laptop",65000,5)
# p2=Product.from_string("Mouse-500-20")
# p3=Product.from_list(["Keyboard",1200,10])
# p4=Product.from_dictionary({
#     "name":"Monitor",
#     "price":12000,
#     "quality":3
# })
# p5=Product.default_product

# p1.display()
# print()

# p2.display()
# print()

# p3.display()
# print()

# p4.display()
# print()

# p5.display()
# print()

#CLASS METHODS VS INSTANCE METHODS VS STATIC METHODS 
# class Bank:
#     interest_rate=7
#     @classmethod
#     def update_rate(cls,rate):
#         cls.interest_rate=rate
# Bank.update_rate(8)
# Bank.interest_rate

# class Maths:
#     @staticmethod
#     def square(x):
#         return x*x
# Maths.square(5)

# class Student:
#     school="ABC school"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print(self.name,self.marks)

#     @classmethod
#     def change_school(cls,new_name):
#         cls.school=new_name

#     @staticmethod
#     def is_pass(mark):
#         return mark>=40
# s=Student("Vaishnavi",92)
# s.display()
# Student.change_school("XYZ school")
# print(Student.is_pass(92))
    

# class NumberUtils:
#     @staticmethod
#     def is_armstrong(number):
#         original=number
#         digits=len(str(number))
#         total=0
#         while number>0:
#             digit=number%10
#             total+=digit**digits
#             number//=10
#         return total==original
# print(NumberUtils.is_armstrong(153))

# class Mathtool:
#     @staticmethod
#     def gcd(a,b):
#         while b!=0:
#             a,b=b,a%b
#         return a
# print(Mathtool.gcd(48,18))

# class Primeanalyzer:
#     def __init__(self,number):
#         self.number=number
#     def is_prime(self):
#         if self.number<=1:
#             return "Not Prime"
#         for i in range(2,self.number):
#             if self.number%i==0:
#                 return "Not Prime"
#         return "Prime"
# obj=Primeanalyzer(29)
# print(obj.is_prime())

# class Calculator:
#     @staticmethod
#     def add(a,b):
#         return a+b
# Calculator.add(10,20)

# class Calculator:
#     precision=2
#     @classmethod
#     def set_precision(cls,value):
#         cls.precision=value
# Calculator.set_precision(4)

# class Calculator:
#     def display_history(self):
#         print(self.history)
# obj.display_history()


# class Bankaccount:
#     def deposit(self,amount):
#         self.balance+=amount

# class Bankaccount:
#     minimum_balance=1000
#     @classmethod
#     def change_minimum_balance(cls,amount):
#         cls.minimum_balance=amount

# class Bankaccount:
#     @staticmethod
#     def is_valid_ifsc(ifsc):

#CLASS METHOD VS INSTANCE METHOD
# class Student:
#     school="ABC school"
#     @classmethod
#     def change_school(cls,new_name):
#         cls.school=new_name
# Student.change_school("XYZ school")

#can a instance method access class variables
# class Student:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)
#         print(Student.school)
# s=Student("Vaishnavi")
# s.display()

# class Student:
#     def study(self):
#         print("Studying")
#     def start(self):
#         print("Starting...")
#         self.study()
# s=Student()
# s.start()

#can a class method call an instance method
# class Student:
#     def greet(self):
#         print("Hello")
#     @classmethod
#     def start(cls):
#         obj=cls()
#         obj.greet()

#can an instance method call a static method
# class Maths:
#     @staticmethod
#     def square(x):
#         return x*x
#     def display(self):
#         print(Maths.square(5))
# obj=Maths()
# obj.display()

#can a class method call a static method
# class Math:
#     @staticmethod
#     def cube(x):
#         return x**3
#     @classmethod
#     def show(cls):
#         print(Math.cube(3))
# Math.show()

#can s static method call another static method
# class Math:
#     @staticmethod
#     def square(x):
#         return x*x
#     @staticmethod
#     def cube(x):
#         return Math.square(x)*x
# Math.cube(4)

#can a static method call an instance method directly
# class Student:
#     def show(self):
#         print("Hello")
#     @staticmethod
#     def start():
#         obj=Student()
#         obj.show()

#can a staticmethod call a class method
# class Student:
#     school="ABC"
#     @classmethod
#     def show_school(cls):
#         print(cls.school)
#     @staticmethod
#     def display():
#         Student.show_school()
# Student.display()

# class Numbertheory:
#     def __init__(self,number):
#             self.number=number
#     @staticmethod
#     def proper_divisors(number):
#         divisors=[]
#         for i in range(1,number):
#             if number%i==0:
#                 divisors.append(i)
#         return divisors

#     def is_perfect(self):
#          divisors=Numbertheory.proper_divisors(self.number)
#          if sum(divisors)==self.number:
#               return "Perfect Number"
#          return "Not Perfect Number"
# obj=Numbertheory(28)
# print(obj.is_perfect())

# class Mathalgorithms:
#     modulo=1000000007
#     @classmethod
#     def change_modulo(cls,value):
#         cls.modulo=value
#     @staticmethod
#     def power(base,exponent,modulo):
#         result=1
#         while exponent>0:
#             if exponent%2==1:
#                 result=(result*base)%modulo
#             base=(base*base)%modulo
#             exponent//=2
#         return result
# Mathalgorithms.change_modulo(998244353)
# print(
#     Mathalgorithms.power(
#         2,
#         10,
#         Mathalgorithms.modulo
#     )
# )

# class Primestatistics:
#     def __init__(self,numbers):
#         self.numbers=numbers
#     @staticmethod
#     def is_prime(number):
#         if number<=1:
#             return False
#         for i in range(2,number):
#             if number%i==0:
#                 return False
#         return True
#     def count_primes(self):
#         count=0
#         for number in self.numbers:
#             if Primestatistics.is_prime(number):
#                 count+=1
#         return count
# obj=Primestatistics([2,3,4,5,6,7])
# print(obj.count_primes())

# class Matrixcalculator:
#     default_size=2
#     def __init__(self,matrix):
#         self.matrix=matrix
#     @staticmethod
#     def multiply_numbers(a,b):
#         return a*b
#     def matrix_sum(self):
#         total=0
#         for row in self.matrix:
#             for value in row:
#                 total+=value
#         return total
#     @classmethod
#     def change_size(cls,size):
#         cls.default_size=size
# obj=Matrixcalculator([[1,2],[3,4]])
# obj.matrix_sum()
# Matrixcalculator.multiply_numbers(8,5)
# Matrixcalculator.change_size(5)
# Matrixcalculator.default_size

# class Cryptoutility:
#     algorithm="AES"
#     def __init__(self,key):
#         self.key=key
#     def encrypt(self,text):
#     @classmethod
#     def change_algorithm(cls,new_algorithm):
#         cls.algorithm=new_algorithm
#     @staticmethod
#     def to_hex(text):

# obj1=Cryptoutility("ABC123")
# obj2=Cryptoutility("XYZ789")
# Cryptoutility.change_algorithm("RSA")
# Cryptoutility.to_hex("HELLO")

