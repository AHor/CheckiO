def safe_pawns(pawns):
    result = 0
    ord_a = ord('a')
    for pawn in pawns:
        row = int(pawn[1])
        col = ord(pawn[0]) - ord_a
        if row == 0:
            continue
        if col != 0 and str(chr(col - 1 + ord_a) + str(row - 1)) in pawns:
            result += 1
            continue
        if col != 7 and str(chr(col + 1 + ord_a) + str(row - 1)) in pawns:
            result += 1
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
