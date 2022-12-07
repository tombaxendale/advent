import string

f = open('3/rucksack.txt', 'r')
rucksacks = f.read()
rucksacks = rucksacks.split("\n")

groups = []

for rucksack in rucksacks:
    # find elf number in rucksack list
    elf_nr = rucksacks.index(rucksack)
    # convert elf number to group number via floor division
    group_nr = int(elf_nr // 3)
    # try adding the elf to the group's list within the groups list
    try:
        groups[group_nr].append(rucksack)
    # else create list if doesn't exist
    except IndexError:
        groups.append([])
        groups[group_nr].append(rucksack)

final_items = []

for group in groups:
    # loop through every item in rucksack 1 to see if in rucksacks 2 & 3 also
    rucksack = group[0]
    for item in rucksack:
        if item in group[1] and item in group[2]:
            final_items.append(item)
            break

alphabet = string.ascii_lowercase + string.ascii_uppercase
values = [alphabet.find(item) + 1 for item in final_items]

answer = sum(values)

print(answer)