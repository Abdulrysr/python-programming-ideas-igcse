# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" 21 Write a program that outputs the Fibonacci sequence from 1 to 500. """

array = [1, 2]
newValue = 0
while newValue<500:
    arrLen = len(array)
    newValue = array[arrLen - 1] + array[arrLen - 2]
    array.append(newValue)


print(array)