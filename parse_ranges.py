def parse_ranges(ranges):
    final = []
    numbers = ranges.split(',')
    for number in numbers:
        first, last = number.split('-')
        *new, = range(int(first), int(last)+1)
        final.extend(new)
    
    return final




if __name__ == '__main__':
    print(parse_ranges('1-2,4-4,8-10'))