# mutable - dict, set, list
# immutable - float, bool, int, str, tuple
# container - dict, set, list, tuple
# iterable - dict, set, list, tuple, str

#
# a = [2, 3, 4, 2]
# print(hex(id(a)))
# a.append(2)
# print(hex(id(a)))

# id (manzil)
# content (malumot)
# type (turi)

# reduce
# map, filter, zip, enumerate
# https://www.programiz.com/python-programming/recursion
# https://www.programiz.com/python-programming/methods/built-in/map
# https://www.programiz.com/python-programming/methods/built-in/filter
# https://www.programiz.com/python-programming/methods/built-in/sorted
# https://www.programiz.com/python-programming/methods/built-in/zip
# https://www.programiz.com/python-programming/methods/built-in/reversed
# https://www.programiz.com/python-programming/methods/built-in/chr
# https://www.programiz.com/python-programming/methods/built-in/ord
# https://www.programiz.com/python-programming/methods/built-in/all
# https://www.programiz.com/python-programming/methods/built-in/any
# https://www.programiz.com/python-programming/methods/built-in/input
#
# https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce
# https://book.pythontips.com/en/latest/map_filter.html
# https://www.educative.io/answers/how-to-use-the-reduce-method-in-python
# https://www.edureka.co/blog/function-map-filter-reduce/

# '''
# int summa(int a, int b){
#
# }
#
# def summa(a, b):
#     pass
#
# '''
#
# a = [2, 3, 4, 4, 5]
#
# for i in a:
#     print(i, end=' ')
#
#
# if len(a):
#     print('print')
#
# snake_case

# argument, parametr(params)
# position based, keyword based

#
# def summa(a, b, c, d, e=3):
#     pass
#     print()
#
#
# s = summa(b=2, c=6, a=4, d=5)
# print(s)
# a = [2, 3, 4]
# for i in a:
#     pass


# 4 ta funksiya
# 1- n(int) *20 + 5 - 30
# 2- l(list) elementlari yigindisi
# 3- 4ta son (2ta float, va 2ta int),
# 2ta float *  va unga qoshish 2ta int ni ayirmasi
# 4- t(tuple) list qaytarish kk

# for i in [2, 3, 4]:
#     pass
#
#
# # PEP8
#
# def first(l):
#     return l * 20 + 5 - 30
#
#
# def second(l):
#     return sum(l)
#
#
# def third(v1, v2, m1, m2):
#     return v1 * v2 + m1 - m2
#
#
# def fourth(t):
#     return list(t)
#
#
# print(first(3))
# print(second([2, 3, 4, 5]))
# print(third(2.3, 5.6, 2, 3))
# print(fourth((2, 3, 4, 5)))


#
#
# def print_square(l):
#     for i in l:
#         print(i * i, end=' ')
#
# a = [2, 3, 4, 5, 6]
# b = [1, 2, 3]
# c = [1, 2, 3]
# d = [1, 2, 3]
#
# print_square(a)
# print_square(b)
# print_square(c)
# print_square(d)

# a = [2, 3, 4, 5, 6]
# for i in a:
#     print(i * i, end=' ')
#
# b = [1, 2, 3]
# for i in b:
#     print(i * i, end=' ')
#
# c = [1, 2, 3]
# for i in c:
#     print(i * i, end=' ')
#
# d = [1, 2, 3]
# for i in d:
#     print(i * i, end=' ')
# packing, unpacking
#
# a = [2, 3, 4, 5]
# for i in zip(*enumerate(a)):
#     print(*i)

# print(list(enumerate(a)))
# for i, v in enumerate(a):
#     print(i, end=' ')
# print()
# for i, v in enumerate(a, 10):
#     print(v, end=' ')

# slicing, slice


# reduce
# map, filter, zip, enumerate, range - hammasi iterable (iterator, iteration)
# from functools import reduce

# from math import gcd (EKUB), lcm(EKUK)

# a = [1, 2, 3, 4]
# a = [3, 3, 4]
# a = [6, 4]
# a = [10]

# gcd()
# lcm()
# def add(n, m):
#     return n * m


# shortcut


# result = reduce(add, a)
# print(result)

# a = [5, 1, 3, 2, 4, 6, 7, 8]
#
# def square(n):
#     return n * n
#
# print(*map(square, a))
#
#
# print(tuple(map(square, a)))
# for i in map(square, a):
#     print(i, end=' ')

# for i in enumerate(a):
#     print(i)


# a = [5, 1, 3, 2, 4, 6, 7, 8]
#
#
# def is_odd(n):
#     return n & 1  # n % 2 == 1
#
#
# for i in filter(is_odd, a):
#     print(i, end=' ')

# result = list(filter(is_odd, a))
# print(result)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in zip(*matrix):
    print(i)
# print()
# for i in zip([1, 2, 3], [4, 5, 6], [7, 8, 9]):
#     print(i)

# a = [1, 2, 3, 4, 5]
# for i in a[::2]:
#     print(i, end=' ')
# print()
# for i in range(1, 6, 2):
#     print(i, end=' ')
#
#
# def f(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return f(n // 2)
#     else:
#         return f(n // 2) + f(n // 2 + 1)
#
# print(f(5))


# 1, 1, 2, 3, 5, 8, 13, 21 ...
#
# def fib(n):
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(6))
