import random


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


def unorder_range(range_size):

    init_list = range(0, range_size)

    return [init_list.pop(int((range_size - i) * random.random())) for i in xrange(0, range_size)]

def create_list_to_sort(list_size):

    return {
        'ordered': range(0, list_size),
        'inverted': range(list_size - 1, -1),
        'random': [int(list_size * random.random()) for i in xrange(list_size)]
    }

if __name__ == '__main__':

    # list_size = []
    #
    # list_to_sort = \
    #     [
    #         # 'ordered':
    #     ]
    #
    # sorting = [straight_insertion]
    #
    # # TO BE CONTINUED...

    list_to_sort = [4, 1, 3, 19, 0]

    straight_insertion(list_to_sort)

    print list_to_sort
