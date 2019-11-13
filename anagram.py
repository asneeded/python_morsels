
import string

def is_anagram(word1, word2):
    *first, = word1.lower().replace(" ", "")
    *second, = word2.lower().replace(" ", "").translate(())
    if sorted(first) == sorted(second):
        return True
    return False
    


if __name__ == '__main__':
    print(is_anagram('tea', 'eat'))
