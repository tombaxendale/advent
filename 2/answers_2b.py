f = open('2/guide.txt', 'r')
guide = f.read()
guide = guide.split("\n")

guide = [answer.split(' ') for answer in guide]
i = 0

for answer in guide:
    opponent = answer[0]
    result = answer[1]
    #lose
    if result == 'X':
        if opponent == "A":
            response = "C"
        elif opponent == "B":
            response = "A"
        elif opponent == "C":
            response = "B"
    #draw
    elif result == 'Y':
        response = opponent
        i += 3
    #win
    elif result == "Z":
        if opponent == "A":
            response = "B"
        elif opponent == "B":
            response = "C"
        elif opponent == "C":
            response = "A"
        i += 6
    
    if response == "A":
        i += 1
    elif response == "B":
        i += 2
    elif response == "C":
        i += 3
print(i)
