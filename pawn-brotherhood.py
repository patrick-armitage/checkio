import string

def alpha_chars():
    return list(string.ascii_lowercase)

def get_prev_alpha_char(char):
    chars = alpha_chars()
    curr_index = chars.index(char)
    if char != 'a':
        return chars[curr_index-1]
    else:
        return char

def get_next_alpha_char(char):
    chars = alpha_chars()
    curr_index = chars.index(char)
    if char != 'h':
        return chars[curr_index+1]
    else:
        return char

def check_for_pawn(pawns, pawn):
    if pawn in pawns:
        return True
    else:
        return False

def safe_pawns_exist(pawns, pawn):
    pawn_is_safe = False
    safe_pawn_num = int(pawn[1]) - 1
    if safe_pawn_num > 0:
        safe_pawn_char = get_prev_alpha_char(pawn[0])
        if safe_pawn_char != pawn[0]:
            safe_pawn = safe_pawn_char + str(safe_pawn_num)
            pawn_is_safe =  check_for_pawn(pawns, safe_pawn)
        safe_pawn_char = get_next_alpha_char(pawn[0])
        if not pawn_is_safe and safe_pawn_char != pawn[0]:
            safe_pawn = safe_pawn_char + str(safe_pawn_num)
            pawn_is_safe =  check_for_pawn(pawns, safe_pawn)

    return pawn_is_safe

def safe_pawns(pawns):
    safe_count = 0

    for p in pawns:
        if safe_pawns_exist(pawns, p):
            safe_count += 1

    return safe_count
