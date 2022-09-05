# 24402 Abdul Rehman Yaser AS PRE ENG B2


"""  Write a program that reads a number from a text file. Output all the numbers between 1 and the
number from the file.  """

f = open("33.txt", 'r')
number = f.read()

for i in range(1, int(number)):
    print(i)



