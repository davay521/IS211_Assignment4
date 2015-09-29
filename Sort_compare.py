#David Vayman
#Sort_compare.py
#IS211_ASSIGNMENT4
import random
import time


def insertion_sort(a_list):
    """from book :
    def insertion_sort(a_list):
    for index in range(1, len(a_list)):
    current_value = a_list[index]
    position = index
    while position > 0 and a_list[position - 1] > current_value:
    a_list[position] = a_list[position - 1]
    position = position - 1
    a_list[position] = current_value
    """

    timstarts = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    timends = time.time()
    timetaken = timends - timstarts

    return timetaken


def shell_sort(a_list):
    """ from book:
    def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
    for start_position in range(sublist_count):
    gap_insertion_sort(a_list, start_position, sublist_count)
    sublist_count = sublist_count // 2
    """

    timstarts = time.time()

    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    timends = time.time()
    timetaken = timends - timstarts

    return timetaken


def gap_insertion_sort(a_list, start, gap):
    """ from:
    def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
    current_value = a_list[i]
    position = i
    while position >= gap and a_list[position - gap] >
    current_value:
    a_list[position] = a_list[position - gap]
    position = position - gap
    a_list[position] = current_value
    """

    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    """ python wrapper that calls sort from a_list"""

    timstarts = time.time()
    a_list.sort()
    timends = time.time()

    timetaken = timends - timstarts

    return timetaken


def main():
    """ calling functons similar to sort and compare"""

    inserti500 = 0
    inserti1000 = 0
    inserti10000 = 0

    shellti500 = 0
    shellti1000 = 0
    shellti10000 = 0

    pythonti500 = 0
    pythonti1000 = 0
    pythonti10000 = 0

    container500 = 0
    container1000 = 0
    container10000 = 0

    for i in xrange(100):
        container500 = [int(100 * random.random())
                        for i in xrange(500)]
        container1000 = [int(100 * random.random())
                         for i in xrange(1000)]
        container10000 = [int(100 * random.random())
                          for i in xrange(10000)]

        """ 500, 1000, 10000 search outputs """
        ins500 = insertion_sort(container500)
        inserti500 = inserti500 + ins500

        ins1000 = insertion_sort(container1000)
        inserti1000 = inserti1000 + ins1000

        ins10000 = insertion_sort(container10000)
        inserti10000 = inserti10000 + ins10000

        shell500 = shell_sort(container500)
        shellti500 = shellti500 + shell500

        shell1000 = shell_sort(container1000)
        shellti1000 = shellti1000 + shell1000

        shell10000 = shell_sort(container10000)
        shellti10000 = shellti10000 + shell10000

        pyth500 = python_sort(container500)
        pythonti500 = pythonti500 + pyth500

        pyth1000 = python_sort(container1000)
        pythonti1000 = pythonti1000 + pyth1000

        pyth10000 = python_sort(container10000)
        pythonti10000 = pythonti1000 + pyth10000

        """taking average"""

        insertion500_average = inserti500 / 100
        insertion1000_average = inserti1000 / 100
        insertion10000_average = inserti10000 / 100

        shell500_average = shellti500 / 100
        shell1000_average = shellti1000 / 100
        shell10000_average = shellti10000 / 100

        pythsort500_average = pythonti500 / 100
        pythsort1000_average = pythonti1000 / 100
        pythsort10000_average = pythonti10000 / 100

    """following format = Sequential Search took %10.7f seconds, on average"""
    print "Insertion sort took %10.7f seconds, on average, to run over a list of 500 items" % insertion500_average
    print "Insertion sort took %10.7f seconds, on average, to run over a list of 1000 items" % insertion1000_average
    print "Insertion sort took %10.7f seconds, on average, to run over a list of 10000 items" % insertion10000_average
    print
    print "Shell sort took %10.7f seconds, on average, to run over a list of 500 items" % shell500_average
    print "Shell sort took %10.7f seconds, on average, to run over a list of 1000 items" % shell1000_average
    print "Shell sort took %10.7f seconds, on average, to run over a list of 10000 items" % shell10000_average
    print
    print "Python sort took %10.7f seconds, on average, to run over a list of 500 items" % pythsort500_average
    print "Python sort took %10.7f seconds, on average, to run over a list of 1000 items" % pythsort1000_average
    print "Python sort took %10.7f seconds, on average, to run over a list of 10000 items" % pythsort10000_average

if __name__ == "__main__":
    main()
