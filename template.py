#template

path = "input/day1.txt"

with open(path, "r") as f:
    data = [line.rstrip() for line in f]

print(data)