import sys

students = dict()

with open(sys.argv[1]) as f:
    for line in f:
        name, dep = line.strip().split(':')
        students[name] = dep.split(',')

names = sys.argv[2]

with open('outputFile.txt', 'w') as f:
    for i in names.split(','):
        try:
            f.write(f"Name: {i}, University: {students[i][0]}, {students[i][1]} ")
        except KeyError:
            f.write(f"No record of '{i}' was found! ")