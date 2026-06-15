from helpers import factors

path = "input/day2.txt"

with open(path, "r") as f:
    line = f.readline()
    data = line.split(",")

#PART ONE
total = 0
for rang in data:
    lower, upper = rang.split("-")
    for i in range(int(lower),int(upper)+1):
        i = str(i)
        l = len(i)
        m = l // 2
        if len(i)%2==0:
            if i[:m] == i[m:]:
                total = total + int(i)

#print(total)

#PART TWO
total = []
for rang in data:
    lower, upper = rang.split("-")
    for i in range(int(lower),int(upper)+1):
        flag = False
        i = str(i)
        l = len(i)
        facts = [j for j in factors(l) if j != l ]

        for x in facts:
            sects = [i[m*x:(m+1)*x] for m in range(0,int(l/x))]
            if len(set(sects)) == 1:
                total.append(int(i))
                
new_total = sum(set(total))
print(new_total)

