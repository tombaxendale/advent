from collections import defaultdict

f = open('5/crate_order.txt', 'r')
input = f.read()
crates = input.split("\n\n")[0] # split text input into crates and instructions
crates = crates.split("\n")

commands = input.split("\n\n")[1]
commands = commands.split("\n")

crate_dict = defaultdict(list)

def remove_nth_char(row, n):

    row = list(row)
    del row[n-1::n]
    row = "".join(row)
    return row

crates_new = []

for row in crates:
    if '1' in row: # skip final row with crate stack numbers
        break
    else:
        row = remove_nth_char(row, 4)
        row = row.replace("   ","[ ]") # count empty crates
        row = row.replace("[","").replace("]","") # remove square brackets
        crates_new.append(list(row))

for row in crates_new: # iterate through each row of crates and add to the corresponding crate pile (1, 2, 3...)
    i = 1
    for crate in row:
        if crate != " ":
            crate_dict[i].append(crate)
        i = i+1

# sort dict by key values
crate_dict = dict(sorted(crate_dict.items()))

def move_crate(command):
    _from = int(command.split(" ")[3])
    _to = int(command.split(" ")[5])
    
    crate = crate_dict[_from][0] # first crate in _from crate stack
    crate_dict[_to].insert(0, crate) # add to beginning (top) of _to crate stack
    del crate_dict[_from][0] # delete from _from crate stack

    #print("from", crate_dict[_from])
    #print("to ", crate_dict[_to])

def move_crates(command):
    _move = int(command.split(" ")[1])
    for i in range(0, _move):
        move_crate(command)

for command in commands:
    move_crates(command = command)

print(crate_dict)