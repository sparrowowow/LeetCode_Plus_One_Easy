

digits = [4, 9, 9, 9]
digits2 = [1, 2, 3]
digits3 = [4,3,2,1]
digits4 = [9]

def plus_one(array):
    output = [str(digit) for digit in array]
    string_value = "".join(output)
    number = int(string_value)
    number += 1
    print(number)

plus_one(digits)
plus_one(digits2)
plus_one(digits3)
plus_one(digits4)