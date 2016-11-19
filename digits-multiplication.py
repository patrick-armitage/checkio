def checkio(number):
    str_n = str(number)
    sum = 1
    for n in str_n:
        n = int(n)
        if n == 0:
            next
        else:
            sum *= n

    return sum

#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio(123405) == 120
#     assert checkio(999) == 729
#     assert checkio(1000) == 1
#     assert checkio(1111) == 1

# print(checkio(123405))
# print(checkio(999))
# print(checkio(1000))
# print(checkio(1111))
