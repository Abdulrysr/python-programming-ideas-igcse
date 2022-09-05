# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Ask a user to enter 10 numbers. Output the largest and smallest number.  """

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
num3 = eval(input("Enter third number: "))
numbers.append(num3)
num4 = eval(input("Enter fourth number: "))
numbers.append(num4)
num5 = eval(input("Enter fifth number: "))
numbers.append(num5)
num6 = eval(input("Enter sixth number: "))
numbers.append(num6)
num7 = eval(input("Enter seventh number: "))
numbers.append(num7)
num8 = eval(input("Enter eigth number: "))
numbers.append(num8)
num9 = eval(input("Enter ninth number: "))
numbers.append(num9)
num10 = eval(input("Enter tenth number: "))
numbers.append(num10)

sortedNumbers = sortNum(numbers)
print(sortedNumbers)



