def hex_output(*args):
    hexnum, *rest = args
    decimal = 0 
    convert = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    # {'0':0,;'1':1,'2':2,'3'}
    for item in hexnum:
        if not item.isdigit():
            decimal += 2 ** convert[item]
        else:
            decimal += 2 ** int(item)
    return decimal

if __name__ == "__main__":
    print(hex_output('50'))
