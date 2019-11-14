def parse_ranges(ranges):
    for number in ranges.split(','):
        if '-' in number:
            first, last = number.split('-')
            for item in range(int(first), int(last)+1):
                yield item
        else:
            yield int(number)
            

# def parse_ranges(ranges):
#     return ( number for number in ranges.split(',')  )
    
    



if __name__ == '__main__':
    print(list(parse_ranges('1-2,4-4,8-10')))