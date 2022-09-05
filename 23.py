# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program that asks the user to enter a sentence, then output the sentence in reverse. """

sentence = input("Enter a sentence: ")
length = len(sentence)-1
reverse = ""
while length>-1:
    reverse = reverse + sentence[length]
    length = length - 1

    
print(reverse)