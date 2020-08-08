import string

def shift_punct(word):
    pass

def capital(word):
    pass


def pig_latin(words):
    converted = []
    for word in words.split():
        if word[0].lower() in 'aeiou':
            new = word + 'way'
            if word[0].isupper():
                new = new.capitalize()
            converted.append(new)
        else:
            if word[0].isupper():
                new = word[1:] + word[0] + 'ay'
                converted.append(new.lower().capitalize())
            else:
                converted.append(word[1:] + word[0] + 'ay')
    return ' '.join(converted)

if __name__ == "__main__":
    print(pig_latin('this is a test translation')) 