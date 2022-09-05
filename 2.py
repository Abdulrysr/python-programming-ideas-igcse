# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" 2 Write a program that lets the user enter the temperature in Celsius. Output the temperature
in Fahrenheit.  """

def celToFaren(temp):
    farenheit = (temp * (9/5)) + 32 
    return f"{temp}°C is {farenheit}°F"

temp = eval(input("Enter the temperature in Celsius: "))
print(celToFaren(temp))
