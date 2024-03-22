from domain.numbers import *


def testAdd():
    my_list = []
    add(my_list, 5)
    assert my_list == [5]
    add(my_list, 10)
    assert my_list == [5, 10]
    add(my_list, 11)
    assert my_list == [5, 10, 11]


def testInsert():
    my_list = [1, 2, 3, 4, 5]
    insert(my_list, 1, 20)
    assert my_list == [1, 20, 2, 3, 4, 5]

    try:
        insert(my_list, 10, 8)
        assert False
    except ValueError:
        assert True

    try:
        insert(my_list, 21, 67)
        assert False
    except ValueError:
        assert True


def testRemove():
    my_list = [1, 2, 3, 4, 5]
    remove(my_list, 2)
    assert my_list == [1, 2, 4, 5]

    try:
        remove(my_list, 20)
        assert False
    except ValueError:
        assert True

    try:
        remove(my_list, 13)
        assert False
    except ValueError:
        assert True


def testRemove_interval():
    my_list = [1, 2, 3, 4, 5, 6]
    remove_interval(my_list, 1, 3)
    assert my_list == [1, 5, 6]

    try:
        remove_interval(my_list, 21, 30)
        assert False
    except ValueError:
        assert True

    try:
        remove_interval(my_list, 13, 15)
        assert False
    except ValueError:
        assert True


def testReplace():
    my_list = [1, 2, 3, 4, 5, 6]
    replace(my_list, [2, 3, 4], [21, 33])
    assert my_list == [1, 21, 33, 5, 6]
    replace(my_list, [21, 33], [99])
    assert my_list == [1, 99, 5, 6]
    replace(my_list, [99, 5], [122])
    assert my_list == [1, 122, 6]


def testPrime():
    my_list = [2, 8, 5, 19, 20, 15]
    assert prime(my_list, 1, 4) == [5, 19]
    assert prime(my_list, 0, 5) == [2, 5, 19]
    assert prime(my_list, 3, 5) == [19]


def testOdd():
    my_list = [2, 5, 19, 20, 15]
    assert odd(my_list, 0, 4) == [5, 19, 15]

    try:
        odd(my_list, 21, 30)
        assert False
    except ValueError:
        assert True

    try:
        odd(my_list, 13, 15)
        assert False
    except ValueError:
        assert True


def testSequence_sum():
    my_list = [2, 3, 4, 5, 6, 8]
    assert sequence_sum(my_list, 0, 3) == 14
    assert sequence_sum(my_list, 1, 4) == 18
    assert sequence_sum(my_list, 0, 5) == 28


def testGcd():
    my_list = [4, 8, 66, 54, 10]
    assert gcd(my_list, 1, 3) == 2
    try:
        gcd(my_list, 12, 22)
        assert False
    except ValueError:
        assert True
    try:
        gcd(my_list, 21, 30)
        assert False
    except ValueError:
        assert True


def testSequence_max():
    my_list = [1, 2, 3, 4, 6, 11]
    assert sequence_max(my_list, 0, 5) == 11

    try:
        sequence_max(my_list, 11, 20)
        assert False
    except ValueError:
        assert True

    try:
        sequence_max(my_list, 8, 12)
        assert False
    except ValueError:
        assert True


def testFilter_prime():
    my_list = [2, 5, 7, 12, 16, 17]
    assert filter_prime(my_list) == [2, 5, 7, 17]
    my_list = [1, 2, 3, 4]
    assert filter_prime(my_list) == [2, 3]
    my_list = [2, 3, 5, 7]
    assert filter_prime(my_list) == [2, 3, 5, 7]


def testFilter_negative():
    my_list = [-1, -2, 3, 4, -5]
    assert filter_negative(my_list) == [-1, -2, -5]
    my_list = [1, 2, 3]
    assert filter_negative(my_list) == []
    my_list = [-1, 2, 3, 4]
    assert filter_negative(my_list) == [-1]


def testUndo():
    my_list = [1, 2, 3, 4, 5, 6]
    before_list = [1, 2, 3, 4, 5]
    assert undo(my_list, before_list) == [1, 2, 3, 4, 5]
    my_list = [1, 2, 3, 4, 5, 6]
    before_list = [5]
    assert undo(my_list, before_list) == [5]
    my_list = [1, 2, 3]
    before_list = [1, 2]
    assert undo(my_list, before_list) == [1, 2]


def runAllTests():
    testAdd()
    testInsert()
    testRemove()
    testRemove_interval()
    testReplace()
    testPrime()
    testOdd()
    testSequence_sum()
    testGcd()
    testSequence_max()
    testFilter_prime()
    testFilter_negative()
    testUndo()
