path = "input/day1.txt"

with open(path, "r") as f:
    data = [line.rstrip() for line in f]

#PART 1
dial = 50
passw = 0

for line in data:
    if line[0] == 'R':
        dial += int(line[1:])
    else:
        dial -= int(line[1:])
    dial = dial % 100
    if dial == 0:
        passw += 1

#print(passw)

#PART 2
dial = 50
passw = 0
prev = 50
flag = False

for line in data:
    if line[0] == 'R':
        dial += int(line[1:])
        if dial >= 100:
            passw += abs(dial) // 100

    else:
        dial -= int(line[1:])
        if dial <= 0:
            if prev == 0:
                passw += (abs(dial) // 100)
            else:
                passw += (abs(dial) // 100) + 1
    
    dial = dial % 100
    prev = dial
    

print(passw)