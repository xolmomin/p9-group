# from math import sin, cos
#
# a, b, c, d = map(int, input().split())
#
# h = 2
# y = 0
# for x in range(c, d + 1, h):
#     y += ((sin(a * x) + b ** (2 * c)) / (b * b + cos(x) ** 2)) ** (1 / 3) - \
#          sin(x * x) / (a * b)
#
# print(f'{y:.2f}')
#
# from math import sin, cos
# a, b, c, d = map(int, input().split())
#
# y = 0
# x = c
#
# while x <= d:
#     y += ((sin(a * x) + b ** (2 * c)) / (b * b + cos(x) ** 2)) ** (1 / 3) - \
#          sin(x * x) / (a * b)
#     x += 2
#
# print(f'{y:.2f}')
#
#
#
# while i != 10:
#     print(1, end=' ')
#     i += 1
# else:
#     print(i, 'else varianti')

# for index, v in enumerate(a):
#     print(index)
#     if v == 5:
#         break
# else:
#     print('else')
#

#
# # 79 - misol
# from math import pi, cos
#
# a = int(input())
# y = 0
# h = pi / 19
# x = -pi / 2
# while x <= pi:
#     y += (a ** a) ** (1 / 3) + x * x * cos(a * x)
#     x += h
#
# print(f'{y:.2f}')

#
# https://www.programiz.com/python-programming/list
# https://www.programiz.com/python-programming/tuple
# https://www.programiz.com/python-programming/string
# https://www.programiz.com/python-programming/set
# https://www.programiz.com/python-programming/dictionary
#
#
# https://www.programiz.com/python-programming/methods/list
# https://www.programiz.com/python-programming/methods/tuple
# https://www.programiz.com/python-programming/methods/string
# https://www.programiz.com/python-programming/methods/set
# https://www.programiz.com/python-programming/methods/dictionary


# 101 - misol

# n = int(input())
# a = list(map(int, input().split()))
#
# ortacha = sum(a) / len(a)  # 47.3
#
# summa = 0
# count = 0
# for i in a:
#     if i < ortacha:
#         summa += i
#         count += 1
#
# print(f'{summa / count:.2f}')
#
# toq orindagi juft elementlarni chiqarish
# 2 9 3 5 65 21 15
# a = [2, 9, 3, 5, 65, 21, 18]
#
#
# for i, value in enumerate(a):
#     if (i + 1) & 1 and not value & 1:
#         print(value, end=' ')
# print()
#
# for i, value in enumerate(a):
#     if (i + 1) % 2 and not value % 2:
#         print(value, end=' ')
# print()
#
# for i, value in enumerate(a):
#     if (i + 1) % 2 == 1 and value % 2 == 0:
#         print(value, end=' ')
# print()
#
# for i in range(len(a)):
#     if (i + 1) % 2 == 1 and a[i] % 2 == 0:
#         print(a[i], end=' ')
# print()
#
# for i in range(len(a)):
#     if (i + 1) % 2 and not a[i] % 2:
#         print(a[i], end=' ')
# print()
#
# for i in range(len(a)):
#     if (i + 1) & 1 and not a[i] & 1:
#         print(a[i], end=' ')
#

# 2 3 65 15
# a = list(map(int, input().split()))
# for index, value in enumerate(a):
#     if (index + 1) % 2 == 1:
#         print(value, end=' ')
#
# for value in a:
#     print(value, end=' ')

# for index, value in enumerate(a, 1):
#     print(index, value)
#
# # 103-misol
# n = int(input())
# a = list(map(int, input().split()))
# k, l = map(int, input().split())
#
# s = c = 0
# for index, v in enumerate(a, 1):
#     if k <= index <= l:
#         s += v
#         c += 1
#
# print(f'{s / c:.2f}')
#

#
# # 102-misol
# from decimal import Decimal, ROUND_HALF_UP, getcontext
# getcontext().rounding = ROUND_HALF_UP
#
# n = int(input())
# l = list(map(int, input().split()))
# a, b = map(int, input().split())
#
# minimal = min(l)
#
# for index, v in enumerate(l, 1):
#     if a <= index <= b:
#         print(f'{Decimal(v / minimal):.1f}', end=' ')
#     else:
#         print(f'{v:.1f}', end=' ')
#
'''

117-ta misol kamida
https://www.programiz.com/python-programming/list
https://www.programiz.com/python-programming/tuple
https://www.programiz.com/python-programming/string
https://www.programiz.com/python-programming/set
https://www.programiz.com/python-programming/dictionary


https://www.programiz.com/python-programming/methods/list
https://www.programiz.com/python-programming/methods/tuple
https://www.programiz.com/python-programming/methods/string
https://www.programiz.com/python-programming/methods/set
https://www.programiz.com/python-programming/methods/dictionary


mutable - dict, list, set
immutable - int, float, str, bool, tuple

hashable - int, float, str, bool, tuple
unhashable - dict, list, set, tuple

container data types - list, set, tuple, dict
iterable data types - list, set, tuple, dict, str


'''