import time

def preprocess(pattern):

    pattern_length = len(pattern)

    d = {}

    for i in xrange(0, pattern_length):

        d[pattern[i - 1]] = pattern_length - i

    return d


def preprocess_2(pattern):

    pattern_length = len(pattern)

    arr = [pattern_length] * 256

    for i in xrange(0, pattern_length):

        arr[ord(pattern[i - 1])] = pattern_length - i

    return arr


def run(text, table, pattern):

    pattern_len = len(pattern)

    start_i = i = j = pattern_len - 1

    while i < len(text) and j >= 0:

        if text[i] == pattern[j]:

            i -= 1
            j -= 1
        else:

            i = start_i + (table[text[start_i]] if text[start_i] in table else pattern_len)
            j = pattern_len - 1
            start_i = i

    if j == -1:

        return start_i - pattern_len + 1

    return -1


def run_2(text, array, pattern):

    pattern_len = len(pattern)

    start_i = i = j = pattern_len - 1

    while i < len(text) and j >= 0:

        if text[i] == pattern[j]:

            i -= 1
            j -= 1
        else:
            i = start_i + array[ord(text[start_i])]
            j = pattern_len - 1
            start_i = i

    if j == -1:

        return start_i - pattern_len + 1

    return -1


if __name__ == '__main__':

    pattern = 'data'

    table = preprocess(pattern)

    t = time.time()

    for i in xrange(1000000):
        run('atataatametaatatadata', table, pattern)

    print 'dictionary approach: %f s' % (time.time() - t) # faster

    arr = preprocess_2(pattern)

    t = time.time()

    for i in xrange(1000000):
        run_2('atataatametaatatadata', arr, pattern)

    print 'array approach: %f s' % (time.time() - t)





