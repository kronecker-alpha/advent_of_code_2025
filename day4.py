path = "input/day4.txt"

with open(path, "r") as f:
    data = [line.rstrip() for line in f]

data = [[i for i in line] for line in data]

#PART ONE

count = 0
for x in range(0, len(data[0])): #x axis across a line
    for y in range(0, len(data)): #y axis down data
        pos_all = [(i,j) for i in range(x-1,x+2) for j in range(y-1,y+2) if i>=0 and i<len(data[0]) and j>=0 and j<len(data)]
        pos_vals = [data[i][j] for (i,j) in pos_all if i != x or j!=y]
        if pos_vals.count("@") < 4 and data[x][y]=="@":
            count += 1

#print(count)

#PART TWO
count = 1
total = 0

while count>0:
    count = 0
    edits = []
    for x in range(0, len(data[0])): #x axis across a line
        for y in range(0, len(data)): #y axis down data
            pos_all = [(i,j) for i in range(x-1,x+2) for j in range(y-1,y+2) if i>=0 and i<len(data[0]) and j>=0 and j<len(data)]
            pos_vals = [data[i][j] for (i,j) in pos_all if i != x or j!=y]
            if pos_vals.count("@") < 4 and data[x][y]=="@":
                count += 1 #mark position
                edits.append((x,y))
    total += count
    #edit all old @s to dots
    for (k,l) in edits:
        data[k][l] = "."

print(total)
    
