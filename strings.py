str = 'str.txt'

file = open(str, 'r')

def read_words():
    words = []
    for word in file.readlines():
        words.append(word)
    return

    for w in words:
        print(word)

read_words()

file.close()