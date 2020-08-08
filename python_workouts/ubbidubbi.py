

def ubbidubbi(words):
    translate = []
    for word in words.split():
        new = ''
        for letter in word:
            if letter in 'aeiou':
                new += f'ub{letter}'
            else:
                new += letter
        translate.append(new)
    return ' '.join(translate)

if __name__ == "__main__":
    print(ubbidubbi('Do you wa)