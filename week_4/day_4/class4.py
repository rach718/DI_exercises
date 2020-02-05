# import random
# def talk():
#     p= random.random()
#     if p>0.5:
#         return "whatever"
#     else:
#         print("coin toss")
#         return "something else"
#
#
# def multiply_2(num):
#     return num*2
#
# output = multiply_2(10)
# print(output)
#
#
# def multiply(num, multiplier):
#     return num * multiplier
#
# output = multiply(10 ,5)
# print(output)
#
# #
# def multiply(num, multiplier=2):
#     return num * multiplier
#
# output = multiply(10)
# print(output)

# mul = [multiply(2, multiplier) for mulitplier in range(1,11)]
# print(mul)

person = "Yair"

# def say_name(name):
#     print("Hey {}".format(name))
# say_name(person)
#
# person = "Yair"
#
# def say_name(person):
#     person += " something"
#     print("Hey {}".format(person))
# say_name(person)
# print(person)
#
# person = "Yair"
#
# def say_name(person):
#     person += " something"
#     other_guy = "Shlomo"
#     print(other_guy)
#     print("Hey {}".format(person))
#     return other_guy
#
# other_guy = say_name(person)
# print(person)
# print(other_guy)
# the * here will unpack the list, and incoorperate all of the list in show_names. the list is not the argument. its saying taking all of the list and loop through it.

# def show_names(*args):
#     for i, name in enumerate(args):
#         print(f"person number {i}: {name}")
#
# show_names("yair", "shlomo", "rachel", "eran", "mitchell")

# def show_names(*args):
#     for i, name in enumerate(args):
#         if type(name) == str:
#             print(f"person number {i}: {name}")
#         else:
#             print("404 wrong stuff happened")
#
# show_names("yair", "shlomo", "rachel", "eran", "mitchell")
#
# def show_names(*args):
#     for i, name in enumerate(args):
#         if type(name) == str:
#             print(f"person number {i}: {name}")
#         else:
#             print("404 wrong stuff happened")
#
# show_names("yair", "shlomo", "rachel", "eran", "mitchell")

# def show_info(**kwargs):
#     # print(kwargs)
#     for key, value in kwargs.items():
#         print(key,value)
# #
# # info = {"Name": 'Fred', "Last name": "Berg", "Profession": "Philosopher", "Nationality": "German"}
#
# show_info(name = "Fred",
#           last_name = "Berg",
#           Profession = "Philosopher",
#           Nationality= "German")
#
# show_info(Name = "John",
#           last_name="Smith")


# def operations(num1, num2, **kwargs):
#     if kwargs:
#         print("Description:/n {}".format(kwargs))
#     return num1 ** num2
#
# result = operations(2,3
#              , description='2 to the power 3',
#              type='mathematical")
#
# YEAR = 2020
# MONTH = 2
# def get_age(year: int, month: int, day: int):
#     if month >= MONTH:
#         age = YEAR - year
#     else:
#         age = YEAR -year -1
#     return age
#
# print(get_age(1990, 3, 1))
#
# def can_retire(sex, date_of_birth):
#     args = list(map(int, date_of_birth.split('/')))
#     month, day, year = args[0], args[1], args[2]
#     age = get_age(year, month, day)
#     print(f'your age{age}')
#     if sex.lower() == "m":
#         return age >=67
#     else:
#         return age>=62
#
# print(can_retire('m', "2/1/1995"))

# if __name__ == "==main__":
#     print("can you retire in israel? answer these few questions:")
#     sex = input("state of sez(m/f):")
#     birthdate = input("state your birth date (mm/dd/yyyy"):")
#
#     output = can_retire()(sex, birthdate)
#     if output:
#         print("happy retirement")
#     else:
#         print("sorry bro....")


# from file import variable






