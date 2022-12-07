import string

f = open('3/rucksack.txt', 'r')
rucksacks = f.read()
rucksacks = rucksacks.split("\n")

j = 0

#split the rucksack in two halves
for rucksack in rucksacks:
    strlen = len(rucksack)
    strlenh = int(strlen/2)
    rucksacks[j] = [rucksack[0:strlenh], rucksack[strlenh:strlen]]
    j += 1

double_items = {}

for rucksack in rucksacks: # entire list of rucksacks
    for item in rucksack[0]: # loop through contents of first compartment per rucksack
        if item in rucksack[1]:
            double_items[rucksack[0]] = item
            # Q for Collin
            # I first tried to break the for loop when item was found in rucksack[1] but the break did not work -- why?

#create string of all lowercase and uppercase letters to find priority value per item
alphabet = string.ascii_lowercase + string.ascii_uppercase
values = [alphabet.find(value) + 1 for key, value in double_items.items()]

print(sum(values))