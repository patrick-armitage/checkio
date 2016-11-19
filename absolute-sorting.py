def checkio(numbers_array):
    numbers_array = list(numbers_array)
    sorted_array = []
    for n in numbers_array:
        if sorted_array == []:
            sorted_array.append(n)
        else:
            for i, c in enumerate(sorted_array):
                if abs(n) <= abs(c):
                    sorted_array.insert(i, n)
                    break
                elif (i+1) == len(sorted_array):
                    sorted_array.append(n)
                    break

    return sorted_array

#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     def check_it(array):
#         if not isinstance(array, (list, tuple)):
#             raise TypeError("The result should be a list or tuple.")
#         return list(array)
#
#     assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
#     assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
#     assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"

# print(checkio((-20, -5, 10, 15)), [-5, 10, 15, -20])
# print(checkio((1, 2, 3, 0)), [0, 1, 2, 3])
# print(checkio((-1, -2, -3, 0)), [0, -1, -2, -3])
