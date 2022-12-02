# import random
#
# a = []
#
# for i in range(20):
#     a.append(random.randint(10, 100))
#     a += [random.randint(10, 100)]
#
# print(a)


# shuffle
# randint
# choice
#
# import random
#
# b = [1, 2, 3, 4, 5, 6]
# random.choices(b)
#
# print(b)
#
# print(12)
# a = 2
#
# print(a)
#
# a += 29
#
# d = {'hello'}
#
# print(d)
#
# l = [2, 3, 4, 5, 6, 7]
#
# for i, v in enumerate(l):
#     if i == 3: # 5
#         print('hello')
#         print()
#     print(v, end=' ')


# module - python file
# package - module lar yigindisi (va ichida __init__ file bolgan papka)
# folder, directory
# framework - package lar yigindisi
# backend framework, django, spring, fastapi, flask

# s = 'ab'
# goal = 'ba'
#
#
# def solve(s, goal):
#     if len(s) != len(goal) or not (s == goal and len(set(s)) < len(s)):
#         return False
#     v = set()
#     for s1, g1 in zip(s, goal):
#         if s1 != g1:
#             v.add(s1)
#         if len(s) > 2:
#             return False
#     return len(s) == 2
#
#
# solve(s, goal)

#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# summa = 0
# for i in range(len(matrix)):
#     summa += matrix[i][i]
#     if i != len(matrix) - i - 1:
#         summa += matrix[i][len(matrix) - i - 1]
#
# # print(summa)


# image = [
#     [1, 1, 0],
#     [1, 0, 1],
#     [0, 0, 0]
# ]
# # 1-v
# for row in image:
#     row.reverse()
#     for i in range(len(row)):
#         if row[i] == 1:
#             row[i] = 0
#         else:
#             row[i] = 1

# # 2-v
# for row in image:
#     row.reverse()
#     for i in range(len(row)):
#         row[i] ^= 1
#
#
# for i in image:
#     print(i)


accounts = [
    [1, 2, 3],  # 6
    [3, 2, 1], # 6
    [2, 2, 1], # 5
]
# # 1v
# result = []
# for row in accounts:
#     result.append(sum(row))
#
# print(max(result))
#

# # 2v
# result = max(sum(row) for row in accounts)
# print(result)


# 3v
# result = max(map(sum, accounts))
# print(result)

