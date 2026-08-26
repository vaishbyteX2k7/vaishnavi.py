#string concatenation
# first="hello"
# second="world"
# print(first+" "+second)

#old style formating
# "%s" % value

#.format()
# "{}".format(value)

#f-string
# f"{value}"

#OLD STYLE STRING FORMATING
#syntax
#"Text %type" % value

#%s string placeholder
# name="Vaishnavi"
# print("Hello %s" % name)
# age=20
# print("Age=%s" % age)
# price=99.99
# print("Price=%s"%price)
# student=True
# print("Student=%s"%student)

#%d integer placeholder
# marks=95
# print("Marks=%d"%marks)

#%f float placeholder
# cgpa=8.75
# print("CGPA=%f"%cgpa)
# cgpa=8.75
# print("CGPA=%.2f"%cgpa)
# pi=3.1415926
# print("%.3f"%pi)

#%c character placeholder
# letter="A"
# print("%c"%letter)
# print("%c"%66)

#%% print a percent symbol placeholder
# discount=20
# print("Discount=%d%%"%discount)

#multiple placeholder
# name = "Vaishnavi"
# age = 20
# cgpa = 8.75

# print("Name = %s, Age = %d, CGPA = %.2f" % (name, age, cgpa))

#width specifier(spaces)
# print("%5d"%42)
# print("%8d"%123)

#Left alignment
# print("%-5d"%42)

#combining width and precision
# pi=3.14159265
# print("%10.2f"%pi)

#STR.FORMAT() METHOD
# name="Vaishnavi"
# print("Hello {}".format(name))
# age=20
# print("Age is {}".format(age))
# price=99.99
# print("Price= {}".format(price))

#multiple placeholder
# name = "Vaishnavi"
# age = 20
# city = "Delhi"
# print("Name: {}, Age: {}, City: {}".format(name, age, city))

#positional arguments
# print("{0} {1}".format("Python","Java"))
# print("{0} {0} {1}".format("Hi","Bye"))

#recording values
# print("{1} {0}".format("Python","Java"))

#keyword argument
# print("Hello {name}".format(name="Vaishnavi"))

#Mixing Positional and keyword
# print(
#     "{0} lives in {city}".format(
#         "Vaishnavi",
#         city="Delhi"
#     )
# )

#Formating numbers
# pi=3.141592653
# print("{}".format(pi))

# print("{:.2f}".format(pi))

#width
# print("{:10}".format("Hi"))

# #Left alignment
# print("{:<10}".format("Hi"))

# #Right alignment
# print("{:>10}".format("Hi"))

# #Centre alignment
# print("{:^10}".format("Hi"))

# #Fill characters
# print("{:*^10}".format("Hi"))
# print("{:-<10}".format("Hi"))


#F-STRING(FORMATTED STRING LITERALS)
# name="Vaishnavi"
# print(f"Hello {name}")

#mutiple variables
# name="vaishnavi"
# age=20
# branch="mechanical"
# print(f"My name is {name}.")
# print(f"I am {age} years old.")
# print(f"My branch is {branch}.")

# print(f"Name: {name}, Age: {age}, Branch: {branch}")


#Expression
# a=10
# b=20
# print(f"Sum={a+b}")

# length=10
# breadth=5
# print(f"Area={length*breadth}")

# x=7
# print(f"Square={x**2}")


#Calling functions inside f-string
# name="Vaishnavi"
# print(name.upper())

# def Square(n):
#     return n*n
# print(f"Square={Square(6)}")


#Calling string methods
# name="Vaishnavi"
# print(f"{name.lower()}")

# print(f"{name.capitalize()}")

# print(f"{name.replace('a','@')}")


#Float formatting
# pi=3.14159265
# print(f"{pi}")
# print(f"{pi:2f}")


#Width and Alignment
#Right align
# print(f"{'Hi':>10}")

# #Left align
# print(f"{'Hi':<10}")

# #Centre align
# print(f"{'Hi':^10}")

# #Fill character
# print(f"{'Hi':*^10}")

#Formatting Integer
# num=42
# print(f"{num:5}")

#Leding zero
# num=42
# print(f"{num:05}")

#Escape Character
# name="Vaishnavi"
# print(f"Hello\n{name}")

# print(f"Name\tAge")


# name = "Vaishnavi"
# marks = 95
# cgpa = 8.756

# print(f"""
# Student Report
# --------------
# Name : {name}
# Marks: {marks}
# CGPA : {cgpa:.2f}
# """)


#ADVANCED DTRING FORMATTING
#Width
# print(f"{'Ram':12}{95}")
# print(f"{'Vaishnavi':12}{88}")
# print(f"{'Aman':12}{90}")

#Alignment
# print(f"|{'Python':<15}|")
# print(f"|{'Python':^15}|")

#Fill character
# print(f"{'Python':=^20}")

#width+precision
# pi = 3.14159265
# print(f"|{pi:10.2f}|")

#Thousand seperator
# salary=1000000
# print(f"{salary:,}")

# salary=1234567.89
# print(f"{salary:,.2f}")

#Underscore seperator
# salary=1234567.89
# print(f"{salary:_}")

#Binary, Octal & Hexadecimal
#Binary
# num=25
# print(f"{num:b}")

# #octal
# print(f"{num:o}")

#Hexadecimal
# print(f"{num:x}")
# print(f"{num:X}")

#scietific Notation
# num=123456789
# print(f"{num:e}")
# print(f"{num:E}")

#Percentage Formatting
# marks=95
# total=100
# percentage=marks/total
# print(f"{percentage:.2%}")

# item = "Laptop"
# price = 58999.5

# print(f"""
# Invoice
# ----------------------
# Item  : {item}
# Price : £{price:,.2f}
# """)


#ESCAPE CHARACTERS(\)
#Newline(\n)
# print("Hello\nworld")

# #tab(\t)
# print("Name\tAge")

# #Backslash(\\)
# print("C:\\Uers\\Vaishnavi")

#Double Quote(\")
#print("He said \"Hello\"")

#Single Quote(\')
# print("It's raining.")
# print('It\'s raining')

#Backspace(\b)=go back one character
# print("ABC\bD")
# print("12345\b")

#Carriage Return
# print("Hello\rHi")

# import time

# for i in range(6):
#     print(f"\rLoading... {i}", end=" ")
#     time.sleep(1)

#Form Feed(\f)
# print("Page1\fPage2")

#Vertical Tab(\v)
# print("Python\vJava")

#bell(\a)
# print("\a")

#Raw Strings
# print(r"Hello\nWorld")
# file = r"D:\Python\Projects\data.txt"
# print(file)

# backup_folder = r"D:\Backups\Python"
# print(f"Saving files to: {backup_folder}")