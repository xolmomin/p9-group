# # import builtins
# # from pprint import pprint
#
# # s = {'hello', '123', 123, 'world'}
# # print(s.pop())
#
# # print(s)
# # {'world', 'hello', 123, '123'}
# # {'hello', '123', 123, 'world'}
# '''
# hello
# {123, 'world', '123'}
#
# 123
# {'hello', 'world', '123'}
# '''
# # pprint(dir(list))
#
# # all, any
#
# # l = {False, 0, 0.0, .0, 0., '', (2,3,4)}
# # print(any(l))
#
# # a = '2^4'
# #
# # print(eval(a))
# # print(a)
#
# # print(ord('A'))
# # print(chr(65))
# # l = [False, -1, [], 0, False]
# # print(any(l))
# # immutable, mutable, hashable, unhashable, all methods + built-in
#
# # matrix = [
# #     [12, 22, 24, 22, 14],
# #     [20, 20, 18, 23, 14],
# #     [10, 17, 18, 10, 13],
# #     [25, 14, 21, 14, 10],
# #     [18, 21, 24, 14, 12]
# # ]
# #
# # for i in range(len(matrix)):
# #     for j in range(len(matrix[0])):
# #         print(matrix[i][j], end=' ')
# #
# # # 4x6
# # # nxm
# #
# # from random import randint
# #
# # n = 5
# # matrix = [[randint(10, 25) for _ in range(n)] for _ in range(n)]
# # print(matrix)
# 100- misol
#
# a = [2, 3, 4, 5]
#
# a[2] = 8
# print(a)
#
# 6
# 51 49 9 76 56 78
# 3 4


# from math import cos, sqrt, sin
# from decimal import Decimal, getcontext, ROUND_HALF_UP
#
# getcontext().rounding = ROUND_HALF_UP
#
# x, y, c, d = map(int, input().split())
#
# S = Decimal(0)
# for i in range(1, x + 1):
#     S += Decimal(sqrt(c * i + d))
#
# P = Decimal(1)
# for k in range(1, y + 1):
#     P *= Decimal((sin(c + d) + 3 * c) / (cos(c * k) + 2.78 * d))
#
# SP = Decimal(0)
# for i in range(1, c + 1):
#     PS = Decimal(1)
#     for k in range(1, d + 1):
#         PS *= Decimal((c * x ** k + i * k) / (d * i + c * k))
#     SP += PS
#
# print(f'{S:.2f} {P:.2f} {SP:.2f}')


# s = 0
# n = 3
# for i in range(1, n + 1):
#     s += (x + 1) ** (1 / i)
#
# # https://algo.ubtuit.uz/problem/221
#
# def fun(n):
#     return abs(n), n
#
# input()
# a = list(map(int, input().split()))
# a.sort(key=fun)
# print(*a)


'''

9, -9
2, 3 -4, 8, 9, -9

'''

# 2 3 -4 8 -9 9


# ls = list(map(int, input().split()))
# ls.sort(key=fun)
#
# print(ls)

# anonymous function

# def add(a, b):
#     return a + b

# add = lambda a, b: a + b
# print(add(2, 6))
#
# print((lambda *args: sum(args))(2, 3, 4, 4))
# *args = 2, 3, 4, 4
# a = 2,3,4,5

# a = add
# print(a(2, 6))
# print(add(2, 6))
# print(add(3, 8))

# 1-101
# from math import sqrt

# s = filter(lambda n: sqrt(n) - int(sqrt(n)) == 0, list(range(1, 101)))
# print(*s)
# s = filter(lambda n: not sqrt(n) % 1, range(1, 101))
# print(*s)
# Output: [0,1,2,4,5,3]


# nums = [0, 2, 1, 5, 3, 4]
# result = [nums[i] for i in nums]
# print(result)
#       0  1  2  4  5  3
from functools import reduce

'''
[0, 1, 2, 4, 5, 3]

'''

s = [2, 3, 4, 5]

print(reduce(lambda x, y: x * y, s))
