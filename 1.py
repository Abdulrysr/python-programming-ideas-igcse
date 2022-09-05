# 24402 Abdul Rehman Yaser AS PRE ENG B2

""" 1 Write a program that asks a user to enter their name and age. Display “name you are age years 
old”. E.g. if Asim and 15 were entered then it would output “Asim you are 15 years old.  """

def showDetails(name, age):
    print(f"{name} you are {age} years old.")


name = input("Enter your name: ")
age = eval(input("Enter your age: "))
showDetails(name, age)
