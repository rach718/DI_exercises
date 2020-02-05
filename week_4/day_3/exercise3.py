# Exercise 1:

# a = int(input("select a number from 1 to 10 "))
# b = int(input("select a number from 1 to 10 "))
# if a > b:
#     print("hello world")
# else:
#     print("try again")

# Exercise 2:
# l = []
# for number in range(3):
#     x = int(input("select a number from 1 to 10 "))
#     l.append(x)
# print(sorted(l)[-1])

# Exercise 3:
# x = int(input("Insert a month in digits "))
# if x in range(3,6):
#     print("spring")
# elif x in range(6,9):
#     print('summer')
# elif x in range(9, 12):
#     print("autumn")
# elif x in [1,2,12]:
#     print("winter")
# else:
#     print("try again")

# Exercise 4:
# x = input("please select any one letter ")
# if x in ('a', 'e', 'i' , 'o', 'u'):
#      print("This letter is a vowel.")
# else:
#     print("This is a consonant.")

# Exercise 5:
# import random
# random_number = random.randint(1,9)
# guess = int(input("enter a number from 1 to 9 to guess computer number "))
# print("You chose", guess)
# if random_number == guess:
#     print("You won")
# else:
#     print(f"sorry, try again. The correct number is {random_number}.")

# Exercise 6:
# x = range(1,21)
# for i in x:
#     print(i)

# Exercise 7:
# l = []
# x = range(1, 1000001)
# for i in x:
#     l.append(x)

# Exercise 8:
# l = []
# for i in range(1, 1000001):
#     l.append(i)
# print(min(l))
# print(max(l))
# print(sum(l))

# Exercise 9:
# for i in range(0,6):
#     print(str(i*"*"))

# # Exercise 10:
# list = ["apple", "oranges", "grapes", "oranges", "banana"]
# print(list.index("oranges"))

# Exercise 11:
# list1 = ["apple", "oranges", "grapefruit"]
# list2 = ["strawberry", "blueberry", "blackberry"]
# list1.extend(list2)
# print(list1)
#
# Exercise 12:
# topping = input("Please select your choice of pizza toppings. Print quit when done. ")
# add_topping = ""
# while topping != "quit":
#         add_topping= input("Please select another topping of your choice ")
#         if add_topping == "quit":
#                 break
#         else:
#                 topping = (topping + ", " + add_topping)
#                 print(topping + " will be added to your pizza.")
# while True:
#                 print("It was great serving you. Goodbye")
#                 break
#
# Exercise 13:

# age = int(input("Welcome: What is your age? "))
#
# while True:
#         if age <=2:
#                 print("  You get in free!")
#                 break
#         elif age <= 12:
#                 print("  Your ticket is $10.")
#                 break
#         else:
#                 print("  Your ticket is $15.")
#                 break