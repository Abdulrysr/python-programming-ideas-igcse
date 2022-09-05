# 24402 Abdul Rehman Yaser AS PRE ENG B2


""" Write a program to play battleships. The computer should store the positions of its ships in a 2D
array. The user should guess the positions of the ships and the program should output if they are
correct or not. The game ends when either the user has identified all the squares, or the user has
had a set number of guesses. 
"""


print("""
\n
================================
General Instructions

User has 3 tries to guess the positions of the ships 
The positions are in the form of (x, y, z) where x is the x coordinate, 
y is the y coordinate and z is the z coordinate.
================================
\n
""")

positions = [
    [5,7,4],
    [8,5,1],
    [6,4,2],
    [2,2,1]
]

tries = 0
found = False
while tries < 3 or found == True:
    print(f"\n============================== TRY {tries+1}  ==============================")
    done = False
    while done==False:
        coordinates = input("Enter coordinates (x, y, z) seperated by commas: ")
        coordArr=[]
        for x in coordinates:
            if x !=",":
                coordArr.append(x)

        if len(coordArr) != 3:
            print("Invalid coordinates, kindly enter three coordinates")
        else:
            done = True
    

    for i in range(0, len(positions), 1):

        
        if positions[i][0] == int(coordArr[0]) and positions[i][1] == int(coordArr[1]) and positions[i][2] == int(coordArr[2]):
            found = True
            break
    
    if found==True:
        break
    else:
        tries+=1

if found==True:
    print("\nFound positions")
else:
    print("\nNo positions found, ran out of tries")          



