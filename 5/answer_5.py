from collections import defaultdict

f = open('5/crate_order.txt', 'r')
input = f.read()

# split text input into crates and instructions
crates_raw = input.split("\n\n")[0]
crates_raw = crates_raw.split("\n")
crates_final = []

commands = input.split("\n\n")[1]
commands = commands.split("\n")

# create new dictionary with list as default value for new keys. enables instant list appending to new keys
crate_dict = defaultdict(list)


# process the text input: remove every fourth character in each row, leaving behind only crates or crate spaces
def remove_nth_char(string, n):

    string = list(string)
    del string[n-1::n]
    string = "".join(string)
    return string

for row in crates_raw:
    if '1' in row: # skip final row with crate stack numbers
        break
    else:
        row = remove_nth_char(row, 4)
        row = row.replace("   ","[ ]") # log crate spaces
        row = row.replace("[","").replace("]","") # remove square brackets
        crates_final.append(list(row))

for row in crates_final: # iterate through each row of crates and add to the corresponding crate pile (1, 2, 3...)
    i = 1
    for crate in row:
        if crate != " ":
            crate_dict[i].append(crate) # list is created upon key creation (defaultdict)
        i += 1

# sort dict by key values (1, 2, 3...)
crate_dict = dict(sorted(crate_dict.items()))

def move_crate(command):
    _from = int(command.split(" ")[3])
    _to = int(command.split(" ")[5])
    
    crate = crate_dict[_from][0] # first crate in _from crate stack
    del crate_dict[_from][0] # delete from _from crate stack
    crate_dict[_to].insert(0, crate) # add to beginning (top) of _to crate stack

def move_crates(command):
    _move = int(command.split(" ")[1])
    for i in range(0, _move):
        move_crate(command)

#for command in commands:
#    move_crates(command = command)

#answer_5a = [value[0] for key, value in crate_dict.items()]
#print(answer_5a)

# create a block of crates, remove from original stack and add to new stack in reverse order
def move_crate_block(command):
    _move = int(command.split(" ")[1])
    _from = int(command.split(" ")[3])
    _to = int(command.split(" ")[5])
    
    crate_block = crate_dict[_from][0:_move]
    del crate_dict[_from][0:_move]
    crate_block.reverse() # first n crates within _from crate stack and reverse crate order (bottom crate now moves first)

    for crate in crate_block:
        crate_dict[_to].insert(0, crate)

for command in commands:
   move_crate_block(command = command)

answer_5b = [value[0] for key, value in crate_dict.items()]
print(answer_5b)