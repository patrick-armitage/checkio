def checkio(*args):
    if not args:
        return 0

    first_n = False
    max_n, min_n = 0, 0
    for n in args:
        if not first_n:
            min_n = n
            max_n = n
            first_n = True
        if n > max_n:
            max_n = n
        elif n < min_n:
            min_n = n

    difference = max_n - min_n
    return difference
    # if min_n >= 0:
    #     return "{0}-{1}={2}".format(max_n, min_n, difference)
    # else:
    #     return "{0}-({1})={2}".format(max_n, min_n, difference)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"

# print(checkio(1, 2, 3), "3-1=2")
# print(checkio(5, -5), "5-(-5)=10")
# print(checkio(10.2, -2.2, 0, 1.1, 0.5), "10.2-(-2.2)=12.4")
# print(checkio(), "Empty")
