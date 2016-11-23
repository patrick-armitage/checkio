def check_snakeeyes_palindrome(text):
    palindrome = ''
    palindromes = []
    length = len(text)
    text = list(text)

    for i, ch in enumerate(text):
        if (i+1) < length:
            j = i
            k = i + 1
            while (j >= 0) and (k < length) and text[j] == text[k]:
                palindrome = text[j] + palindrome + text[k]
                j -= 1
                k += 1
        if len(palindrome) > 0:
            palindromes.append(palindrome)
        palindrome = ''

    return palindromes

def check_symmetrical_palindrome(text):
    palindrome = ''
    palindromes = []
    length = len(text)
    text = list(text)

    for i, ch in enumerate(text):
        palindrome = text[i]
        if (i - 1 >= 0) and (i + 1 < length):
            j = i - 1
            k = i + 1
            if text[j] == text[k]:
                while (j >= 0) and (k < length) and (text[j] == text[k]):
                    palindrome = text[j] + palindrome + text[k]
                    j -= 1
                    k += 1
        if len(palindrome) > 0:
            palindromes.append(palindrome)
        palindrome = ''

    return palindromes

def find_longest_palindrome(palindromes):
    palindrome = ''
    length = 0

    for p in palindromes:
        if len(p) > length:
            length = len(p)
            palindrome = p

    return palindrome

def longest_palindromic(text):
    palindromes = check_snakeeyes_palindrome(text)
    palindromes += check_symmetrical_palindrome(text)

    return find_longest_palindrome(palindromes)

# if __name__ == '__main__':
#     assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
#     assert longest_palindromic("abacada") == "aba", "The First"
#     assert longest_palindromic("aaaa") == "aaaa", "The A"

print(longest_palindromic("artrartrt"), "rtrartr")
print(longest_palindromic("abacada"), "aba")
print(longest_palindromic("aaaa"), "aaaa")
