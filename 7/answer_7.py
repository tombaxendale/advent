# two methods required: cd and ls
# cd can have one of three operations
#    "x"  : go one level down to directory x
#    ".."  : go one level out to outer directory
#    "/"   : go to outermost directory    
# ls lists all objects in current directory
#
# my directory will be a dict containing lists of dicts and other files
#
#
#

output = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j"""

output = output.split("\n")

from collections import defaultdict

master_dir = {"/" : []}
current_dir = []

def goto_directory(command):
    dir = command[2]
    if not current_dir:
        current_dir = dir
    elif dir == "/":
        

for line in output:
    if line.startswith("$"): # user commands
        command = line.split(" ")
        if command[1] == "cd":




#def cd(operation):
