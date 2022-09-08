# from random import random


# number = [1, 4, 2]

# num = [2, 3, 5]

# print([x*y for x in number for y in num])

# print(len(num))
# print(random.shuffle(num))

# import string


# print(string.ascii_lowercase+string.ascii_uppercase)

# def out(a, b):
#     def inn(c, d):
#         return c + d
#     return inn(a, b)
    

# red = out(5, 10)
# print(red)

# def fun(name, age=20):
#     print(name, age)
# fun("emma", 25)

# if 4 + 5 == 10:
#     print("True")
# else:
#     print("false")
# print("True")

# i = 2
# while True:
#     if i%3 == 0:
#         break
#     print(i)

#     i += 2

# w = 0.5
# numItems = 5

# if w < 1:
#     price = 1.45
# if w >= 1:
#     price = 1.15
# total = w * price
# if numItems >= 10:
#     total *= 0.9

# print(3 * w)
# print(3 * price)
# print(3 * total)

# import sys
# print("enter: ")
# name= ''
# while True:
#     c = sys.stdin.read(1)
#     if c == '\n':
#         break
#     name += c

# print("name is ", name)


# def change(a):
#     b=[x*2 for x in a]
#     print(b)

# def change(a):
#     b=[x*x for x in a]
#     print(b)

# s=[1,2,3]
# print(change(s))

# a = {1:"a", 2:"b", 3:"c"}
# print(a)
# print(1 in a)
# del a

# print(a)

# import  collections

# a=collections.Counter([1,1,2,3,3,4,4,4])

# print(a)

# d1 = {"jon": 40, "peter": 45}
# d2 = {"jon": 400, "peter": 45}

# print(d1>d2)

# class test:
#     def __init__(self, a):
#         self.a = a

#     def dis(self):
#         print(self.a)

# obj=test()
# print(obj.dis())

# class fruit:
#     def __init__(self, price):
#         self.price = price
# obj=fruit(50)

# obj.quantity = 10
# obj.bags = 2
# print(obj.quantity+len(obj.__dict__))

class demo:
    def __init__(self):
        pass

    def test(self):
        print(__name__)

obj = demo()
print(obj.test())