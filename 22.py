# 24402 Abdul Rehman Yaser AS PRE ENG B2


"""  Write a program that creates a username for a user. It consists of the first 3 letters of the last
name and the first three letters of their first name.  """

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

f = ""
l = ""

for i in range(0, 3):
    f += fname[i]
    l += lname[i]

username=f"{l}{f}"
print(username)