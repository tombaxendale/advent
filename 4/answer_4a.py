f = open('4/assignments.txt', 'r')
assignments = f.read()
assignments = assignments.split("\n")

counter = 0

for assignment_pair in assignments:
    assignment_pair = assignment_pair.split(",")

    i = 0
    for assignment in assignment_pair:
        assignment_pair[i] = [int(x) for x in assignment.split("-")]
        i += 1
        
    if (assignment_pair[0][0] <= assignment_pair[1][0] and assignment_pair[0][1] >= assignment_pair[1][1])\
        or (assignment_pair[1][0] <= assignment_pair[0][0] and assignment_pair[1][1] >= assignment_pair[0][1]):
        counter += 1

print(counter)