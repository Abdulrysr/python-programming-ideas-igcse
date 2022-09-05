# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program to ask the user to enter 3 numbers. Output which of the numbers is the largest,
and which number is the smallest.  """

def sortNum(arr):
    x = True
    while x:
        sorted = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                sorted = True
        
        if sorted==False:
            break

    return arr

numbers = []
num1 = eval(input("Enter first number: "))
numbers.append(num1)
num2 = eval(input("Enter second number: "))
numbers.append(num2)
num3 = eval(input("Enter third number: \n"))
numbers.append(num3)

sortedNumbers = sortNum(numbers)

for num in sortedNumbers:
    print(num)



