# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Ask the user to enter a sentence. Output the number of characters (excluding spaces) in the
sentence, and to output the number of vowels.  """

word = input("Enter a sentence: ")

counter = 0
vowels = 0
for letter in word:
    print(letter)
    if letter != " ":
        counter += 1
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowels += 1

print(f"Total Letters excluding spaces: {counter}")
print(f"Total vowels excluding spaces: {vowels}")
    