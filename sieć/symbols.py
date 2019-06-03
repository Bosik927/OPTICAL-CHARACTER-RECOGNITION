def lowercase_a():
    return "a"


def lowercase_b():
    return "b"


def lowercase_c():
    return "c"


def lowercase_d():
    return "d"


def lowercase_e():
    return "e"


def lowercase_f():
    return "f"


def lowercase_g():
    return "g"


def lowercase_h():
    return "h"


def lowercase_i():
    return "i"


def lowercase_j():
    return "j"


def lowercase_k():
    return "k"


def lowercase_l():
    return "l"


def lowercase_m():
    return "m"


def lowercase_n():
    return "n"


def lowercase_o():
    return "o"


def lowercase_p():
    return "p"


def lowercase_q():
    return "q"


def lowercase_r():
    return "r"


def lowercase_s():
    return "s"


def lowercase_t():
    return "t"


def lowercase_u():
    return "u"


def lowercase_v():
    return "v"


def lowercase_w():
    return "w"


def lowercase_x():
    return "x"


def lowercase_y():
    return "y"


def lowercase_z():
    return "z"


def uppercase_a():
    return "A"


def uppercase_b():
    return "B"


def uppercase_c():
    return "C"


def uppercase_d():
    return "D"


def uppercase_e():
    return "E"


def uppercase_f():
    return "F"


def uppercase_g():
    return "G"


def uppercase_h():
    return "H"


def uppercase_i():
    return "I"


def uppercase_j():
    return "J"


def uppercase_k():
    return "K"


def uppercase_l():
    return "L"


def uppercase_m():
    return "M"


def uppercase_n():
    return "N"


def uppercase_o():
    return "O"


def uppercase_p():
    return "P"


def uppercase_q():
    return "Q"


def uppercase_r():
    return "R"


def uppercase_s():
    return "S"


def uppercase_t():
    return "T"


def uppercase_u():
    return "U"


def uppercase_v():
    return "V"


def uppercase_w():
    return "W"


def uppercase_x():
    return "X"


def uppercase_y():
    return "Y"


def uppercase_z():
    return "Z"


def number_0():
    return "0"


def number_1():
    return "1"


def number_2():
    return "2"


def number_3():
    return "3"


def number_4():
    return "4"


def number_5():
    return "5"


def number_6():
    return "6"


def number_7():
    return "7"


def number_8():
    return "8"


def number_9():
    return "9"


def full_stop():
    return "."


def comma():
    return ","


def question_mark():
    return "?"


def exclamation_mark():
    return "!"


# =================================================================================
def plus_sign():
    return "+"


def equal_sign():
    return "="


def dash():
    return "-"


def underscore():
    return "_"


def round_bracket_close():
    return ")"


def round_bracket_open():
    return "("


def asterisk():
    return "*"


def ampersand():
    return "&"


def caret():
    return "^"


def percent():
    return "%"


def dollar():
    return "$"


def hash_sign():
    return "#"


def at_sign():
    return "@"


def backslash():
    return "\\"


def vertical_bar():
    return "|"


def square_bracket_close():
    return "]"


def square_bracket_open():
    return "["


def curly_bracket_close():
    return "}"


def curly_bracket_open():
    return "{"


def quotation_mark():
    return "'"


def semicolon():
    return ";"


def colon():
    return ":"


def guillemet_end():
    return ">"


def guillemet_start():
    return "<"


def ten_znaczek_na_tyldzie():
    return "`"


def tilde():
    return "~"


def slash():
    return "/"


def select_symbol(n):
    switcher = {
        0: lowercase_a(),
        1: lowercase_b(),
        2: lowercase_c(),
        3: lowercase_d(),
        4: lowercase_e(),
        5: lowercase_f(),
        6: lowercase_g(),
        7: lowercase_h(),
        8: lowercase_i(),
        9: lowercase_j(),
        10: lowercase_k(),
        11: lowercase_l(),
        12: lowercase_m(),
        13: lowercase_n(),
        14: lowercase_o(),
        15: lowercase_p(),
        16: lowercase_q(),
        17: lowercase_r(),
        18: lowercase_s(),
        19: lowercase_t(),
        20: lowercase_u(),
        21: lowercase_v(),
        22: lowercase_w(),
        23: lowercase_x(),
        24: lowercase_y(),
        25: lowercase_z(),
        26: uppercase_a(),
        27: uppercase_b(),
        28: uppercase_c(),
        29: uppercase_d(),
        30: uppercase_e(),
        31: uppercase_f(),
        32: uppercase_g(),
        33: uppercase_h(),
        34: uppercase_i(),
        35: uppercase_j(),
        36: uppercase_k(),
        37: uppercase_l(),
        38: uppercase_m(),
        39: uppercase_n(),
        40: uppercase_o(),
        41: uppercase_p(),
        42: uppercase_q(),
        43: uppercase_r(),
        44: uppercase_s(),
        45: uppercase_t(),
        46: uppercase_u(),
        47: uppercase_v(),
        48: uppercase_w(),
        49: uppercase_x(),
        50: uppercase_y(),
        51: uppercase_z(),
        52: number_0(),
        53: number_1(),
        54: number_2(),
        55: number_3(),
        56: number_4(),
        57: number_5(),
        58: number_6(),
        59: number_7(),
        60: number_8(),
        61: number_9(),
        62: full_stop(),
        63: comma(),
        64: question_mark(),
        65: exclamation_mark(),
        66: plus_sign(),
        67: equal_sign(),
        68: dash(),
        69: underscore(),
        70: round_bracket_close(),
        71: round_bracket_open(),
        72: asterisk(),
        73: ampersand(),
        74: caret(),
        75: percent(),
        76: dollar(),
        77: hash_sign(),
        78: at_sign(),
        79: backslash(),
        80: vertical_bar(),
        81: square_bracket_close(),
        82: square_bracket_open(),
        83: curly_bracket_close(),
        84: curly_bracket_open(),
        85: quotation_mark(),
        86: semicolon(),
        87: colon(),
        88: guillemet_end(),
        89: guillemet_end(),
        90: ten_znaczek_na_tyldzie(),
        91: tilde(),
        92: slash()
    }
    func = switcher.get(n, lambda: "Invalid number")
    return func()

# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 01234567890
# .,?!+=-_)(*&^%$#@\|][}{';:><`~/

