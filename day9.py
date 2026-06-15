path = "input/day9.txt"

with open(path, "r") as f:
    data = [line.rstrip().split(",") for line in f]


def ssize(l1,l2):
    [x1,y1] = l1
    [x2,y2] = l2
    x = abs(int(x1) - int(x2)) + 1
    y = abs(int(y1) - int(y2)) + 1
    return int(x * y)

maxx = 0
for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        s = ssize(data[i], data[j])
        if s > maxx:
            maxx = s
print(maxx)

#PART TWO


