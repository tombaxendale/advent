from copy import deepcopy

f = open('8/input.txt', 'r')
forest = f.read()
forest = forest.split("\n")

forest = [list(map(int,treeline)) for treeline in forest]
forest_vis = deepcopy(forest) # map of visible trees in forest. deepcopy creates new object in memory

forest_depth = len(forest) 
forest_width = len(forest[0]) # forest is rectangular

i = 0 # treeline row number

for treeline in forest:
    j = 0 # tree number in row
    for tree in treeline:
        if i == 0 \
            or i == forest_depth - 1 \
            or j == 0 \
            or j == forest_width - 1: # if tree is on edge of forest 
            forest_vis[i][j] = 'x'
            j += 1
            continue

        tree_height_left = max(treeline[0:j])
        tree_height_right = max(treeline[j+1:forest_width])
        if tree_height_left < tree or tree_height_right < tree:
            forest_vis[i][j] = 'x'
            j += 1
            continue
        j += 1
    i += 1

forest_transposed = [list(treeline) for treeline in zip(*forest)]
forest_transposed_depth = len(forest_transposed) 
forest_transposed_width = len(forest_transposed[0]) # forest is rectangular

i = 0
for treeline in forest_transposed:
    j = 0 # tree number in row
    for tree in treeline:
        if i ==0 \
            or i == forest_transposed_depth - 1\
            or j == 0 \
            or j == forest_transposed_width - 1:
            j += 1
            continue

        #print(treeline)
        tree_height_left = max(treeline[0:j])
        tree_height_right = max(treeline[j+1:forest_transposed_width])

        if tree_height_left < tree or tree_height_right < tree:
            print ('assigning', i, j, tree, 'value of x')
            try:
                forest_vis[j][i] = 'x'
            except Exception as e:
                print(j, i, e)
            j += 1
            continue
        j += 1
    i += 1

vis_count = 0

for treeline in forest_vis:
    for tree in treeline:
        if tree == 'x':
            vis_count += 1

for treeline in forest_vis:
    print(treeline,'\n')
print(vis_count)