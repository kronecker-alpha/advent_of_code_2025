#helper functions

def factors(x):
    fs = []
    for i in range(1,x+1):
        if x % i == 0:
            fs.append(i)
    return fs

def get_indices(lst, target):
    return [index for index, element in enumerate(lst) if element == target]


if __name__ == "__main__":
    facts = [j for j in factors(10) if j != 10 ]
    print(facts)