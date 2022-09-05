# 24402 Abdul Rehman Yaser AS PRE ENG B2


"""  

Write a program that stores a sentence. Ask the user to enter a word. Output whether the word
input also exists in the stored sentence. 

"""

storedSentence = "python is cool dayum.".split()
word = input("Enter a word: ")

found = False
for i in range(0, len(storedSentence)-1):
    if word == storedSentence[i]:
        found = True

if found==True:
    print("Word exists in stored sentence")
else:
    print("Word doesn't exist in stored sentence")

        