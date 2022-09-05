# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program to perform a Caesar cypher on a word that is input by the user """

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cipher = ["X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]

word = input("Enter a word: ")

encrypted = ""
for letter in word: 
    letterUpper = letter.upper()
    index = letters.index(letterUpper)
    cipherLetter = cipher[index]
    encrypted = encrypted + cipherLetter.lower()

print(f"\nPlain Text: {word}")
print(f"Encrypted: {encrypted}")
