def minmax(items, *, key=None):
    try:
        return min(iter(items), key=key ),max(iter(items), key=key)
    except StopIteration as e:
        



if __name__ == "__main__":
    words = ["alfalfa", "animal", "apple", "acoustic"]
    print(minmax(words, key=len))
