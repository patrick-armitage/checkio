def numeral_values():
    numerals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    values = {}

    for i, n in enumerate(numerals):
        values[n] = i

    return values

def checkio(str_number, radix):
    numerals = numeral_values()
    number = 0
    radix_multiplier = 1
    for i in range((len(str_number) - 1)):
        radix_multiplier *= radix

    for s in str_number:
        v = numerals[s]
        if v >= radix:
            return -1

        number += (v * radix_multiplier)
        radix_multiplier /= radix

    return number
