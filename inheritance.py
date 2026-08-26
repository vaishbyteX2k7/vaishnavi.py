# class Animal:
#     def eat(self):
#         print("Animal is Eating")
# class Dog(Animal):
#     pass
# dog=Dog()
# dog.eat()

#Adding Child-Speicific Behavior
# class Animal:
#     def eat(self):
#         print("Animal Is Eating")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is Barking")
# dog=Dog()
# dog.eat()
# dog.bark()

# class Vehicle:
#     def start(self):
#         print("Vehicle Started")
#     def stop(self):
#         print("Vehicle Stopped")
# class Car(Vehicle):
#     def drive(self):
#         print("Car is Driving")
# car=Car()
# car.start()
# car.drive()
# car.stop()

# class Employee:
#     def work(self):
#         print("Employee is Working")
# class Developer(Employee):
#     def write_code(self):
#         print("Developer is writing code")
# class Designer(Employee):
#     def design(self):
#         print("Designer is Designing")
# developer=Developer()
# designer=Designer()
# developer.work()
# developer.write_code()
# designer.work()
# designer.design()

#Child uses Parent Funtionality
# class Vehicle:
#     def start(self):
#         print("Vehicle Stared")
# class Car(Vehicle):
#     def drive(self):
#         print("Car is Driving")
# car=Car()
# car.start()
# car.drive()

#Child can Add New Functionality
# class Animal:
#     def eat(self):
#         print("Eating")
# class Dog(Animal):
#     def bark(self):
#         print("Barking")

# class Person:
#     def introduce(self):
#         print("I Am A Person")
# class Student(Person):
#     def study(self):
#         print("I AM Studying")
# student=Student()
# student.introduce()
# student.study()

# class Employee:
#     def __init__(self,name):
#         self.name=name
#     def work(self):
#         print(self.name,"is working")
# class Developer(Employee):
#     def write_code(self):
#         print(self.name,"is writing code")
# class Designer(Employee):
#     def design(self):
#         print(self.name,"is designing")
# developer=Developer("Vaishnavi")
# designer=Designer("Anaya")
# developer.work()
# developer.write_code()
# designer.work()
# designer.design()


# class Number:
#     def is_prime(self,n):
#         if n<2:
#             return False
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 return False
#         return True
# class PrimeAnalyzer(Number):
#     def count_primes(self,start,end):
#         count=0
#         for number in range(start,end+1):
#             if self.is_prime(number):
#                 count+=1
#         return count
# start,end=map(int,input("Enter Start and end:").split())
# analyzer=PrimeAnalyzer()
# result=analyzer.count_primes(start,end)
# print("Prime count:",result)
    
# class MathOperations:
#     def gcd(self,a,b):
#         while b!=0:
#             a,b=b,a%b
#         return a
# class NumberAnalyzer(MathOperations):
#     def analyze(self,a,b):
#         gcd_value=self.gcd(a,b)
#         lcm_value=(a*b)//gcd_value
#         print("GCD:",gcd_value)
#         print("LCM:",lcm_value)
# a,b=map(int,input("Enter two numbers:").split())
# analyzer=NumberAnalyzer()
# analyzer.analyze(a,b)


# class NumberTool:
#     def is_prime(self,n):
#         if n<2:
#             return False
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 return False
#         return True
# class SpecialNumberCounter(NumberTool):
#     def count_primes(self,numbers):
#         count=0
#         for number in numbers:
#             if self.is_prime(number):
#                 count+=1
#         return count
# n=int(input())
# numbers=list(map(int,input().split()))
# counter=SpecialNumberCounter()
# result=counter.count_primes(numbers) 
# print("Prime Count:",result)   


#SINGLE INHERITANCE
# class Person:
#     def introduce(self):
#         print("I am a Person")
# class Student(Person):
#     def study(self):
#         print("I am Studying")
# student=Student()
# student.introduce()
# student.study()

#Child Can Add Its Own Methods
# class Animal:
#     def eat(self):
#         print("Eating")
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
# dog=Dog()
# dog.eat()
# dog.bark()

#Inherited Attribute
# class Person:
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def study(self):
#         print(self.name,"is Studying")
# student=Student("Vaishnavi")
# student.study()

#Single Inheritance With Constructor
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def introduce(self):
#         print("Name:",self.name)
# class Student(Person):
#     def __init__(self,name,course):
#         self.name=name
#         self.course=course
#     def study(self):
#         print(self.name,"is studying",self.course)
# student=Student("Vaishnavi","BTech")
# student.introduce()
# student.study()

#SUPER() 
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def introduce(self):
#         print("Name:",self.name)
# class Student(Person):
#     def __init__(self,name,course):
#         super().__init__(name)
#         self.course=course
#     def study(self):
#         print(self.name,"is studying",self.course)
# student=Student("Vaishnavi","BTech")
# student.introduce()
# student.study()


#CONSTRUCTOR BEHAVIOR IN SINGLE INHERITANCE
#Parent Constructor + Child Without Constructor
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def introduce(self):
#         print("Name:",self.name)
# class Student(Person):
#     def study(self):
#         print(self.name,"is studying")
# student=Student("Vaishnavi")
# student.introduce()
# student.study()

#Child Class mein Constructor Add karein
class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,course):
        self.course=course
student=Student("BTech")

#Parent Constructor Call
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def introduce(self):
#         print("Name:",self.name)
# class Student(Person):
#         def __init__(self,name,course):
#             super().__init__(name)
#             self.course=course
#         def study(self):
#             print(self.name,"is Studying",self.course)
# student=Student("Vaishnavi","Btech")
# student.introduce()
# student.study()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def __init__(self,name,age,course,roll_no):
#         super().__init__(name,age)
#         self.course=course
#         self.roll_no=roll_no
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Course:",self.course)
#         print("Roll No:",self.roll_no)
# student=Student("Vaishnavi",20,"Btech",101)
# student.display()

# class Parent:
#     def __init__(self,x):
#         self.x=x
# class Child(Parent):
#     def __init__(self,x,y):
#         super().__init__(x)
#         self.y=y
# obj=Child(10,20)

#Praent Constructor Inheritance
# class Parent:
#     def __init__(self,x):
#         self.x=x
# class Child(Parent):
#     pass
# obj=Child(10)
# print(obj.x)

#Child Gets Its Own Constructor
# class Parent:
#     def __init__(self,x):
#         self.x=x
# class Child(Parent):
#     def __init__(self,y):
#         self.y=y
# obj=Child(20)
# print()

#Parent Constructor Call Manually
# class Parent:
#     def __init__(self,x):
#         self.x=x
# class Child(Parent):
#     def __init__(self,x,y):
#         super().__init__(x)
#         self.y=y
# obj=Child(10,20)

#Different Parameter In Praent And Child
# class Parent:
#     def __init__(self,value):
#         self.value=value
# class Child(Parent):
#     def __init__(self,number,square):
#         super().__init__(number)
#         self.square=square
# obj=Child(5,25)

#Default Paramter in Parent
# class Parent:
#     def __init__(self,x=10):
#         self.x=x
# class Child(Parent):
#     def __init__(self,y):
#         super().__init__()
#         self.y=y
# obj=Child(20)

#Passing a Different Value
# class Parent:
#     def __init__(self,x=10):
#         self.x=x
# class Child(Parent):
#     def __init__(self,x,y):
#         super().__init__(x)
#         self.y=y
# obj=Child(50,20)


# class Number:
#     def __init__(self,value):
#         self.value=value
# class SquareNumber(Number):
#     def __init__(self,value):
#         super().__init__(value)
#     def square(self):
#         return self.value*self.value
# number=int(input("Enter a number:"))
# obj=SquareNumber(number)
# print("Square:",obj.square())


# class NumberTool:
#     def __init__(self,number):
#         self.number=number
# class SquareCecker(NumberTool):
#     def __init__(self,number):
#         super().__init__(number)
#     def is_perfect_square(self):
#         if self.number<0:
#             return False
#         i=0
#         while i*i<=self.number:
#             if i*i==self.number:
#                 return True
#             i+=1
#         return False
# number=int(input("Enter Number:"))
# obj=SquareCecker(number)
# if obj.is_perfect_square():
#     print(number,"is a perfect square")
# else:
#     print(number,"is not a perfect square")
            

# class Number:
#     def __init__(self,number):
#         self.number=number
# class NumberAnalyzer(Number):
#     def __init__(self,number):
#         super().__init__(number)
#     def square(self):
#         return self.number*self.number
#     def cube(self):
#         return self.number**3
#     def is_even(self):
#         return self.number%2==0
#     def is_prime(self):
#         if self.number<2:
#             return False
#         i=2
#         while i*i<=self.number:
#             if self.number%i==0:
#                 return False
#             i+=1
#             return True
#     def digit_sum(self):
#         n=abs(self.number)
#         total=0
#         while n>0:
#             digit=n%10
#             total+=digit
#             n//=10
#         return total
#     def display(self):
#         print("Number:",self.number)
#         print("Square:",self.square())
#         print("Cube:",self.cube())
#         print("Even:",self.is_even())
#         print("Prime:",self.is_prime())
#         print("Digit Sum:",self.digit_sum())
# number=int(input("Enter number:"))
# analyzer=NumberAnalyzer(number)
# analyzer.display()


#SUPER()

#Parent Constructor call syntax
#super().__init__()

#Parent Method Call syntax
#super().method_name()

# class Person:
#     def introduce(self):
#         print("I am a Person") 
# class Student(Person):
#     def introduce(self):
#         super().introduce()
#         print("I am a Student")
# student=Student()
# student.introduce()

#Parent can have Multiple Methods
# class Person:
#     def introduce(self):
#         print("I am a person")
#     def walk(self):
#         print("Person is walking")
# class Student(Person):
#     def show(self):
#         super().introduce()
#         super().walk()
#         print("Student is studying")
# student=Student()
# student.show()

#Parent Constructor + Multiple Parent Methods
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def introduce(self):
#         print("Name:", self.name)
#     def walk(self):
#         print(self.name, "is walking")
# class Student(Person):
#     def __init__(self, name, course):
#         super().__init__(name)
#         self.course = course
#     def show(self):
#         super().introduce()
#         super().walk()
#         print("Course:", self.course)
# student = Student("Vaishnavi", "BTech")
# student.show()

# class Number:
#     def __init__(self,number):
#         self.number=number
#     def display_number(self):
#         print("Number:",self.number)
# class NumberAnalyzer(Number):
#     def square(self):
#         return self.number**2
#     def display(self):
#         super().display_number()
#         print("Square:",self.square())
# number=int(input("Enter number:"))
# obj=NumberAnalyzer(number)
# obj.display()

#CONSTRUCTOR CHAINING IN SINGLE HERITANCE
# class Parent:
#     def __init__(self, x):
#         self.x = x
# class Child(Parent):
#     def __init__(self, x, y):
#         super().__init__(x)
#         self.y = y

#Default Value
# class Person:
#     def __init__(self, name, country="India"):
#         self.name = name
#         self.country = country
# class Student(Person):
#     def __init__(self, name, course):
#         super().__init__(name)
#         self.course = course
# student = Student("Vaishnavi", "BTech")
# print(student.name)
# print(student.country)
# print(student.course)

#Passing a Different Default Value
# class Person:
#     def __init__(self, name, country="India"):
#         self.name = name
#         self.country = country
# class Student(Person):
#     def __init__(self, name, course, country):
#         super().__init__(name, country)
#         self.course = course
# student = Student("Vaishnavi", "BTech", "Nepal")

#Constructor Chaining With Methods
# class Number:
#     def __init__(self, number):
#         self.number = number
#     def show_number(self):
#         print("Number:", self.number)
# class NumberAnalyzer(Number):
#     def __init__(self, number):
#         super().__init__(number)
#     def show_square(self):
#         print("Square:", self.number ** 2)
# obj = NumberAnalyzer(8)
# obj.show_number()
# obj.show_square()

#Multiple Level Constructor Chaining 
# class A:
#     def __init__(self):
#         print("A constructor")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B constructor")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("C constructor")
# obj=C()

# class Number:
#     def __init__(self,number):
#         self.number=number
# class FactorialAnalyzer(Number):
#     def __init__(self,number):
#         super().__init__(number)
#     def factorial(self):
#         result=1
#         for i in range(1,self.number+1):
#             result=result*i
#         return result
# number=int(input("Enter Number:"))
# obj=FactorialAnalyzer(number)
# print("Number:",obj.number)
# print("Factorial:",obj.factorial())


#MULTILEVEL INHERITANCE
# class A:
#     def show_a(self):
#         print("Class A")
# class B(A):
#     def show_b(self):
#         print("Class B")
# class C(B):
#     def show_c(self):
#         print("Class C")
# obj=C()
# obj.show_a()
# obj.show_b()
# obj.show_c()

#Multilevel inheritance with Constructors
# class Person:
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def __init__(self,name,roll_no):
#         super().__init__(name)
#         self.roll_no=roll_no
# class EngineeringStudent(Student):
#     def __init__(self,name,roll_no,branch):
#         super().__init__(name,roll_no)
#         self.branch=branch
# student=EngineeringStudent(
#     "Vaishnavi",
#     101,
#     "ECE"
# )
# print(student.name)
# print(student.roll_no)
# print(student.branch)

#can Parent Access Child Methods?
# class A:
#     def method_a(self):
#         print("A")
# class B(A):
#     def method_b(self):
#         print("B")
# obj=A()

#Can Middle Level Class Access Bottom Level Methods
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     def method_c(self):
#         print("C")
# obj=B()

#MultiLevel Inheitance + Super()
# class Number:
#     def __init__(self,number):
#         self.number=number
#     def display_number(self):
#         print("Number:",self.number)
# class EvenOdd(Number):
#     def __init__(self,number):
#         super().__init__(number)
#     def display_type(self):
#         if self.number%2==0:
#             print("Type: Even")
#         else:
#             print("Type: Odd")
# class NumberAnalyzer(EvenOdd):
#     def __init__(self,number):
#         super().__init__(number)
#     def display_square(self):
#         print("Square:",self.number**2)
# number=int(input("Enter Number:"))
# obj=NumberAnalyzer(number)
# obj.display_number()
# obj.display_type()
# obj.display_square()


#Inheritance is Transitive
# class B(A):
#     pass
# class C(B):
#     pass

# class Number:
#     def __init__(self,number):
#         self.number=number
# class DivisibilityChecker(Number):
#     def __init__(self,number):
#         super().__init__(number)
#     def check_divisibility(self):
#         print("Divisible by 2:",self.number%2==0)
#         print("Divisible by 3:",self.number%3==0)
#         print("Divisible by 5:",self.number%5==0)
# class NumberAnalyzer(DivisibilityChecker):
#     def __init__(self,number):
#         super().__init__(number)
#     def digit_count(self):
#         return len(str(self.number))
# number=int(input("Enter Number:"))
# obj=NumberAnalyzer(number)
# print("Number:",obj.number)
# obj.check_divisibility()
# print("Digit Count:",obj.digit_count())


#HIERARCHICAL INHERITANCE
# class Animal:
#     def eat(self):
#         print("Animal eats")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")
# animal=Animal()
# animal.eat()
# animal.bark()


#Hierarchical vs Multilevel Inheritance
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass

# class Vehicle:
#     def Start(self):
#         print("Vehicle starts")
#     def stop(self):
#         print("Vehicle stops")
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")
# class Bike(Vehicle):
#     def ride(self):
#         print("Bike is riding")
# car=Car()
# bike=Bike()
# car.start()
# car.drive()
# car.stop()
# print()
# bike.start()
# bike.ride()
# bike.stop()

#Constructor in Hierarchical
# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
# class Car(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model=model
# class Bike(Vehicle):
#     def __init__(self,brand,engine):
#         super().__init__(brand)
#         self.engine=engine
# car=Car("Toyoto","camry")
# bike=Bike("Honda",150)
# print(car.brand)
# print(car.model)
# print(bike.brand)
# print(bike.engine)

# class Number:
#     def __init__(self,number):
#         self.number=number
# class Even(Number):
#     def check(self):
#         return self.number%2==0
# class Odd(Number):
#     def check(self):
#         return self.number%2!=0
# even_obj=Even(8)
# odd_obj=Odd(7)
# print("8 is even:",even_obj.check())
# print("7 is odd:",odd_obj.check())


# class Shape:
#     def __init__(self,name):
#         self.name=name
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         super().__init__("Rectangle")
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__("Circle")
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
# rectangle=Rectangle(10,5)
# circle=Circle(7)
# print(rectangle.name)
# print("Area:",rectangle.area())
# print(circle.name)
# print("Area",circle.area())

#Method Overriding in Hierarchical Inheritance
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog Bark")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# dog=Dog()
# cat=Cat()
# dog.sound()
# cat.sound()

#Super() with Method Overriding
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dog Barks")
# dog=Dog()
# dog.sound()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# class Developer(Employee):
#     def display(self):
#         print("Developer:", self.name)
#         print("Salary:", self.salary)
# class Tester(Employee):
#     def display(self):
#         print("Tester:", self.name)
#         print("Salary:", self.salary)
# name = input("Enter employee name: ")
# salary = float(input("Enter salary: "))
# choice = input("Enter role (developer/tester): ")
# if choice == "developer":
#     obj = Developer(name, salary)
# else:
#     obj = Tester(name, salary)
# obj.display()

#CONSTRUCTOR + SUPER()
# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
# class Car(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model=model
# class Bike(Vehicle):
#     def __init__(self,brand,engine):
#         super().__init__(brand)
#         self.engine=engine
# car=Car("Toyota","Camry")
# bike=Bike("Honda",150)
# print(car.brand)
# print(car.model)
# print(bike.brand)
# print(bike.engine)

#Constructor + Method Together
# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
#         def start(self):
#             print(self.brand,"starts")
# class Car(Vehicle):
#     def __Init__(self,brand,model):
#         super().__init__(brand)
#         self.model=model
#     def drive(self):
#         print(self.model,"is driving")
# class Bike(Vehicle):
#     def __init__(self, brand, engine):
#         super().__init__(brand)
#         self.engine = engine
#     def ride(self):
#         print(self.brand, "bike is riding")
# car = Car("Toyota", "Camry")
# bike = Bike("Honda", 150)
# car.start()
# car.drive()
# bike.start()
# bike.ride()        

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#     def start(self):
#         print("Vehicle starts")
# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model
#     def start(self):
#         super().start()
#         print("Car starts")
#     def drive(self):
#         print(self.model, "is driving")
# class Bike(Vehicle):
#     def __init__(self, brand, engine):
#         super().__init__(brand)
#         self.engine = engine
#     def start(self):
#         super().start()
#         print("Bike starts")
#     def ride(self):
#         print(self.brand, "bike is riding")
# car = Car("Toyota", "Camry")
# bike = Bike("Honda", 150)
# print("CAR")
# print("Brand:", car.brand)
# print("Model:", car.model)
# car.start()
# car.drive()
# print()
# print("BIKE")
# print("Brand:", bike.brand)
# print("Engine:", bike.engine)
# bike.start()
# bike.ride()


#MULTIPLE INHERITANCE 
#syntax
# class Child(Parent1,Parent2):
#     pass

# class Father:
#     def father_method(self):
#         print("Father method")
# class Mother:
#     def mother_method(self):
#         print("Mother method")
# class Child(Father,Mother):
#     def child_method(self):
#         print("Child's method")
# obj=Child()
# obj.father_method()
# obj.mother_method()
# obj.child_method()

#Child Can Add Its Own Methods
# class Camera:
#     def take_photo(self):
#         print("Taking photo")
# class MusicPlayer:
#     def play_music(self):
#         print("Playing music")
# class SmartPhone(Camera,MusicPlayer):
#     def call(self):
#         print("Calling")
# phone=SmartPhone()
# phone.take_photo()
# phone.play_music()
# phone.call()

#Multiple Inheritance With Constructors
# class Father:
#     def __init__(self,father_name):
#         self.father_name=father_name
# class Mother:
#     def __init__(self,mother_name):
#         self.mother_name=mother_name
# class Child(Father,Mother):
#     def __init__(self,fater_name,mother_name):
#         print(Child.mro())

#Multiple Inheritance and Method Search
# class Father:
#     def show(self):
#         print("Father")
# class Mother:
#     def show(self):
#         print("Mother")
# class Child(Father,Mother):
#     pass
# obj=Child()
# obj.show()

#Changing Parent Order Changes the Result
# class Child(Mother,Father):
#     pass

#Super() in Multiple Inheritance
# class A:
#     def show(self):
#         print("A")
# class B:
#     def show(self):
#         print("B")
# class C(A,B):
#     def show(self):
#         super().show()
#         print("C")
# obj=C()
# obj.show()


class NumberProperties:
    def square(self):
        return self.number**2
class DivisibilityChecker:
    def divisible_by_3(self):
        return self.number%3==0
class NumberAnalyzer(NumberProperties,DivisibilityChecker):
    def __init__(self,number):
        self.number=number
obj=NumberAnalyzer(12)
print(obj.square())
print(obj.divisible_by_3())


