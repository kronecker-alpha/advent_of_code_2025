path = "input/day3.txt"

with open(path, "r") as f:
    data = [line.rstrip() for line in f]

#PART ONE
total = 0

for line in data:
    line = [int(i) for i in line]
    num1 = max(line[:len(line)-1])
    ind = line.index(num1)
    num2 = max((line[ind+1:len(line)]))
    num = str(num1)+str(num2)
    total += int(num)

#print(total)

#PART TWO
total = 0

for line in data:
    line = [int(i) for i in line]
    num = []
    num_ind = [-1]
    for i in range(1,13):
        next_num = max(line[num_ind[i-1]+1:len(line)-12+i])
        num.append(next_num)
        indicies = [k for k, x in enumerate(line) if x == next_num]
        ind = [k for k in indicies if k > num_ind[i-1]][0]
        num_ind.append(ind)
    num = [str(i) for i in num]     
    total = total + int(''.join(num))


print(total)



