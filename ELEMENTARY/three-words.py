def checkio(words):
    word_start = 0
    words_cnt = 0
    for index in range(0, len(words)):
        if words[index] == ' ' or index == len(words)-1:
            if str(words[word_start:index]).isalpha():
                words_cnt += 1
                word_start = index + 1
                if words_cnt == 3:
                    return True
            else:
                word_start = index + 1
                words_cnt = 0
        else:
            continue
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
