# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program to ask the user to enter a word that has between 5 and 10 characters (inclusive).
Output an error if the word is not valid.  """

proceed = False
while proceed==False:
    word = input("Enter a word between 5 to 10 characters (inclusive): ")
    if len(word)>10 or len(word)<5:
        print("\nInvalid please input again again between 5 to 10 characters (inclusive)\n")
    else:
        print("\nValid")
        proceed = True