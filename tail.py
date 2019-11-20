def tail(input, many):
    final = []
    if many <= 0:
        return final
    
    return list(input[-many:])

if __name__ == '__main__':
    print(tail([1,2,4,6,8,6],3))