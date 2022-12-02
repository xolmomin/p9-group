# 300-349
# 147
# 135

# list, tuple, set, dict, str
# # 300-misol
# s = 'double' if n % 2 == 0 and n % 3 == 0 else (2 if n % 2 == 0 else (3 if n % 3 == 0 else 'none'))
# print(s)
#
# n = int(input())
# print('double' if not n % 6 else 2 if not n & 1 else 3 if not n % 3 else 'none')


# list comprehension
# set comprehension
# dict comprehension

# a = [2, 3, 4, 5, 6, 7, 8, 9]

# list comprehension
# b = []
#
# for i in a:
#     b.append(i * i)
#
# print(b)
# print(*b)  # unpacking
# a = [2, 3, 4, 5]
# b = [i * i for i in a]

#
# print(b)
# print(*b)


# a = [2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# toq sonlar va juft sonlarni 0ga aylantiradi
# for i in a:
#     if i % 2 == 1:
#         b.append(i)
#     else:
#         b.append(0)
#
# print(b)

# b = [i if i % 2 == 1 else 0 for i in a if]
# print(b)


# 1-51
# 3ga karrali bolsa, **3
# toq bolsa 0
# juft bolsa ** 2

# b = []
# for i in range(1, 51):
#     if not i % 3:
#         b.append(i ** 3)
#     elif i & 1:
#         b.append(0)
#     else:
#         b.append(i * i)
#
# print(b)

# b = [i ** 3 if i % 3 == 0 else (i * i if i % 2 == 0 else 0) for i in range(1, 51)]
# print(b)

# b = [i ** 3 if not i % 3 else 0 if i & 1 else i * i for i in range(1, 51)]
# print(b)

# 1-101
# 2 3 5
# %2 = **2
# %5 = 1

# b = [i * i if i % 2 == 0 else (1 if i % 5 == 0 else i) for i in range(1, 101) if i % 2 == 0 or i % 3 == 0 or i % 5 == 0]
# print(b)

# 4,3,8,1,36

# n = 8
# m = 6
#
# if n < m:
#     print('m katta')
# else:
#     print('n katta')
#
# s = 'm katta' if n < m else 'n katta'
# print(s)

# for i in a:
#     if i % 2 == 1:  # if i & 1:
#         print(i, end=' ')
#
# b = [i for i in a if i % 2 == 1]
# print(b)
#
# d = (2, 9, 4, 5, 4)
# # % 3 = **2

# d1 = set(i * i if i % 3 == 0 else i for i in d)
# print(d1)

# d1 =  []
# for i in d:
#     if i % 3 == 0:
#         d1.append(i * i)
#     else:
#         d1.append(i)
# d1 = tuple(d1)
# print(d1)


# d = (2, 9, 4, 5, 8, 3, 3, 2, 2, 2)
# 0, 7, 8, 9
#
# r = [index for index, value in enumerate(d) if value == 2]
# print(r)
#
#
# r = []
# for index, value in enumerate(d):
#     if not value ^ 2:
#         r.append(index)
#
# print(r)
#
# XOR
# n ^ n = 0

# a ^ b = c
# c ^ b = a
# a ^ c = b
# a = 7
# b = 4
# c = a ^ b
#
# print(c ^ b)
# print(c ^ a)
#
# # 101
# # 100
# # 001

# dict
# d = {
#     'key-2': 'value-2',
#     'key-3': 'value-3',
#
# }

# mutable, immutable
# d.clear()
# print(d)
# print(d.popitem())
# print(d)
# d['key-5'] = 'new value-3'

# t = {'key-3': 'new value-3', 'key-2': 'new value-2', 'key-4': 'new-value-4'}
# d.update(t)

# print(d)
# for i in d:
#     print(i, end=' ')
#
# print()
# for i in d.keys():
#     print(i, end=' ')
#
# print()
# for i in d.values():
#     print(i, end=' ')

# print()
# for key, value in enumerate(d):
#     print(key, value)
#

# print(list(d.items()))
# print(list(d.keys()))
# print(d.pop('key-3'))
# d.
# print(d.get('key-3', 'yoq'))
# print(d)
# print(d['key-3'])
