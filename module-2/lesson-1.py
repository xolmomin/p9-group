# safety name
#
# ubuntu, mint
#
# identifier
#
# name_9 =
# % = 2
# package, folder, directory, module
#


# OOP concepts 6ta

# Inheritance (Vorislik)
# Polymorphism (kop hillik 2ga bolinadi)
# - overloading (2ta bir hil funksiya yozish) (pythonda yoq)
# - overridden (ota classdagi methodni bolasida qayta yozish)

# Encapsulation
# public, protected, private

# Abstraction
# Object
# Class

#
# def add(a, b, c):
#     return a + b + c
#
#
# def add(a):
#     return a + 10
#
# # result = add(5, 10, 15)
# # print()
#
# print(locals())

# dunder method, magic method
# class Student:
#     name = 'Botirjon'
#     age = 14
#
#
# student_1 = Student()
# student_2 = Student()
# print(student_1.name, student_1.age)
# print(student_2.name, student_2.age)

#
# class Student:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def get_age(self):
#         return 2022 - self.year
#
#     def __str__(self):
#         return f'{self.name} {self.year}'
#
#
# student_1 = Student('Botirjon', 2002)
# student_2 = Student("G'aybulla", 1994)
# print(student_1.get_age())

# print(student_1.)
# print(student_2.get_age())

# print(student_2)

# student_2.age = 35
#
# print(student_1)
# print(student_2)
#
# a = [2, 3, 4]


#
# class Student:
#     def __init__(self, name: str, year: int) -> None:
#         self.name = name
#         self.year = year
#
#     def get_age(self):
#         return 2022 - self.year
#
#     def __str__(self):
#         return f'{self.name} {self.year}'
#
#
# student_1 = Student('Botirjon', 2002)
# student_2 = Student("G'aybulla", 1994)
# print(student_1.get_age())

'''
Student
first_name, last_name, phone, age, course

'''

# class Student:
#
#     def __init__(self, first_name: str, last_name: str, phone: int, age: int, course: str) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phone = phone
#         self.age = age
#         self.course = course

# def __str__(self) -> str:
#     return f'{self.first_name} {self.last_name}'

# def __repr__(self) -> str:
#     return f'{self.first_name} {self.last_name} repr'


# s = 'Botirjon Jumabayev 998991002020 45 English'
#
# students: list = []
#
# for _ in range(2):
#     first_name, last_name, phone, age, course = input().split()
#     phone = int(phone)
#     age = int(age)
#     student_1 = Student(first_name, last_name, phone, age, course)
#     students.append(student_1)
#
#
# print(*students)
# for student in students:
#     print(student)

# def __int(self):

# students = []

# 6ta student

# Botirjon Jumabayev 998991002020 45 English
# Botirjon Jumabayev 998991002020 45 English
# Botirjon Jumabayev 998991002020 45 English
# Botirjon Jumabayev 998991002020 45 English


# numbers = []
#
#
# 13
# 45
# 67
# 14
# 0

# 13 45 67 14

# class Student:
#     name = 'Botirjon'
#
#     def __str__(self) -> str:
#         return f'{self.name}'
#
#
# s1 = Student()
# print(s1)
#


# class Shape:  # shakl
#     def __init__(self, yuzasi) -> None:
#         self.yuzasi = yuzasi
#
#
#
# class Triangle:  # uchburchak
#
#     def __init__(self, a, b, c, burchaklar_soni) -> None:
#         self.a = a
#         self.b = b
#         self.c = c
#         self.burchaklar_soni = burchaklar_soni
#


# class Car:
#     model = 'GM'

# attribute, field - ozgaruvchi
# class attribute - obyekt olmasdan turib ishlatish mumkin
# object attribute - obyekt olingandan keyin ishlatiladigan attribute
#
# class Car:  # 30%
#     __slots__ = ['age', 'name']
#     # # constructor
#     # def __init__(self, year) -> None:
#     #     self.year = year
#
#
# car = Car()
# car.name = 'BWM'
# # car.year = 2020
# print(car.name)
# print(car.year)
#
# Car.name = 'BWM'
# Car.year = 2017
# Car.hdgasjh = 36721
#
# setattr(Car, 'name', 'BWM')
#
# print(Car.hdgasjh)
# print(Car.year)
# print(Car.age)
# print(Car.name)

'''
delattr()
setattr()
getattr()
hasattr()
'''


# a = [2, 3, 4]
# print(a[-2])

# print(Car.name)
# class Cobalt(Car):
#     name = 'cobalt'
#     year = 2020
#     color = 'oq'
#
# d = {
#     # 'key': 5
# }
# print(d)
# d['key'] = 11
# print(d)

# s = 'name'
# print(Car.age)
# delattr(Car, 'age')
# print(Car.age)


# car_1 = Car()
# setattr(Car, 'model', 'BWM')
#
# print(car_1.model)
# print(Car.model)

# car_1 = Car()
# print(car_1.name)
# print(car_1.age)
# print(Car.age)

# name = 'BWM x5'
# year = 2020
# color = 'oq'


# s = input('Object attribute ni kiriting: ')
# if hasattr(Car, s):
#     print(getattr(Car, s),' bor')
# else:
#     print(s, ' yoq')

# s = input() # rangi
# print(car.rangi)
# print(car.name)
# print(getattr(car, s)) # car.rangi

# cobalt = Cobalt()
# Car.model = 'BMW'
# cobalt_2 = Cobalt()
# print(cobalt.model)
# print(cobalt_2.model)
#

# overridden
# class Car(object):
#
#     def get_model(self) -> None:
#         print('Car')
#
#
# class GM(Car):
#
#     def get_model(self) -> None:
#         super().get_model()
#         print('GM')
#
#
# a = GM()
#
# a.get_model()
#
