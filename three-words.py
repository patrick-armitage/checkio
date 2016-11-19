def is_word(word):
    result = True
    non_word_chars = "0123456789"
    for c in word:
        if c in non_word_chars:
            result = False
    return result

def checkio(words):
    result = False
    num_consecutive_words = 0
    words_arr = words.split()
    for w in words_arr:
        if is_word(w):
            num_consecutive_words += 1
        else:
            num_consecutive_words = 0

        if num_consecutive_words == 3:
            result = True
            break

    return result

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
