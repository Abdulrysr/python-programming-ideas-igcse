# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program that reads 10 numbers from the user and stores them in an array. 
Total and output the numbers from the array, and the average number """

numbers = []
numbersInput = eval(input("Enter 10 numbers below seperated by a comma: "))

for x in numbersInput:
    numbers.append(x)

total = 0
for x in numbers:
    total += x

average = total/len(numbers)

print(f"Total of numbers: {total}")
print(f"Average of numbers: {average}")


