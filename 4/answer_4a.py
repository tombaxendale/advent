f = open('4/assignments.txt', 'r')
assignments = f.read()
assignments = assignments.split("\n")

counter_4a = 0
counter_4b = 0

# transform the text into a list of lists e.g. [[[46, 74], [46, 76]],[[2, 70], [3, 21]]]
for assignment_pair in assignments:
    assignment_pair = assignment_pair.split(",")

    i = 0
    for assignment in assignment_pair:
        assignment_pair[i] = [int(x) for x in assignment.split("-")]
        i += 1

    # answer 4a: check if assignment 1 is fully within assignment 2 and vice versa
    if (assignment_pair[0][0] <= assignment_pair[1][0] and assignment_pair[0][1] >= assignment_pair[1][1])\
        or (assignment_pair[1][0] <= assignment_pair[0][0] and assignment_pair[1][1] >= assignment_pair[0][1]):
        counter_4a += 1
    # answer 4b:    if the upper bound of assignment 1 (2) is higher than the lower bound of assignment 2 (1) in a given assignment pair
    #               or vice versa, there is overlap
    #               so count when this doesn't happens

    if not (assignment_pair[0][1] < assignment_pair[1][0]\
        or assignment_pair[1][1] < assignment_pair[0][0]):
        counter_4b += 1

print(counter_4a)
print(counter_4b)

