# class Calculator:
#     @staticmethod
#     def multiply(a,b):
#         return a*b
# answer=Calculator.multiply(5,8)
# print(answer)

class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

#MULTIPLE STATIC METHODS IN ONE CLASS
# class Calculator:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     @staticmethod
#     def subtract(a,b):
#         return a-b
#     @staticmethod
#     def multiply(a,b):
#         return a*b
# print(Calculator.add(10,5))
# print(Calculator.subtract(10,5))
# print(Calculator.multiply(10,5))

# class Calculator:
#     @staticmethod
#     def square(x):
#         return x*x
#     @staticmethod
#     def sum_of_square(a,b):
#         return Calculator.square(a)+Calculator.square(b)
# print(Calculator.sum_of_square(3,4))

#calling staticmethod from an instance method
# class Calculator:
#     @staticmethod
#     def cube(n):
#         return n**3
#     def show_cube(self,number):
#         print(Calculator.cube(number))
# obj=Calculator()
# obj.show_cube(2)

#calling staticmethod from a class method
# class Calculator:
#     @staticmethod
#     def double(n):
#         return n*2
#     @classmethod
#     def display(cls,number):
#         print(cls.double(number))
# Calculator.display(8)

#calling static method from outside the class
# class Greeting:
#     @staticmethod
#     def hello():
#         print("Hello")
# Greeting.hello()

#UTILITY FUNCTION USING STATICMETHODS
# class Mathutils:
#     @staticmethod
#     def square(x):
#         return x*x
#     @staticmethod
#     def cube(x):
#         return x*x*x
# print(Mathutils.square(6))

#even numbers
# class Mathutils:
#     @staticmethod
#     def is_even(n):
#         return n%2==0
# print(Mathutils.is_even(10))

#maximum
# class Mathutils:
#     @staticmethod
#     def maximum(a,b):
#         return max(a,b)
# print(Mathutils.maximum(20,35))

#string utility methods
# class Stringutils:
#     @staticmethod
#     def to_upper(text):
#         return text.upper()
# print(Stringutils.to_upper("Python"))

# class Stringutils:
#     @staticmethod
#     def reverse(text):
#         return text[::-1]
# print(Stringutils.reverse("Vaishnavi"))

# class Stringutils:
#     @staticmethod
#     def count_characters(text):
#         return len(text)
# print(Stringutils.count_characters("Python"))

#date and time utility functions
# class Timeutils:
#     @staticmethod
#     def seconds_to_minutes(seconds):
#         return seconds/60
# print(Timeutils.seconds_to_minutes(300))

# class Timeutils:
#     @staticmethod
#     def hours_to_minutes(hours):
#         return hours*60
# print(Timeutils.hours_to_minutes(120))

#validation utility functions
# class Passwordvalidation:
#     @staticmethod
#     def is_valid(password):
#         return len(password)>=8
# print(Passwordvalidation.is_valid("Python123"))

# class Mathutils:
#     @staticmethod
#     def square(n):
#         return n*n
#     @staticmethod
#     def cube(n):
#         return n*n*n
#     @staticmethod
#     def is_even(n):
#         return n%2==0
#     @staticmethod
#     def is_odd(n):
#         return n%2!=0
#     @staticmethod
#     def maximum(a,b):
#         if a>b:
#             return a
#         else:
#             return b
#     @staticmethod
#     def minimum(a,b):
#         if a<b:
#             return a
#         else:
#             return b
# print("Square of 5:", Mathutils.square(5))
# print("Cube of 4:", Mathutils.cube(4))
# print("Is 10 Even?:", Mathutils.is_even(10))
# print("Is 15 Odd?:", Mathutils.is_odd(15))
# print("Maximum of 20 and 35:", Mathutils.maximum(20, 35))
# print("Minimum of 20 and 35:", Mathutils.minimum(20, 35))

# class Mathutils:
#     @staticmethod
#     def factorial(n):
#         if n<0:
#             return "Factorial is not defined for negative numbers"
#         fact=1
#         for i in range(1,n+1):
#             fact=fact*i
#         return fact
#     @staticmethod 
#     def power(base,exponent):
#         return base**exponent
#     @staticmethod
#     def is_prime(n):
#         if n<=1:
#             return False
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True
# print("Factorial of 5 =", Mathutils.factorial(5))
# print("2 raised to power 5 =", Mathutils.power(2, 5))
# print("Is 17 Prime? =", Mathutils.is_prime(17))
# print("Is 20 Prime? =", Mathutils.is_prime(20))

#BANK MANAGEMENT SYSTEM
# class FinanceUtils:
#     @staticmethod
#     def calculate_simple_interest(principal,rate,time):
#         return (principal*rate*time)/100
#     @staticmethod
#     def calculate_compound_interest(principal,rate,time):
#         amount=principal*(1+rate/100)**time
#         compound_interest=amount-principal
#         return round(compound_interest,2)

#     @staticmethod
#     def calculate_gst(price,gst_percent):
#         gst=(price*gst_percent)
#         total=price+gst
#         return total

#     @staticmethod
#     def calculate_discount(price,discount_percent):
#         discount=(price*discount_percent)/100
#         final_price=price-discount
#         return final_price

#     @staticmethod
#     def calculate_emi(loan_amount,months):
#         emi=loan_amount/months
#         return round(emi,2)
# print("Simple Interest:",
#       FinanceUtils.calculate_simple_interest(10000, 10, 2))

# print("Compound Interest:",
#       FinanceUtils.calculate_compound_interest(10000, 10, 2))

# print("Price after GST:",
#       FinanceUtils.calculate_gst(5000, 18))

# print("Price after Discount:",
#       FinanceUtils.calculate_discount(5000, 20))

# print("Monthly EMI:",
#       FinanceUtils.calculate_emi(120000, 24))


# from datetime import datetime
# class DateUtils:

#     @staticmethod
#     def current_date():
#         return datetime.now().date()

#     @staticmethod
#     def current_year():
#         return datetime.now().year

#     @staticmethod
#     def is_leap_year(year):
#         if year%400==0:
#             return True
#         elif year%100==0:
#             return False
#         elif year%4==0:
#             return True
#         else:
#             return False

#     @staticmethod
#     def days_between(date1,date2):
#         d1=datetime.strptime(date1,"%d-%m-%y")
#         d2 = datetime.strptime(date2, "%d-%m-%Y")

#         difference = abs((d2 - d1).days)

#         return difference

#     @staticmethod
#     def format_date(date):

#         d = datetime.strptime(date, "%d-%m-%Y")

#         return d.strftime("%d %B %Y")
# print("Today's Date:",
#       DateUtils.current_date())

# print("Current Year:",
#       DateUtils.current_year())

# print("Is 2024 Leap Year?",
#       DateUtils.is_leap_year(2024))

# print("Days Between:",
#       DateUtils.days_between("01-01-2025", "15-01-2025"))

# print("Formatted Date:",
#       DateUtils.format_date("22-07-2026"))

#overriding static method
# class Animal:
#     @staticmethod
#     def sound():
#         print("Some Sound")
# class Dog(Animal):
#     @staticmethod
#     def sound():
#         print("Bark")
# Dog.sound()
# Animal.sound()

#method resolution order (MRO)
# class A:
#     @staticmethod
#     def hello():
#         print("A")
# class B(A):
#     pass
# class C(B):
#     pass
# C.hello()

#can staticmethod create objects
# class Student:
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def create_student():
#         return Student("Vaishnavi")
# obj=Student.create_student()
# print(obj.name)

# class StringUtils:
#     @staticmethod
#     def to_upper(text):
#         return text.upper()

#     @staticmethod 
#     def to_lower(text):
#         return text.lower()

#     @staticmethod
#     def reverse(text):
#         return text[::-1]

#     @staticmethod
#     def count_characters(text):
#         return len(text)

#     @staticmethod
#     def count_words(text):
#         return len(text.split())

#     @staticmethod
#     def remove_spaces(text):
#         return text.replace(" ","")

#     @staticmethod
#     def capitalize_words(text):
#         return text.title()

#     @staticmethod
#     def is_palindrome(text):
#         text=text.lower()
#         text=text.replace(" ","")
#         return text==text[::-1]
# print("Upper :", StringUtils.to_upper("hello world"))

# print("Lower :", StringUtils.to_lower("PYTHON"))

# print("Reverse :", StringUtils.reverse("Python"))

# print("Characters :", StringUtils.count_characters("Python"))

# print("Words :", StringUtils.count_words("I Love Python"))

# print("Without Spaces :", StringUtils.remove_spaces("I Love Python"))

# print("Capitalized :", StringUtils.capitalize_words("welcome to python"))

# print("Palindrome :", StringUtils.is_palindrome("Madam"))

# print("Palindrome :", StringUtils.is_palindrome("Hello"))


