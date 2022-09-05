# 24402 Abdul Rehman Yaser AS PRE ENG B2


" Store a set of letters in an array. Ask the user to input a letter to search for. Output whether the letter is in the array or not. "

array = ["a", "x", "t", "g", "i", "p", "z"]

letter = input("Enter a letter: ")

found = False
for item in array:
    if item==letter:
        found = True

if found==True:
    print(letter, " exists in array")
else:
    print(letter, " doesn't exist in array")
