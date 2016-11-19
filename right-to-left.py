def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """

    phrases = list(phrases)
    for i, p in enumerate(phrases):
        phrases[i] = p.replace("right", "left")

    return ','.join(phrases)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"

# print(left_join(("left", "right", "left", "stop")), "left,left,left,stop")
# print(left_join(("bright aright", "ok")), "bleft aleft,ok")
# print(left_join(("brightness wright",)), "bleftness wleft")
# print(left_join(("enough", "jokes")), "enough,jokes")
