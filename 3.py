# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program that asks the user to enter two numbers. Add them together and output
the result.  """

def sum(num1, num2):
    return f"{num1} + {num2} is {num1+num2}"
    

num1 = eval(input('Enter number 1: '))
num2 = eval(input('Enter number 2: '))

print(sum(num1, num2))