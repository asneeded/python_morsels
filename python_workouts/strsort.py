def strsort(word):

    to_sort = [ x for x in word ]
    return ''.join(sorted(to_sort))

if __name__ == "__main__":
    print(strsort('cda'))