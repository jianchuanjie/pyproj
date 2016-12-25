import string


def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


def total_words(hist):
    return sum(hist.values())


def different_words(hist):
    return len(hist)


def most_common(hist):
    t = []
    for key, valus in hist.items():
        t.append((valus, key))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are:')
    i = 1
    for freq, word in t[:num]:
        print('%d:' % i, word, freq, sep='\t')
        i += 1


hist = process_file('emma.txt')

if __name__ == '__main__':
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))
    print_most_common(hist, 11)
