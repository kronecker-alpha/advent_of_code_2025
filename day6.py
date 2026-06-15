import numpy as np
from math import prod

path = "input/day6.txt"

with open(path, "r") as f:
    data = [line.rstrip().split(" ") for line in f]

data = [[i for i in item if i != ''] for item in data]

arr = np.transpose(np.array(data))

#PART ONE

total = 0

for line in arr:
    args = [int(i) for i in line if i!='*' and i!='+']
    if line[-1] == '*':
        total += prod(args)
    else:
        total += sum(args)


#PART TWO

with open(path, "r") as f:
    data = [[char for char in line] for line in f]

arr = np.transpose(np.array(data))

def list_to_int(lst):
    result = ''
    for num in lst:
        result += num
    return int(result)

total = 0
args = []
for i in range(0, len(arr)):
    if [x for x in arr[i] if x != np.str_(' ')] == []:
        args = [list_to_int(p) for p in args]
        if temp == '*':
            total += prod(args)
        else:
            total += sum(args)
        args = []
    else:
        if arr[i][-1] == '*':
            temp = '*'
        elif arr[i][-1] == '+':
            temp = '+'
        args.append([x for x in arr[i] if x != np.str_(' ') and x!='*' and x!='+'])
    

print(total)




