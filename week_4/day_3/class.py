# from typing import List
#
# l = [1, 2, 3, 45, 96]
#
# if 1 in l:
#     print("yes")
# elif 0 in l:
#     print("no")
# else:
#     print("don't know")
# #
# # empty lists, dictionaries, tupples are false
# # 0 is false too, nothing in there, unless in the list[0]
#
# l = 0
#
# if l:
#     print("yes")
# else:
#     print("don't know")
#
# l = []
#
# if l:
#     print("yes")
# elif 0 in l:
#     print("no")
# else:
#     print("don't know")
#
# l = [1, 2, 3, 45, 96]
#
# if sum(l)<10 and 2 in l:
#     print("yes")
# else:
#     print("don't know")
#
# l = [1, 2, 3, 45, 96]
# # ANY: if any values are true, it'll return true. ALL:If allll the values return true will be true, if one isnt, itll return fals.
# if all(l):
#     print("yes")
# elif 0 in l:
#     print("no")
# else:
#     print("don't know")
#
#     # if there is ALL statement if there is a 0 in the list of true values, itll return false l =[1, 4, 0] this will be false
#
# l=["u", 4, [3,2,1], {'a':28}]
#
# for element in l:
#     print(element)
#
# for index in range(len(l)):
#     print(index, l[index])

# list(range(50,100,2))
# list(range(100,50,-2))
#
# TO DUPLICATE A STRING  OR NUMBER:
# for i in range(5):
#     print("hello")

#
# [12]*10- will give me 12-10 times
#
# for i in range(10):
#     if i%2 == 0:
#         print(i)
#     elif i == 5:
#         print(i)
#     else:
#         continue
#     # (continue skips the iteration, says go to the next iteration)
#
# for i in range(10):
#     if i%2 == 0:
#         print(i)
#     elif i == 5:
#         print(i)
#         break

i = 10
while i<10:
    print(i)
    i += 1
 # (same as i = i + 1)
#
# while True:
#     value = int(input("input a number between 1 and 10: "))
#
#     if i<= value <= 10:
#         print("thank you !")
#         break
# else:
#     print("not in the valid range, please try again...")
#
# while True:
#     value = input("input a number between 1 and 10: ")

# try:
#     value = int(value)
# except ValueError:
#     print("not a number")
#     continue
#
# if not value.isdigit():
#         print("not a number")
#         continue
# else:
#         value = int(value)
#
# [num for num in range(10)]
# [num*2 for num in range(10)]
# sum([num*2 for num in range(10)])
# for num in range(10):
#     print(num)
# list comprehension is different
#
# [num*2 for num in range(10) if num%2 == 0]
# # (for num in range(10), if its even, then times it by 2, check the loop before the multiplying)
#
# l =  [num*2 for num in range(10) if num%2 == 0]
#
# [num*2 for num in range(10) if num%2 != 0] will output [1,3,5,7,9]
#
# {str(key): value for key, value in zip(range(5), range(5))}
#
# list(zip(range(5), range(5)))
#
# {str(key): value for key, value in zip(range(5), range(5))}
# {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
# >>>
# >>> list(zip(range(5), range(5)))
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
# >>> {str(key):key for key in range(5)}
# {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
#
# ages = {'20','23'}
# list(map(int,ages))
# ages = list(map(int,ages))
# print(ages)
# # MAP-will be able to map it for all list, convert it into integers for all of list in this case)
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

# NINJA EXERCISE:
# import random
# import string
# random.choices(string.ascii_letters, k=5)
# # letters = string.ascii_lowercase
# # integers = [random.randint(1, 1000) for i in range(10)]
# strings = [''.join(random.choices(string.ascii_letters, k=5)) for i in range(10)]
#
# l =integers + strings
# random.shuffle(l)
#
# string_list = []
# int_list = []
# for element in l:
#     if type(element) == str:
#         string_list.append(element)
#     else:
#         int_list.append(element)
#         print(str_list)
#         print(int_list)

# NINJA EXERCISE
#
# l = ["hi", "goes", "a", "kitchen"]
# print(sorted(l,key=len)[-1])

# def count_a(array):
#     return array.count('a')
#
# long = map(len,strings)
#
# max_length = 1
# for s in strings:
#     temp = len(s)
#
# for index in range(len(l)):
#      print(long)
#
# def find_longest_word(word_list):
#     longest_word =  max(word_list, key=len)
#     return longest_word
# # for index, element in enumerate([1,5,36]):
# #     print(index,element)