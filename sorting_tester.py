import random
import time
import pyodbc
from collections import namedtuple


class SortingTester:

    class WrongOrderError(Exception):

        def __init__(self, sort_name):
            self.__sortName = sort_name

        def __str__(self):
            return 'sorting %s has error' % self.__sortName

    RESULT_DESCRIPTOR = namedtuple('RESULT_DESCRIPTOR', 'arr_len, order_degree, case_name, sort_name, time')

    DEFAULT_RELATIVE_CLUSTER_SIZE = 0.1

    def __init__(self, min_len_log_2, max_len_log_2, rel_cluster_size = DEFAULT_RELATIVE_CLUSTER_SIZE):

        self.__testLength = []

        for i in xrange(min_len_log_2, max_len_log_2 + 1):
            t = 1 << i
            self.__testLength.append(t)

        self.__results = []

        self.__relativeClusterSize = rel_cluster_size

    @staticmethod
    def unorder_range(range_size, output_len):

        init_list = range(0, range_size)

        return [init_list.pop(int((range_size - i) * random.random())) for i in xrange(0, output_len)]

    @staticmethod
    def partly_unorder_list(input_list, unorder_power):

        unorder_len = int(len(input_list) * unorder_power)

        unorder_list = SortingTester.unorder_range(len(input_list), unorder_len)

        shift_list = SortingTester.unorder_range(unorder_len, unorder_len)

        for i in xrange(0, unorder_len):

            shift_list[i] = input_list[unorder_list[shift_list[i]]]

        for i in xrange(0, unorder_len):

            input_list[unorder_list[i]] = shift_list[i]

        return input_list

    @staticmethod
    def cluster_unorder(min_cluster_size, max_cluster_size, list_size):

        output_list = []

        while len(output_list) < list_size:

            start_value = int(random.random() * list_size)
            output_list.extend([start_value + i
                       for i in xrange(0, min_cluster_size + int(random.random() * (max_cluster_size - min_cluster_size)))])

        return output_list[0:list_size]

    @staticmethod
    def create_list_to_sort(list_size, rel_cluster_size):

        class NullValue:
            __repr__ = lambda self: "NULL"

        return [
            (1.0, 'ordered', range(0, list_size)),
            (0.8, 'unordered_0.2', SortingTester.partly_unorder_list(range(0, list_size), 0.2)),
            (0.6, 'unordered_0.4', SortingTester.partly_unorder_list(range(0, list_size), 0.4)),
            (0.4, 'unordered_0.6', SortingTester.partly_unorder_list(range(0, list_size), 0.6)),
            (0.2, 'unordered_0.8', SortingTester.partly_unorder_list(range(0, list_size), 0.8)),
            (0.0, 'unordered', SortingTester.unorder_range(list_size, list_size)),
            (-0.2, 'invert_unordered_0.8', SortingTester.partly_unorder_list(range(list_size - 1, -1, -1), 0.8)),
            (-0.4, 'invert_unordered_0.6', SortingTester.partly_unorder_list(range(list_size - 1, -1, -1), 0.6)),
            (-0.6, 'invert_unordered_0.4', SortingTester.partly_unorder_list(range(list_size - 1, -1, -1), 0.4)),
            (-0.8, 'invert_unordered_0.2', SortingTester.partly_unorder_list(range(list_size - 1, -1, -1), 0.2)),
            (-1.0, 'inverted', range(list_size - 1, -1, -1)),
            (NullValue(), 'cluster_unordered', SortingTester.cluster_unorder(1, max(1, int(list_size * rel_cluster_size)), list_size))
        ]

    @staticmethod
    def check_sequence(input_list, sort_name):

        for i in xrange(0, len(input_list) - 1):

            if input_list[i] > input_list[i + 1]:
                raise SortingTester.WrongOrderError(sort_name)

    def run(self, sorting_list):

        self.__results = []

        for test_length in self.__testLength:

            test_list = SortingTester.create_list_to_sort(test_length, self.__relativeClusterSize)

            for order_degree, case_name, cur_test_list in test_list:

                for sort in sorting_list:
                    list_to_sort = list(cur_test_list)
                    t = time.time()
                    sort(list_to_sort)
                    t = time.time() - t

                    SortingTester.check_sequence(list_to_sort, sort.__name__)

                    self.__results.append(
                        SortingTester.RESULT_DESCRIPTOR(len(cur_test_list), order_degree, case_name, sort.__name__, t))

    def print_results(self):

        cur_size = -1
        case_name = ''
        case_results = []

        self.__results.append(SortingTester.RESULT_DESCRIPTOR(0, '', '', 0.0))

        for result in self.__results:

            if case_name != result.case_name:

                case_results.sort(key=lambda r: r.time)

                if case_name != '':
                    print '\n%20s:' % case_name

                for r in case_results:
                    print "          %20s, time %f" % (r.sort_name, r.time)

                case_results = []

                case_name = result.case_name

            if cur_size != result.arr_len and result.arr_len != 0:
                cur_size = result.arr_len
                print("______________________size = %6d______________________" % cur_size)

            case_results.append(result)

    def csv_to_file(self, path):

        with open(path, "w") as f:

                f.writelines(("".join([str(list(result)).strip("[]"), "\n"]) for result in self.__results))

    def write_to_db(self, db_path):

        conn = pyodbc.connect(
            "Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s" % db_path)

        cursor = conn.cursor()
        cursor.execute("DELETE FROM sorting_result")

        for insert_sql in ("INSERT INTO sorting_result (array_size, order_degree, case_name, sort_name, compute_time)" \
                           " VALUES (%s);" % str(list(result)).strip("[]") for result in self.__results):
            cursor.execute(insert_sql)

        conn.commit()

        cursor.close()
        conn.close()



