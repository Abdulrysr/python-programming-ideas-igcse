# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a multiple choice quiz program. The user should be asked 3 questions and the program
should output how many they got correct. """


class makeQuestion:
    def __init__(self, question, options, correct):
        self.question = question
        self.options = options
        self.correct = correct

        
questions = [
    makeQuestion("How many holes are there in a golf court?", ["18", "1", "2"], "18"),
    makeQuestion("Which country are the Giza Pyramids in?", ["Egypt", "Syria", "Dubai"], "Egypt"),
    makeQuestion("Fastest animal on earth is?", ["Falcon", "Kangroo", "Cheetah"], "Cheetah"),
]

correct = 0
for obj in questions:
    # print(obj)
    print(f"\n{obj.question}\nOptions:\n")

    for option in obj.options:
        print(f"{option}")
    answer = input("\nEnter your answer: ")

    if answer == obj.correct:
        correct = correct + 1
    
    
print(f"You got {correct} answers correct")