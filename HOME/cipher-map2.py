def recall_password(cipher_grille, ciphered_password):
    result = ""
    for flip in range(0, 4, 1):
        for row_index in range(0, len(ciphered_password), 1):
            for col_index in range(0, len(ciphered_password[row_index]), 1):
                if flip == 0:
                    if cipher_grille[row_index][col_index] == "X":
                        result += ciphered_password[row_index][col_index]
                elif flip == 1:
                    if cipher_grille[3 - col_index][row_index] == "X":
                        result += ciphered_password[row_index][col_index]
                elif flip == 2:
                    if cipher_grille[3 - row_index][3 - col_index] == "X":
                        result += ciphered_password[row_index][col_index]
                elif flip == 3:
                    if cipher_grille[col_index][3 - row_index] == "X":
                        result += ciphered_password[row_index][col_index]
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
