# I 1 (unus)
# V 5 (quinque)
# X 10 (decem)
# L 50 (quinquaginta)
# C 100 (centum)
# D 500 (quingenti)
# M 1,000 (mille)
def roman_numerals():
    numerals = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    return numerals

def roman_numeral_amts():
    numeral_amts = list(sorted(roman_numerals().keys()))
    return numeral_amts

def get_previous_numeral(numeral_amt):
    numeral_amts = roman_numeral_amts()
    current_index = numeral_amts.index(numeral_amt)
    if current_index > 0:
        return numeral_amts[current_index-1]
    else:
        return 0

def get_next_numeral(numeral_amt):
    numeral_amts = roman_numeral_amts()
    current_index = numeral_amts.index(numeral_amt)
    if current_index < len(numeral_amts)-1:
        return numeral_amts[current_index+1]
    else:
        return 0

def append_numeral(roman_number, total, numeral_amt, remainder):
    numerals = roman_numerals()
    if total > (numeral_amt - 1):
        for i in range(int(total/numeral_amt)):
            prev_numeral = get_previous_numeral(numeral_amt)
            next_numeral = get_next_numeral(numeral_amt)

            roman_number += numerals[numeral_amt]
            remainder = total % numeral_amt

    return roman_number, remainder

def replace_quad_chars_for_off_ones(numeral_str):
    numerals = roman_numerals()
    str_to_replace, replacement_str = '', ''
    for amt, ch in numerals.items():
        if ch != 'M':
            next_amt = get_next_numeral(amt)
            next_numeral = numerals[next_amt]
            if ch != 'D':
                large_numeral = numerals[get_next_numeral(next_amt)]
                str_to_replace = next_numeral + ch + ch + ch + ch
                replacement_str = ch + large_numeral
                numeral_str = numeral_str.replace(str_to_replace, replacement_str)
            str_to_replace = ch + ch + ch + ch
            replacement_str = ch + next_numeral
            numeral_str = numeral_str.replace(str_to_replace, replacement_str)

    return numeral_str

def checkio(data):
    roman_number = ''
    numerals = reversed(roman_numeral_amts())
    remainder = data

    for numeral in numerals:
        roman_number, remainder = append_numeral(roman_number, remainder, numeral, remainder)

    roman_number = replace_quad_chars_for_off_ones(roman_number)
    return roman_number

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(6) == 'VI', '6'
#     assert checkio(76) == 'LXXVI', '76'
#     assert checkio(499) == 'CDXCIX', '499'
#     assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'

print(checkio(6), 'VI')
print(checkio(76), 'LXXVI')
print(checkio(499), 'CDXCIX')
print(checkio(3888), 'MMMDCCCLXXXVIII')
