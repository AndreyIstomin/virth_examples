import math

from sorting_tester import SortingTester


def straight_insertion(list_to_sort):

    n = len(list_to_sort)
    list_to_sort.append(0)

    for i in xrange(n - 2, -1, -1):

        x = list_to_sort[-1] = list_to_sort[i]

        j = i

        while x > list_to_sort[j + 1]:

            list_to_sort[j] = list_to_sort[j + 1]
            j += 1

        list_to_sort[j] = x

    list_to_sort.pop()

    return list_to_sort


def binary_insertion(list_to_sort):

    n = len(list_to_sort)

    for i in xrange(n - 2, -1, -1):

        x = list_to_sort[i]
        l = i
        r = n - 1

        while l < r:

            m = -((l + r) / -2)

            if list_to_sort[m] <= x:

                l = m

            else:

                r = m - 1

        for j in xrange(i, r):

            list_to_sort[j] = list_to_sort[j + 1]

        list_to_sort[r] = x

    return list_to_sort


def straight_selection(list_to_sort):

    n = len(list_to_sort)

    for i in xrange(0, n - 1):

        k = i
        x = list_to_sort[i]

        for j in xrange(i + 1, n):

            if list_to_sort[j] < x:

                k = j
                x = list_to_sort[j]

        list_to_sort[k] = list_to_sort[i]
        list_to_sort[i] = x

    return list_to_sort


def bubble_sort(list_to_sort):

    n = len(list_to_sort)

    for i in xrange(1, n):
        for j in xrange(n - 1, i - 1, -1):

            if list_to_sort[j - 1] > list_to_sort[j]:
                x = list_to_sort[j - 1]
                list_to_sort[j - 1] = list_to_sort[j]
                list_to_sort[j] = x

    return list_to_sort


def shaker_sort(list_to_sort):

    n = len(list_to_sort)

    l = 1
    r = n - 1
    k = n - 1

    while l <= r:

        for j in xrange(r, l - 1, -1):

            if list_to_sort[j - 1] > list_to_sort[j]:

                x = list_to_sort[j - 1]
                list_to_sort[j - 1] = list_to_sort[j]
                list_to_sort[j] = x
                k = j

        l = k + 1

        for j in xrange(l, r + 1):

            if list_to_sort[j - 1] > list_to_sort[j]:

                x = list_to_sort[j - 1]
                list_to_sort[j - 1] = list_to_sort[j]
                list_to_sort[j] = x
                k = j

        r = k - 1

    return list_to_sort


def shell_sort_9531(list_to_sort):

    n = len(list_to_sort)

    h = [9, 5, 3, 1]

    list_to_sort.extend([0] * h[0])

    for step in h:

        barrier_shift = step

        for i in xrange(n - 1 - step, -1, -1):

            x = list_to_sort[n - 1 + barrier_shift] = list_to_sort[i]  # barrier

            j = i

            while x > list_to_sort[j + step]:
                list_to_sort[j] = list_to_sort[j + step]
                j += step

            list_to_sort[j] = x

            barrier_shift -= 1
            if barrier_shift == 0:
                barrier_shift = step

    for i in xrange(0, h[0]):
        list_to_sort.pop()

    return list_to_sort


# Floyd shift
def sift(l, r, array):

    i = l
    j = 2 * l + 1
    x = array[l]

    if j < r and array[j] < array[j + 1]:
        j = j + 1

    while j <= r and x < array[j]:

        array[i] = array[j]
        i = j
        j = 2 * i + 1

        if j < r - 1 and array[j] < array[j + 1]:

            j = j + 1

    array[i] = x


def heap_sort(list_to_sort):

    n = len(list_to_sort)

    l = n / 2 + 1
    r = n - 1

    # seap left part of the input list, while the base level of the heap remains unordered
    while l > 0:

        l -= 1
        sift(l, r, list_to_sort)

    # seap each element of the base level of the heap one by one, to make tree fully ordered;
    while r > 0:

        x = list_to_sort[0]
        list_to_sort[0] = list_to_sort[r]
        list_to_sort[r] = x
        r -= 1
        sift(l, r, list_to_sort)

    return list_to_sort


if __name__ == '__main__':

    tester = SortingTester(min_len_log_2=12, max_len_log_2=13)

    tester.run([
        straight_insertion,
        binary_insertion,
        straight_selection,
        bubble_sort,
        shaker_sort,
        shell_sort_9531,
        heap_sort
    ])

    tester.print_results()

    # list_to_sort = SortingTester.unorder_range(20, 20)
    #
    # print heap_sort(list_to_sort)





