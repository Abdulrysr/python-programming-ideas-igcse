# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program that takes a number from the user and then increases it by 5%. It should keep
doing this until the number is more than 500. Output the number of times the number was
increased by 5%. """

number = eval(input("Enter a number: "))

counter = 0
updatedNumber = number
while updatedNumber < 500:
    updatedNumber = updatedNumber + (updatedNumber*(5/100))
    counter += 1

print(f"New number: {updatedNumber}")
print(f"Number of times number was increased: {counter}")