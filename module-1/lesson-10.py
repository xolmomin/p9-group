'''
mutable - list, set, dict
immutable
hashable
unhashable - list, set, dict, [tuple]
iterable - str, list, set, dict, tuple
container - dict, tuple, set, list
sequence - str, tuple, dict, list
'''

# type hinting
# docs
from typing import Any, Union, Optional, List

# a: Union[list[float]] = [2.3, 2.3]
# b: Optional[list] = [2.3, 2.3]

# l: Union[list, int, None] = None
# t: Optional[Union[int, str]] = None
# t: Any = 2


# def add(a: int, b: int) -> str:
#     return str(a + b)


# add(7, 4)
#
# a: int = 5
# a = 'hello'
# print(a)


# lambda, function

# nums = [2, 7, 11, 15]
# target = 17
# d = {
#     15: 0,
#
# }
#
# for i in range(len(nums)):
#     if nums[i] in d:
#         print(i, d[nums[i]])
#     d[target - nums[i]] = i

# for i in range(len(nums)):
#     if d.get(nums[i]):
#         print(i, d[nums[i]])
#     d[target - nums[i]] = i

#
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# counter = 0
# d = {}
# for i in sentence:
#     if not d.get(i):
#         counter += 1
#         d[i] = True
#
#
# print(counter == 26)
#
# if counter == 26:
#     print(True)
# else:
#     print(False)
#

# len(set(sentence)) == 26


# sentence = "thequickbrownfoxjumpsoverthelazydog"
#
# '''
# eng kop qatnashgan
# eng kam qatnashgan
#
# '''

d = {
    'key': 'value',
    'key1': 'value'
}

for i in d.items():
    print(i)

