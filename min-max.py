import types

def min(*args, **kwargs):
    key = kwargs.get("key", None)

    minimum = None
    args_type = type(list(args)[0])
    if args_type == types.GeneratorType or args_type == filter or args_type == set:
        args = list(list(args)[0])
    elif len(args) == 1:
        if type(args[0]) == str:
            args = list(args[0])
        else:
            args = args[0]

    for a in args:
        if minimum == None:
            minimum = a
        if key:
            curr_arg = key(a)
            if curr_arg < key(minimum):
                minimum = a
        else:
            curr_arg = a
            if curr_arg < minimum:
                minimum = a

    return minimum

def max(*args, **kwargs):
    key = kwargs.get("key", None)

    maximum = None
    args_type = type(list(args)[0])
    if args_type == types.GeneratorType or args_type == filter or args_type == set:
        args = list(list(args)[0])
    elif len(args) == 1:
        if type(args[0]) == str:
            args = list(args[0])
        else:
            args = args[0]

    for a in args:
        if maximum == None:
            maximum = a
        if key:
            curr_arg = key(a)
            if curr_arg > key(maximum):
                maximum = a
        else:
            curr_arg = a
            if curr_arg > maximum:
                maximum = a

    return maximum

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert max(3, 2) == 3, "Simple case max"
#     assert min(3, 2) == 2, "Simple case min"
#     assert max([1, 2, 0, 3, 4]) == 4, "From a list"
#     assert min("hello") == "e", "From string"
#     assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
#     assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

print(max(3, 2), 3, "Simple case max")
print(min(3, 2), 2, "Simple case min")
print(max([1, 2, 0, 3, 4]), 4, "From a list")
print(min("hello"), "e", "From string")
print(max(2.2, 5.6, 5.9, key=int), 5.6, "Two maximal items")
print(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]), [9, 0], "lambda key")
print(min(abs(i) for i in range(-10, 10)), 0)
print(max(filter(str.isalpha, "@v$e56r5CY{]")), 'v')
print(min({1, 2, 3, 4, -10}), -10)
print(min([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum), [1, 2, 3])
