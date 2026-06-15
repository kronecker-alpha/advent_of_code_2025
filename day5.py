path = "input/day5.txt"

with open(path, "r") as f:
    data = [line for line in f]

clean_data1 = []
clean_data2 = []

flag = False
for line in data:
    if line == "\n":
        flag = True
        continue
    if flag == False:
        clean_data1.append(line.rstrip())
    else:
        clean_data2.append(int(line.rstrip()))

marks = [0 for i in clean_data2]
maxx = 0
minn = 9999999999999999999999

#PART ONE
for rang in clean_data1:
    lower, upper = rang.split("-")
    lower = int(lower)
    upper = int(upper)
    if upper > maxx:
        maxx = upper
    if lower < minn:
        minn = lower
    for x in range(0,len(clean_data2)):
        if (clean_data2[x] <= (upper)) and (clean_data2[x]>= lower):
            marks[x] = 1

#print(sum(marks))

#PART TWO
total = 0
ranges = []
for rang in clean_data1:
    lower, upper = rang.split("-")
    ranges.append((int(lower), int(upper)))

#using sympy union
from sympy import Interval, Union, FiniteSet

intervals = [Interval(lower,upper) for (lower,upper) in ranges]

u = Union(*intervals)

for subset in u.args:
    if type(subset) == FiniteSet:
        pass
    else:
        total += subset.end - subset.start + 1


print(total)
