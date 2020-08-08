def firstlast(item):
    return item[:1] + item[-1:]


def odd_even_sum(items):
    evens = 0
    odds = 0
    for i, k in enumerate(items):
        if i % 2 == 0:
            evens += k
        else:
            odds += k
    return [evens, odds]

def plus_minus(items):
    total = items[0]
    symbol = 0
    for i, k in enumerate(items):
        if i != 0:
            if symbol % 2 == 0:
                total += k
                symbol += 1
            else:
                total -= k
                symbol += 1
    return total

if __name__ == "__main__":
    print(plus_minus([10,20,30,40,50,60]))