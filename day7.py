import numpy as np
from helpers import get_indices

path = "input/day7.txt"

with open(path, "r") as f:
    data = [[x for x in line if x != '\n'] for line in f]

arr = np.array(data, dtype=np.dtype('U100'))

#PART ONE

count = 0
for x in range(0,len(arr)-1):
    line = arr[x]
    ss = get_indices(line,"S")
    for idx in ss:
        if arr[x+1][idx] == '^':
            arr[x+1][idx-1] = 'S'
            arr[x+1][idx+1] = 'S'
            count += 1
        else:
            arr[x+1][idx] = 'S'

#print(count)


#PART TWO

count = 0
for x in range(0,len(arr)-1):
    line = arr[x]
    ss =[]
    for l in range(0,len(arr[x])):
        try:
            int(arr[x][l])
            ss.append(l)
        except ValueError:
            pass
    for idx in ss:
        if arr[x+1][idx] == '^':
            if arr[x+1][idx-1] == '.':
                arr[x+1][idx-1] = arr[x][idx]
            else:
                arr[x+1][idx-1] = int(arr[x+1][idx-1]) + int(arr[x][idx])
            if arr[x+1][idx+1] == '.':
                arr[x+1][idx+1] = arr[x][idx]
            else:
                arr[x+1][idx+1] = int(arr[x+1][idx+1]) + int(arr[x][idx])
        elif arr[x+1][idx] == '.':
            arr[x+1][idx] = arr[x][idx]
        else: #is a number
            arr[x+1][idx] = int(arr[x+1][idx]) + int(arr[x][idx])

total = 0
for val in arr[-1]:
    try:
        total = int(total) + int(val)
    except:
        pass
print(total)