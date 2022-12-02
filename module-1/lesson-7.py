# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 100000, 1000000, 10000000,
#           100000000, 1000000000, 1000000000]
# harf = [
#     'bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz', 'o\'n',
#     'yigirma', 'o\'ttiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to\'qson', 'bir yuz',
#     'bir ming', 'bir yuz ming', 'bir million', 'o\'n million', 'bir milliard'
# ]
#
# son = 1909
# i = 23
#
# res = []
#
# while son:
#     butun_qism = son // sonlar[i]
#     son %= sonlar[i]
#
#     while butun_qism:
#         res += [harf[i]]
#         butun_qism -= 1
#     i -= 1
#
# print(*res)
