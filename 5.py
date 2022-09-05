# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program that takes a learner’s score in a test out of 100. Decide on the mark that a
learners should achieve an A, B, C, D or U for. Output the learner’s grade. """


def getGrade(marks):
    if marks > 95:
        grade = "W"
    elif marks > 90:
        grade = "A"
    elif marks > 80:
        grade = "B"
    elif marks > 70:
        grade = "C"
    elif marks > 60:
        grade = "D"
    elif marks > 50:
        grade = "L"

    return grade

marks = eval(input("Enter student's marks out of 100: "))
print(getGrade(marks))


