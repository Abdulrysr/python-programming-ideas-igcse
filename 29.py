# 24402 Abdul Rehman Yaser AS PRE ENG B2

"""Write a program that asks a user to enter a number. Use a procedure to output the numbers 1 to the number entered"""

def outputNumbers(start, end):
    for i in range(start, end, 1):
        print(i)

number = int(input('Enter a number: '))
outputNumbers(1, number)



