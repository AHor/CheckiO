def checkio(data):

    #replace this for solution
    if len(data) < 10:
        return False
    number = False
    up_letter = False
    lower_letter = False
    for letter in data:
        if number and up_letter and lower_letter:
            return True
        if letter.isnumeric() and not number:
            number = True
            continue
        if letter.islower() and not lower_letter:
            lower_letter = True
            continue
        if letter.isupper() and not up_letter:
            up_letter = True
            continue
    if number and up_letter and lower_letter:
        return True
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
