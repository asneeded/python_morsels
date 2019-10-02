def compact(items):
    final = []
    
    for i,v in enumerate(items):
        if v != items[i-1]:
            final.append(v)
    return final


if __name__ == "__main__":                              
    print(compact([1,1,1,2,2,3,2,3,4,4,5]))
    print(compact([1,1,1,1,1,1,1,1]))
    print(compact([None, "",0, []]))