
def interleave(first, second):
    final = []
    for key, value in enumerate(first):
        final.extend([value, second[key]])
    
    return final



if __name__ == '__main__':
    print(interleave([1,2,3,4],[5,6,7,8]))