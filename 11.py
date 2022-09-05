# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program that asks the user to enter a number, and output the times table for
that number.  """

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {i*number}")
