import timeit

f = open('calories.txt', 'r')
calories = f.read()
calories = calories.split("\n")

def calorie_count(calories = calories):
    elf = 0
    elf_list = [0]
    for i in calories:
        if i == "":
            elf += 1
            elf_list.append(0)
        else:
            elf_list[elf] += int(i)
            pass
    return elf_list

answer_1a = max(calorie_count())

print(answer_1a)

def top_n(calorie_count = calorie_count(), n = 3):
    calorie_count.sort(reverse = True)
    calorie_count = calorie_count[0:n]
    return sum(calorie_count)

answer_1b = top_n()
print(answer_1b)

#print(timeit.timeit(stmt = elfing, number = 1))