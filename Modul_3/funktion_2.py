import math
from parse import *



# def max3 (a, b, c):
#     if a >= b and a >= c:
#         return a
#     if b > a and b > c:
#         return b
#     if c > a and c > b:
#         return c

# or

# def max3 (a, b, c):
#     return max(a, b, c)
#
# assert max3(1, 2, 3) == 3
# assert max3(-1, -2, 10) == 10
# assert max3(1, 1, 1) == 1
# assert max3(1.0, 1.1, 1.2) == 1.2

# def reverse_string(s):
#     return s[::-1]
#
# reverse_string('abcdf')


# def is_palindrome(s):
#     if s[::] == s[::-1]:
#         return True
#     else:
#         return False
#
# assert is_palindrome('') == True
# assert is_palindrome('a') == True
# assert is_palindrome('aba') == True
# assert is_palindrome('abba') == True
# assert is_palindrome('abab') == False
# assert is_palindrome('abbaa') == False
# assert is_palindrome('asdf') == False



# def uniques(xs):
#     a = []
#     a.append(xs[0])
#     for i in xs:
#         if i not in a:
#             a.append(i)
#
#     return print(a)


# uniques([1, 4, 1, 2, 3, 4])
# print(parse("It's {}, I love it!", "It's spam, I love it!"))

from parse import compile
p = compile("It's {}, I love it!")
print(p)
# <Parser "It's {}, I love it!">
print(p.parse("It's spam, I love it!"))

def check_number_in_range(
        number, minimum, maximum):
    if number >= minimum and number <= maximum:
        return True
    else:
        return False





assert check_number_in_range(1, 0, 10) == True
assert check_number_in_range(1, 2, 10) == False
assert check_number_in_range(1, 1, 10) == True
assert check_number_in_range(1, 0, 1) == True
assert check_number_in_range(0, 0, 1) == True
