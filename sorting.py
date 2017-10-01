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


if __name__ == '__main__':

    tester = SortingTester(min_len_log_10=2, max_len_log_10=3)

    tester.run([
        ('straight_insertion', straight_insertion),
        ('binary_insertion', binary_insertion)
    ])

    tester.print_results()

    # list_to_sort = SortingTester.unorder_range(10, 10)
    #
    # print binary_insertion(list_to_sort)









