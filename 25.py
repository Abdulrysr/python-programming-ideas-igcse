# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Ask a user to enter their date of birth in the format DD/MM/YY. 
    Output their date of birth in text, e.g. Your birthday is on the first of February 2000."""

ordinalNum = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth", "Eighteenth", "Nineteenth", "Twentieth", "Twenty-first", "Twenty-second", "Twenty-third", "Twenty-fourth", "Twenty-Fifth", "Twenty-sixth", "Twenty-eighth", "Twenty-ninth", "Thirtieth", "Thirty-first"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]


def getOrdinalNum(day):

    if (day[0] == "0"):
        return ordinalNum[int(day)[1] - 1]
    else:
        return ordinalNum[int(day) - 1]

dob = input("Enter date of birth in the format DD/MM/YY: ")
day = f"{dob[0]}{dob[1]}"
month_num = f"{dob[3]}{dob[4]}"
year = f"20{dob[6]}{dob[7]}"

print("Your birthday is on the ", getOrdinalNum(day), " of ", months[int(month_num)-1], " ", year)













