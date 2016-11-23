def horizontal_match(matrix):
    length = len(matrix)

    match_found = False
    matches_found = 0
    for row in matrix:
        i = 1
        curr_num = row[0]
        while i < length:
            if curr_num == row[i]:
                matches_found += 1
                if matches_found == 3:
                    match_found = True
            else:
                if matches_found > 0:
                    matches_found = 0
            curr_num = row[i]
            i += 1

    return match_found

def vertical_match(mtrx):
    length = len(mtrx)
    match_found = False

    for y in range(length):
        for x in range(length):
            # check upward
            if (y-3) >= 0:
                if mtrx[y][x] == mtrx[y-1][x] == mtrx[y-2][x] == mtrx[y-3][x]:
                    match_found = True
            # check downward
            if (y+3) < length:
                if mtrx[y][x] == mtrx[y+1][x] == mtrx[y+2][x] == mtrx[y+3][x]:
                    match_found = True

    return match_found

def diagonal_match(mtrx):
    length = len(mtrx)
    match_found = False

    for y in range(length):
        for x in range(length):
            # check upper-left
            if (x-3) >= 0 and (y-3) >= 0:
                if mtrx[y][x] == mtrx[y-1][x-1] == mtrx[y-2][x-2] == mtrx[y-3][x-3]:
                    match_found = True
            # check upper-right
            if (x+3) < length and (y-3) >= 0:
                if mtrx[y][x] == mtrx[y-1][x+1] == mtrx[y-2][x+2] == mtrx[y-3][x+3]:
                    match_found = True
            # check lower-left
            if (x-3) >= 0 and (y+3) < length:
                if mtrx[y][x] == mtrx[y+1][x-1] == mtrx[y+2][x-2] == mtrx[y+3][x-3]:
                    match_found = True
            # check lower-right
            if (x+3) < length and (y+3) < length:
                if mtrx[y][x] == mtrx[y+1][x+1] == mtrx[y+2][x+2] == mtrx[y+3][x+3]:
                    match_found = True

    return match_found

def checkio(matrix):
    match = False
    if horizontal_match(matrix) or vertical_match(matrix) or diagonal_match(matrix):
        match = True
    return match

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio([
#         [1, 2, 1, 1],
#         [1, 1, 4, 1],
#         [1, 3, 1, 6],
#         [1, 7, 2, 5]
#     ]) == True, "Vertical"
#     assert checkio([
#         [7, 1, 4, 1],
#         [1, 2, 5, 2],
#         [3, 4, 1, 3],
#         [1, 1, 8, 1]
#     ]) == False, "Nothing here"
#     assert checkio([
#         [2, 1, 1, 6, 1],
#         [1, 3, 2, 1, 1],
#         [4, 1, 1, 3, 1],
#         [5, 5, 5, 5, 5],
#         [1, 1, 3, 1, 1]
#     ]) == True, "Long Horizontal"
#     assert checkio([
#         [7, 1, 1, 8, 1, 1],
#         [1, 1, 7, 3, 1, 5],
#         [2, 3, 1, 2, 5, 1],
#         [1, 1, 1, 5, 1, 4],
#         [4, 6, 5, 1, 3, 1],
#         [1, 1, 9, 1, 2, 1]
#     ]) == True, "Diagonal"

print(checkio([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]), True)
print(checkio([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
]), False)
print(checkio([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
]), True)
print(checkio([
    [7, 1, 1, 8, 1, 1],
    [1, 1, 7, 3, 1, 5],
    [2, 3, 1, 2, 5, 1],
    [1, 1, 1, 5, 1, 4],
    [4, 6, 5, 1, 3, 1],
    [1, 1, 9, 1, 2, 1]
]), True)
print(checkio([
    [2, 6, 2, 2, 7, 6, 5],
    [3, 4, 8, 7, 7, 3, 6],
    [6, 7, 3, 1, 2, 4, 1],
    [2, 5, 7, 6, 3, 2, 2],
    [3, 4, 3, 2, 7, 5, 6],
    [8, 4, 6, 5, 2, 9, 7],
    [5, 8, 3, 1, 3, 7, 8]
]), False)
print(checkio([
    [1, 9, 7, 8, 9, 3, 6, 5, 6, 2],
    [4, 9, 4, 8, 3, 4, 8, 8, 5, 9],
    [2, 8, 5, 5, 7, 8, 6, 1, 3, 6],
    [6, 4, 7, 6, 9, 1, 4, 5, 7, 8],
    [4, 7, 7, 9, 8, 8, 8, 8, 4, 4],
    [3, 7, 3, 2, 1, 9, 1, 8, 9, 1],
    [4, 7, 2, 4, 8, 1, 2, 3, 6, 2],
    [4, 4, 1, 3, 3, 3, 9, 2, 6, 7],
    [8, 6, 1, 9, 3, 5, 8, 1, 7, 5],
    [7, 3, 6, 5, 3, 6, 6, 4, 8, 2]
]), True)
print(checkio([
    [2, 3, 6, 5, 6, 2, 8, 3, 7, 4],
    [6, 9, 5, 9, 7, 6, 8, 5, 1, 6],
    [6, 8, 2, 6, 1, 9, 3, 6, 6, 4],
    [5, 8, 3, 2, 3, 8, 7, 4, 6, 4],
    [2, 3, 1, 4, 5, 1, 2, 5, 6, 9],
    [5, 4, 8, 7, 5, 5, 8, 4, 9, 5],
    [9, 7, 9, 9, 5, 9, 9, 8, 1, 2],
    [5, 1, 7, 4, 8, 3, 4, 1, 8, 8],
    [5, 3, 3, 2, 6, 1, 4, 3, 8, 8],
    [4, 8, 1, 4, 5, 8, 8, 7, 4, 7]
]),  True)
print(checkio([
    [7, 9, 1, 7, 6, 7, 5, 9, 6],
    [5, 5, 9, 3, 1, 6, 7, 4, 7],
    [1, 7, 5, 2, 3, 1, 6, 4, 7],
    [2, 2, 2, 8, 7, 2, 6, 6, 9],
    [5, 6, 4, 2, 6, 7, 3, 4, 7],
    [5, 5, 6, 4, 9, 4, 3, 1, 7],
    [7, 3, 2, 3, 2, 4, 4, 7, 3],
    [3, 6, 9, 7, 2, 5, 6, 2, 5],
    [4, 1, 3, 9, 4, 2, 4, 8, 4]
]), True)
print(checkio([
    [6, 6, 7, 4, 4, 6, 7, 9, 7, 9],
    [4, 1, 8, 4, 7, 3, 5, 1, 1, 6],
    [6, 1, 8, 8, 9, 3, 7, 6, 8, 9],
    [8, 8, 7, 1, 6, 2, 1, 4, 1, 6],
    [4, 4, 9, 9, 8, 8, 5, 4, 9, 8],
    [5, 8, 1, 6, 8, 7, 1, 2, 9, 7],
    [1, 8, 2, 7, 8, 9, 8, 1, 7, 1],
    [7, 2, 7, 3, 7, 4, 3, 7, 1, 3],
    [7, 3, 8, 7, 5, 2, 8, 9, 2, 2],
    [5, 6, 4, 3, 1, 5, 5, 9, 2, 9]
]),  False)
print(checkio([
    [1, 5, 6, 3, 7, 3, 2],
    [2, 9, 1, 1, 5, 3, 8],
    [3, 3, 3, 1, 1, 8, 9],
    [4, 2, 1, 3, 2, 1, 4],
    [1, 4, 5, 7, 1, 3, 6],
    [4, 5, 8, 6, 1, 1, 2],
    [3, 7, 1, 5, 7, 4, 7]
]), False)
print(checkio([
    [1, 1, 2, 4, 6, 4, 1, 4],
    [3, 3, 4, 9, 9, 1, 9, 9],
    [2, 6, 7, 2, 7, 8, 8, 8],
    [5, 7, 8, 6, 5, 6, 3, 1],
    [7, 7, 4, 4, 1, 7, 8, 1],
    [2, 5, 7, 9, 7, 5, 8, 6],
    [1, 5, 3, 7, 2, 1, 6, 3],
    [1, 1, 3, 7, 7, 4, 9, 7]
]), True)
print(checkio([
    [2, 6, 2, 3, 5, 2, 4, 8, 7],
    [5, 7, 8, 5, 9, 5, 7, 3, 4],
    [6, 4, 1, 2, 1, 6, 5, 8, 5],
    [9, 3, 1, 3, 5, 4, 6, 4, 8],
    [9, 6, 6, 8, 1, 9, 1, 2, 1],
    [5, 5, 5, 8, 6, 5, 3, 2, 5],
    [7, 5, 2, 9, 2, 9, 8, 2, 5],
    [5, 8, 1, 9, 1, 2, 6, 2, 2],
    [7, 5, 3, 6, 1, 6, 9, 5, 9]
]), True)
print(checkio([
    [1, 1, 7, 2, 8, 1, 9, 2, 6, 2],
    [3, 7, 6, 6, 7, 4, 7, 5, 3, 7],
    [2, 4, 8, 5, 3, 9, 4, 9, 4, 4],
    [3, 1, 4, 9, 8, 9, 5, 3, 6, 8],
    [4, 5, 6, 4, 7, 3, 9, 1, 9, 9],
    [7, 7, 6, 4, 8, 9, 2, 3, 5, 7],
    [9, 1, 2, 1, 1, 7, 9, 2, 6, 4],
    [5, 7, 6, 9, 5, 3, 5, 4, 4, 9],
    [5, 4, 7, 8, 9, 3, 1, 4, 5, 1],
    [9, 5, 7, 9, 4, 7, 4, 5, 8, 8]
]), True)
