# a = [2, 3, 4, 5]  # 15tr6
#
# a += [2] # 15tr6
# # a = a + [2]
#
#
# a += [2]
# a = a + [2]
#

# def add(a, b):
#     return a + b
#
# result1 = add(6, 7)
# result = (lambda a, b: a + b)(5, 6)

# def add(n):
#     return int(n) + 1
#
#
# a = list(map(add, input().split()))
# print(a)


# a = list(map(lambda n: int(n) + 1, input().split()))
# print(a)
#
# def sub(a, b):
#     return a + b
#
# def add(n: int) -> str:
#     n = str(n ** 2)
#     summa = 0
#     i = 0
#     while i < len(n):
#         summa += int(i)
#         i += 1
#     return str(summa)

# a = [2, 3, 4, 5, 6, 7]
#
# def is_even(n):
#     return n % 2 == 0
#     # return not n & 1
#
# result = filter(is_even, a)
#
# print(list(result)[2])
#
# b = '2345'
# c = 'hello'
# d = 'he'
#
# print(list(zip(b, c, d)))
# for a1 in zip(b, c, d):
#     print(a1)
#


# string, hashtable, array, matrix

# [3, 0]
# s = [9, 9]
# k = 1
# for i in range(len(s) - 1, -1, -1):
#     s[i] += k
#     if s[i] > 9:
#         s[i] = 0
#         k = 1
#     else:
#         k = 0
# if k:
#     s.insert(0, 1)
#
# print(s)
#
#
# s[-1] += 1
# k = 0
# for i in range(len(s) - 1, -1, -1):
#     s[i] += k
#     if s[i] > 9:
#         s[i] = 0
#         k = 1
#     else:
#         k = 0
# if k == 1:
#     s.insert(0, 1)
#
# print(s)


# result = list(map(int, str(int(''.join(map(str, s))) + 1)))
# print(result)
# a = "11"
# b = "1"
#
# a = int(a, 2)
# b = int(b, 2)
# s = str(bin(a + b))[2:]
#
# print(s)


s = ['world  hello  ', 'a bu soz emas harf', 'python darslari boshlanish arafasida', 'botirjon aylanishga ketti']

# result = list(map(lambda i: len(i.split()), s))
# _max = max(result)
# print(s[result.index(_max)])


#
# word = ' hello  world'
#
# r1 = word.split(' ')
# r2 = word.split()
#
# print(r1)
# print(r2)


allowed = "ab"
words = ["ad", "aa", "aaab", "baa", "badab"]
allowed = set(allowed)

summa = 0
for word in words:
    if len(set(word).difference(allowed)) == 0:
        summa += 1

print(summa)


# summa = 0
# for word in words:
#     summa += not set(word).difference(allowed)
#
# print(summa)
#
#

# d = 'aaab'
# print(set(d))
