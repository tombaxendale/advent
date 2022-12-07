import pandas as pd

f = open('2/guide.txt', 'r')
guide = f.read()
guide = guide.split("\n")

guide = [answer.split(' ') for answer in guide]

def score(opponent, response):
    #equate response to opponent's letters
    response = chr(ord(response) - 23)
    i = 0

    #convert to a, b, c == 1, 2, 3 score
    choice_score = ord(str.lower(response)) - 96
    i += choice_score 

    #draw
    if opponent == response:
        i += 3

    #win
    elif (opponent == "A" and response == "B") or (opponent == "B" and response == "C") or (opponent == "C" and response == "A"):
        i += 6

    return i

a = 0

for answer in guide:
    new_score = score(answer[0],answer[1])
    answer.append(new_score)
    a += new_score

print(a)
