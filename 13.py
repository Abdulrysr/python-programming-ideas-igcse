# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a simple calculator where the user enters two numbers and an operator. Output the result
of the calculation.  """

print("""

Operators are as following

+ --> Addition
- --> Subtraction
/ --> Division
* --> Multiplication

\n
""")

def calculate(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2
    else:
        return "Operator Invalid"

num1 = eval(input("Enter number 1: "))
num2 = eval(input("Enter number 2: "))
oper = input("Enter operator: ")

print("\nResult: ", calculate(num1, num2, oper))
