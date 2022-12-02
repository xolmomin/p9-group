# def add(a, b, c=1, d=0): # 4
#     return a + b + c + d
# # keyword, position
# b = add
# result = b(4, 2) # 4, 3, 2, 1, 0
# print(result)

# def add(*args, b, a, name=None, **kwargs):
#     print(b, a)
#     print(args)
#     print(kwargs)
#     print(name)
#
#
# # args - arguments
# # kwargs - keyword arguments
#
# add(1, 2, 'botirjon', b=2, a=2, name='kimdir', t=3, y=2, age=10)

# overloading
#
# def add(b, *args, a):
#     print(b, a)
#     print(args)
#
# add
# from pprint import pprint
#
#
# def add(a, b):
#     return a + b
# a = 2
# def add(a, b, c=1):
#     return a + b + c
#
# pprint(locals())
# print()
# print(add)
# print(add(2, 3))

# snake_case = ''
# n, m, *t = 1, 2, 3, 4, 5
# print(n, m, *t)

# underscore
# l = [2, 3, 4, 5, 6]
# a, b, *_ = l
# print(a, b, _)
# print(_[1])
# print(l[3])
#
# for _ in range(10):
#     print(_)


# # 4 + 3 + 2 + 1
# def recursive(n):
#     if n == 1:
#         return 1
#     return recursive(n - 1) + n
#
# print(recursive(4))
#
# # 1 + 2 + 3 + 4
# def recursive(n, stop):
#     if n == stop:
#         return n
#     return recursive(n + 1, stop) + n
#
#
# print(recursive(1, 4))

'''

recursive(4) = recursive(3) + 4
recursive(3) = recursive(2) + 3
recursive(2) = recursive(1) + 2
recursive(1) = 1


recursive(4) = 1 + 2 + 3 + 4

'''
#
# def power_n(x, n):
#     if n == 0:
#         return 1
#     if n > 0:
#         if n % 2 == 0:
#             return power_n(x, n // 2) ** 2
#         else:
#             return power_n(x, n - 1) * x
#     else:
#         return power_n(1 / x, -n)
#
#
# def power_n(x, n):
#     if n == 0:
#         return 1
#     if n > 0:
#         if n & 1:
#             return power_n(x, n - 1) * x
#         return power_n(x, n // 2) ** 2
#     return power_n(1 / x, -n)
# 8!! = 8 * 6 * 4 * 2
# 7!! = 7 * 5 * 3 * 1

# bin_pow (binary power)
import time

#
# def bin_pow(a, n):
#     if n < 1:
#         return 1
#     if n % 2 == 0:
#         return bin_pow(a, n // 2) ** 2
#     else:
#         return bin_pow(a, (n - 1) // 2) ** 2 * a
#

# (n-1)// 2
# n//2
#
# def bin_pow(a, n):
#     if n < 1:
#         return 1
#     # return bin_pow(a, n // 2) ** 2 * (a if n & 1 else 1)
#     return bin_pow(a, n // 2) ** 2 * (1, a)[not n & 1]
#
#
# start = time.time()
# print(bin_pow(6, 237))
# # print(6 ** 2373)
# end = time.time()
# print((end - start) * 1000)  # 1.6927719116210938e-05
# 12 * 2 ** 28 + 25 * 2 ** 28

'''
eski qolaki variant     0.11
0.11181831359863281
0.12421607971191406
0.10776519775390625
0.1239776611328125

yangi variant           0.02
0.02002716064453125
0.0209808349609375
0.02002716064453125
0.015735626220703125
0.019311904907226562

'''


#
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# decorator
# from functools import lru_cache
#
# @lru_cache
# def fib(n):
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(500))
# from math import gcd
#
# print(gcd(15, 18))
#
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
#
# print(gcd(15, 18))
#



def sum_digit(n):
    pass


n = 325

# map, filter, zip, range, enumerate
# lambda , function


