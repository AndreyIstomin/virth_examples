import math
from collections import namedtuple

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


def quick_sort(list_to_sort):

    def sort(l, r):

        i = l
        j = r
        x = list_to_sort[(l + r) / 2]

        while i <= j:

            # search for the first element greater or equal then x
            while list_to_sort[i] < x:
                i += 1

            # search for the first from right element less or equal then x
            while list_to_sort[j] > x:
                j -= 1

            if i <= j:

                swap = list_to_sort[i]
                list_to_sort[i] = list_to_sort[j]
                list_to_sort[j] = swap
                i += 1
                j -= 1

        if l < j:
            sort(l, j)

        if i < r:
            sort(i, r)

    sort(0, len(list_to_sort) - 1)

    return list_to_sort


def quick_sort_non_recursive(list_to_sort):

    stack = [(0, len(list_to_sort) - 1)]

    while len(stack) > 0:

        (l, r) = stack.pop()

        while l < r:
            i = l
            j = r
            x = list_to_sort[(l + r)/2]

            while i <= j:

                while list_to_sort[i] < x:
                    i += 1
                while list_to_sort[j] > x:
                    j -= 1

                if i <= j:
                    swap = list_to_sort[i]
                    list_to_sort[i] = list_to_sort[j]
                    list_to_sort[j] = swap
                    i += 1
                    j -= 1
            # Choose the shortest sort interval
            if j - l < r - i:
                if i < r:
                    # Will be done later
                    stack.append((i, r))
                r = j
            else:
                if j > l:
                    stack.append((l, j))
                l = i


def built_in_sort(list_to_sort):

    list_to_sort.sort()
    return list_to_sort


if __name__ == '__main__':

    import os

    tester = SortingTester(min_len_log_2=10, max_len_log_2=13)

    tester.run([
        straight_insertion,
        binary_insertion,
        straight_selection,
        bubble_sort,
        shaker_sort,
        shell_sort_9531,
        heap_sort,
        quick_sort,
        quick_sort_non_recursive,
        built_in_sort
    ])

    # # tester.print_results()
    # tester.csv_to_file("d:/sort_results.csv")
    tester.write_to_db(os.path.dirname(__file__) + "/result_db.accdb")





