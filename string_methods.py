#Lower()
# name="PYTHON"
# print(name.lower())

#Upper()
# text="Hello World"
# print(text.upper())

#capitalize()
# text="python"
# print(text.capitalize())

# text = "hELLO WORLD"
# print(text.capitalize())

#title()
# text="hello world"
# print(text.title())

#Swapcase()
# text="PyThOn"
# print(text.swapcase())

#Casefold()
# a = "Python"
# b = "PYTHON"
# print(a.casefold() == b.casefold())

# print("HELLO".casefold())

#SEARCHING METHODS
#Find()
#result=string.find(substring) 

# text="Python"
# print(text.find("P"))
# print(text.find("Java"))


#Searching from a specific position
#string.find(substring,start)
# text="banana"
# print(text.find("a",2))

#Searching between two position
#string.find(substring,start,end)
# text="banana"
# print(text.find("a",2,5))

# text = "apple"
# if text.find("a") != -1:
#     print("Found")
# else:
#     print("Not Found")


#rfind()[reverse find]
# text="banana"
# print(text.rfind("a"))


#index()
# text="Python"
# print(text.index("P"))

#Searching from a particular position
#string.index(substring,start)
# text="banana"
# print(text.index("a",2))
# print(text.index("a",2,5))

#rindex()
# text="banana"
# print(text.rindex("a"))

#count()[occurence]
# text="banana"
# print(text.count("a"))
# print(text.count("n"))
# print(text.count("an"))
# print(text.count("a",2,6))


#WHITESPACE METHODS
#strip()
# text="   Python   "
# print(text.strip())

#lstrip()[fromleft]
# text="   python   "
# print(text.lstrip())

#rstrip() [from right]
# text="   Python   "
# print(text.rstrip())

#Removing tabs
# text="\t\tPython\t\t"
# print(text.strip())

#Removing newline
# text="\n\nPython\n\n"
# print(text.strip())

#Mixed whitespace
# text="\n\t Python \t\n"
# print(text.strip())

#Removing Custom Characters
# text="###Python###"
# print(text.strip("#"))

# text="00012345000"
# print(text.strip("0"))

#Multiple Characters
# text="@#$Python#$@"
# print(text.strip("@#$"))

# name = input("Enter your name: ")
# name = name.strip()
# print("Hello", name)

# username = input("Username: ").strip()
# print(username)


#replace()
#new_string=string.replace(old,new)
# text="Hello World"
# print(text.replace("World","Vaishnavi"))

# text="banana"
# print(text.replace("a","o"))

# text = "apple@google.com"
# print(text.replace("@", "#"))

#Replacing multiple occurence
# text="Python Python Python"
# print(text.replace("Python","Java"))

#Limiting the Number of Replacement
#string.replace(old,new,count)
# text = "Python Python Python"
# print(text.replace("Python", "Java", 1))

# text="banana"
# print(text.replace("a","o",2))

#Replacing with a empty string
# text="banana"
# print(text.replace('a'," "))

#Replacing Spaces
# text="Python Programming Language"
# print(text.replace(" ","_"))

# text = "Hello World"
# print(text.replace(" ", "-"))

#Replacing tabs
# text="Python\tJava\tC"
# print(text.replace("\t","|"))

#Replacing Newline
# text="Apple\nBanana\nOrange"
# print(text.replace("\n",", "))

#Chaining replace()
# text = "Python Java C++"
# result = text.replace("Python", "C").replace("Java", "Go")
# print(result)

# date = "25/12/2025"
# print(date.replace("/", "-"))

# phone = "98765 43210"
# print(phone.replace(" ", ""))


#split()
# text="Pyton is Easy"
# result=text.split()
# print(result)

#Accessing Elements
# text="Python is Easy"
# words=text.split()
# print(words[0])

#Splitting Using a Seperator
# text="Aplle,Mango,Banana"
# print(text.split(","))

# numbers = "10,20,30,40"
# print(numbers.split(","))

#Splitting Using a Hyphen
# text="Red-blue-green"
# print(text.split("-"))

#Splitting with Slash
# date="25/12/2026"
# print(date.split("/"))

#Splitting with Pipe Symbol
# text="Python|Java|c++"
# print(text.split("|"))

#MaxSplit
#string.split(separator,maxsplit)
# text="Apple,Mango,Orange,Grapes"
# print(text.split(",",1))

#Empty String
# text=""
# print(text.split())

#Splitting a single Word
# text="Python"
# print(text.split())

# date = "25/12/2025"
# day, month, year = date.split("/")
# print(day)
# print(month)
# print(year)

# sentence = "Python is fun"
# words = sentence.split()
# print(len(words))


#rsplit() [Reverse split]
# text="Python is Very Easy"
# print(text.rsplit())

# text="Apple,Mango,Banana,Grapes"
# print(text.rsplit(",",1))

# text = "A-B-C-D-E"
# print(text.rsplit("-", 2))


#splitlines()
# text="Python\nJava\nC++"
# print(text.splitlines())

#Empty string
# text=""
# print(text.splitlines())

#Keepends Parameters
# text="Python\nJava\nC++"
# print(text.splitlines(True))


#partition()
# text="Python-Java"
# print(text.partition("-"))

# text = "A-B-C-D"
# print(text.partition("-"))

#Accessing the Parts
# text="Python-Java"
# parts=text.partition("-")
# print(parts[0])

#Tuple Unpacking
# text = "Python-Java"
# left, symbol, right = text.partition("-")
# print(left)
# print(symbol)
# print(right)

# text = "Python"
# print(text.partition("-"))


#rpartition [right side]
# text="A-B-C-D"
# print(text.rpartition("-"))

# email = "vaishnavi@gmail.com"
# username, symbol, domain = email.partition("@")
# print(username)
# print(domain)

# filename = "report.pdf"
# name, dot, extension = filename.partition(".")
# print(name)
# print(extension)

# path = "Documents/Python/notes.txt"
# folder, slash, file = path.rpartition("/")
# print(folder)
# print(file)


#JOINING METHODS
#join()
# fruits=["Apple","Mango","Banana"]
# result="-".join(fruits)
# print(result)

# words=["Python","is","easy"]
# sentence=" ".join(words)
# print(sentence)

# numbers = ["10", "20", "30"]
# print(",".join(numbers))

# letters = ["P", "Y", "T", "H", "O", "N"]
# print("".join(letters))

# letters = ["A", "B", "C"]
# print("*".join(letters))

# students = ["Rahul", "Aman", "Vaishnavi"]
# print("\n".join(students))

# cities = ["Delhi", "Mumbai", "Chennai"]
# print(" -> ".join(cities))

# numbers = ["1", "2", "3"]
# print(",".join(numbers))

# numbers = [1, 2, 3]
# string_numbers = []
# for num in numbers:
#     string_numbers.append(str(num))
# print(",".join(string_numbers))

#Joining a Tuple
# languages = ("Python", "Java", "C++")
# print(", ".join(languages))

#Joining a Set
# colors = {"Red", "Green", "Blue"}
# print(", ".join(colors))

#Joining Dictionary keys
# student = {
#     "name": "Vaishnavi",
#     "age": 20,
#     "branch": "Mechanical"
# }
# print(", ".join(student))

#ADVANCED JOIN()
# words = ["Python", "is", "easy"]
# result = " ".join(words)
# print(result)

#split()+join()
# sentence = "Python is easy"
# words = sentence.split()
# print(words)
# new_sentence = "-".join(words)
# print(new_sentence)

#Joining After Slicing
# letters=["P","Y","T","H","O","N"]
# first=letters[:4]
# print(first)

# numbers = ["1", "2", "3", "4", "5"]
# print(",".join(numbers[1:4]))

#join() with map()
# numbers=[10,20,30]
# result=",".join(map(str,numbers))
# print(result)

#Joining with List Comprehension
# words=["Python","java","c++"]
# new=[]
# for word in words:
#     new.append(word.upper())
# result=" ".join([word.upper() for word in words])
# print(result)

# names = ["vaishnavi", "rahul", "aman"]
# print(", ".join([name.title() for name in names]))

#Joining Nested Lists
# data=[
#     ["A","B"]
#     ["C","D"]
#     for row in data:
#         print(",".join(row))
# ]

# name = "Vaishnavi Gupta"
# initials = "".join([word[0] for word in name.split()])
# print(initials)


#STRING TESTING METHODS
#startswith()
#result=string.startswith(prefix)
# text="Python"
# print(text.startswith("P"))
# print(text.startswith("Py"))
# print(text.startswith("Python"))
# print(text.startswith("Java"))
# print(text.startswith("python"))  

#Using start Parameter
#string.startswith(prefix,start)
# text="I Love Python"
# print(text.startswith("Love",2))

#string.startswith(prefix,start,end)
# text="Python Programming"
# print(text.startswith("Prog",7,18))

#Multiple prefixes
# text="photo.pn"
# print(text.startswith(("photo","image")))

# url = input("Enter URL: ")
# if url.startswith("https://"):
#     print("Secure Website")
# else:
#     print("Not Secure")


# roll = input("Enter Roll Number: ")
# if roll.startswith("ME"):
#     print("Mechanical Student")


#endswith()
#string.endswith(suffix)
# text="Python.py"
# print(text.endswith(".py"))

# text = "holiday.jpg"
# print(text.endswith(".png"))

# text="Hello"
# print(text.endswith("lo"))

# text = "Python Programming"
# print(text.endswith("Python", 0, 6))

# file = "holiday.png"
# print(file.endswith((".jpg", ".png", ".jpeg")))

# email = input("Enter Email: ")
# if email.endswith("@gmail.com"):
#     print("Gmail Account")


#CHARACTER TESTING METHODS
#isalpha() [checks alphabet letter]
# text="Python"
# print(text.isalpha())

# text="Python123"
# print(text.isalpha())

# text="Hello-World"
# print(text.isalpha())

# text=""
# print(text.isalpha())

# name=input("Enter your name:")
# if name.isalpha():
#     print("Valid Name")
# else:
#     print("Invalid Name")


#isdigit() [checks digits]
# text="12345"
# print(text.isdigit())

# text="123A"
# print(text.isdigit())

# text="12 34"
# print(text.isdigit())

# text="12.5"
# print(text.isdigit())

# text="-25"
# print(text.isdigit())

# text=""
# print(text.isdigit())

# otp = input("Enter OTP: ")
# if otp.isdigit():
#     print("Valid OTP")
# else:
#     print("Invalid OTP")


#isalnum() [checks letter and digit]
# text="Python123"
# print(text.isalnum())

# text="Python"
# print(text.isalnum())

# text = "Python 123"
# print(text.isalnum())

# text = "Python@123"
# print(text.isalnum())

# text = ""
# print(text.isalnum())

# username = input("Enter username: ")
# if username.isalnum():
#     print("Valid Username")
# else:
#     print("Only letters and digits are allowed.")


#CASE TESTING METHODS
#islower() [checks lowercase]
# text="python"
# print(text.islower())

# text = "python123"
# print(text.islower())

# text = "python!"
# print(text.islower())

# text = "python programming"
# print(text.islower())

# text = "12345"
# print(text.islower())

# text = ""
# print(text.islower())

# password = input("Enter password: ")
# if password.islower():
#     print("Password contains only lowercase letters.")
# else:
#     print("Password contains uppercase letters or has no letters.")


#isupper() [checks uppercase]
# text="PYTHON"
# print(text.isupper())

# text="PYTHON123"
# print(text.isupper())

# text = "PYTHON!!!"
# print(text.isupper())

# text = "HELLO WORLD"
# print(text.isupper())

# text = "12345"
# print(text.isupper())

# text = ""
# print(text.isupper())

# code=input("Enter Product Code:")
# if code.isupper():
#     print("Correct Format")
# else:
#     print("Use only Uppercase Letters")



#istitle()
# text="Python Programming"
# print(text.istitle())

# text = "Python programming"
# print(text.istitle())

# text = "HELLO WORLD"
# print(text.istitle())

# text = "Hello World 2026"
# print(text.istitle())

# text = "Hello World!"
# print(text.istitle())

# text = ""
# print(text.istitle())

# title = input("Enter Book Title: ")
# if title.istitle():
#     print("Correct Title Format")
# else:
#     print("Please use Title Case.")


#isspace() [checks whitespace]
# text = " "
# print(text.isspace())

# text = "     "
# print(text.isspace())

# text = "\t"
# print(text.isspace())

# text = "\n"
# print(text.isspace())

# text = "  \t\n "
# print(text.isspace())

# text = "123"
# print(text.isspace())

# name = input("Enter your name: ")
# if name == "" or name.isspace():
#     print("Please enter a valid name.")
# else:
#     print("Input Accepted")


#isidentifier()
# text = "student"
# print(text.isidentifier())

# text = "student123"
# print(text.isidentifier())

# text = "_student"
# print(text.isidentifier())

# text = "123student"
# print(text.isidentifier())

# text = "student name"
# print(text.isidentifier())

# text = "student-name"
# print(text.isidentifier())

# text = "student@"
# print(text.isidentifier())

# text = "for"
# print(text.isidentifier())

# import keyword
# print(keyword.iskeyword("for"))


#isdecimal() [checks decimal digit]
# text = "12345"
# print(text.isdecimal())

# text = "12.5"
# print(text.isdecimal())

# text = "-25"
# print(text.isdecimal())

# text = "123A"
# print(text.isdecimal())

# text = "²"
# print(text.isdigit())

# print("²".isdigit())

# text = "123²"
# print(text.isdigit())


#isnumeric()
# text = "Ⅷ"
# print(text.isnumeric())

# text = "½"
# print(text.isnumeric())

# otp = input("OTP: ")
# if otp.isdecimal():
#     print("Correct")


#isprintable() [checks printable characters]
# text = "@#$%^"
# print(text.isprintable())

# text = "Hello\nWorld"
# print(text.isprintable())

# text = ""
# print(text.isprintable())

# text = input("Enter text: ")
# if text.isprintable():
#     print("Valid")
# else:
#     print("Contains hidden characters")


#isascii()
# text = "@#$"
# print(text.isascii())

# text = "नमस्ते"
# print(text.isascii())

# text = "你好"
# print(text.isascii())

# text = "😀"
# print(text.isascii())

# text = "₹"
# print(text.isascii())

# text = ""
# print(text.isascii())


