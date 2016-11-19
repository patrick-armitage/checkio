def find_message(text):
    """Find a secret message"""

    secret_msg = ""
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in text:
        if c in caps:
            secret_msg += c
    return secret_msg

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
