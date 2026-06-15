from math import cbrt
path = "input/day8.txt"

with open(path, "r") as f:
    data = [line.rstrip().split(",") for line in f]


def eu_dis(list1, list2):
    [e1,e2,e3] = [int(list1[i]) - int(list2[i]) for i in range(0,3)]
    total = e1**2 + e2**2 + e3**2
    return cbrt(total)

'''
dist = []
pairs = []

for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        dist.append(eu_dis(data[i],data[j]))
        pairs.append({i,j})

circuits = [{i} for i in range(0,len(data))]
for i in range(0,1000):
    minn = min(dist)
    idx = dist.index(minn)
    [x,y] = pairs[idx]
    #find x and y in list
    [ix] = [p for p in range(0,len(circuits)) if x in circuits[p] ]
    [iy] = [p for p in range(0,len(circuits)) if y in circuits[p] ]
    #if different, add together
    if ix != iy:
        a = circuits[ix]
        b = circuits[iy]
        circuits.remove(a)
        circuits.remove(b)
        circuits.append(a.union(b))
    #remove from old list idx
    dist.pop(idx)
    pairs.pop(idx)

#find three biggest sets

a1 = max(circuits, key=len)
circuits.remove(a1)
a2 = max(circuits, key=len)
circuits.remove(a2)
a3 = max(circuits, key=len)
#print(len(a1)*len(a2)*len(a3))
'''

#part two

dist = []
pairs = []

for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        dist.append(eu_dis(data[i],data[j]))
        pairs.append({i,j})

circuits = [{i} for i in range(0,len(data))]
for i in range(0,100000000):
    minn = min(dist)
    idx = dist.index(minn)
    [x,y] = pairs[idx]
    #find x and y in list
    [ix] = [p for p in range(0,len(circuits)) if x in circuits[p] ]
    [iy] = [p for p in range(0,len(circuits)) if y in circuits[p] ]
    #if different, add together
    if ix != iy:
        a = circuits[ix]
        b = circuits[iy]
        circuits.remove(a)
        circuits.remove(b)
        circuits.append(a.union(b))
    #remove from old list idx
    dist.pop(idx)
    pairs.pop(idx)
    if len(circuits) == 1:
        print(x,y)
        exit()
