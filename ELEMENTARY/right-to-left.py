def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    len_right = len("right")
    res_str = ""
    for word in phrases:
        if res_str != "":
            res_str += ","
        index = 0
        while index < len(word):
            if word[index:index+len_right] == "right":
                res_str += "left"
                index += len_right
            else:
                res_str += word[index]
                index += 1
    return res_str

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
