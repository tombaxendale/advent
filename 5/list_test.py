
sample = "move 1 from 2 to 4"

_move = int(sample.split(" ")[1])
_from = int(sample.split(" ")[3])
_to = int(sample.split(" ")[5])

print(_move, _from, _to)

for i in range(0,_move):
    print(i)
