# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program that takes the length of two sides of a right-angled triangle and outputs the
hypotenuse. """

# pythagoras theorum is ( a2 + b2 = c2 )

from math import sqrt


a = eval(input("Enter length of side a: "))
b = eval(input("Enter length of side b: "))

a2 = a*a 
b2 = b*b
sum = a2 + b2
c = sqrt(sum)

print(f"\nHypotenuse of the right-angled triangle is {c}")