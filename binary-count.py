def find_lowest_multiple(number):
    multiple = 2

    while number > multiple:
        multiple *= 2

    return multiple

def checkio(number):
    num_unities = 0
    multiple = find_lowest_multiple(number)

    while number > 0:
        # use 2 as the base case for simplicity
        if number <= 2:
            num_unities += 1
            break
        elif multiple <= number <= (multiple*2):
            num_unities += 1
            number -= multiple
        multiple /= 2

    return num_unities

#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio(4) == 1
#     assert checkio(15) == 4
#     assert checkio(1) == 1
#     assert checkio(1022) == 9

# print(checkio(1), 1)
# print(checkio(4), 1)
# print(checkio(15), 4)
# print(checkio(1), 1)
# print(checkio(1022), 9)
