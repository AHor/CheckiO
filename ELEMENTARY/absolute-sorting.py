def checkio(numbers_array):
    # numbers_array = sorted((abs(num) for num in numbers_array))
    # return sorted(numbers_array, key=abs)
    numbers_array = list(numbers_array)
    result = list()
    n = len(numbers_array)
    j = 0
    while j < n-1:
        f = 0
        i = 0
        while i < n-j-1:
            if abs(numbers_array[i]) > abs(numbers_array[i+1]):
                tmp = numbers_array[i+1]
                numbers_array[i+1] = numbers_array[i]
                numbers_array[i] = tmp
                f = 1
            i += 1
        if f == 0:
            break
        j += 1
    return numbers_array

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)
    
    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
