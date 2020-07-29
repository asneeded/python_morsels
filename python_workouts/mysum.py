
def mysum(*args):
    new = []
    for item in args:
        if not isinstance(item, int):
            if isinstance(item, str):
                raise TypeError
            for i in item:
                new.append(i)
        else:
            new.append(item)
    total = 0
    for num in new:
        total += num
    return total

if __name__ == "__main__":
    print(mysum(1,2,3,[4,6]))