def pig_latin(words):
    converted = []
    for word in words.split():
        if word[0] in 'aeiou':
            converted.append(word + 'way')
        elif word.isalpha():
            converted.append(word[1:] + word[0] + 'ay')
    return ' '.join(converted)

if __name__ == "__main__":
    print(pig_latin('computer air'))