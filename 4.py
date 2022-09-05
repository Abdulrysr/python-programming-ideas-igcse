# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program to ask the user to input a number between 1 and 12. Output which month of
the year that number is for.  """

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]



error = False
while error==False:
    index = int(input("Enter number of month (1 - 12): "))
    if index > 0 and index < 13:
        error = True
    else:
        print("Error, the value should be between 1 and 12\n")

print(months[index-1])


