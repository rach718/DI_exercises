# # Exercise 1- Part 1:
# import random
# def get_random_temp():
#     return random.randint(-10, 40)
#
# def main():
#     temp = get_random_temp()
#     print(f'The temperature right now is {temp} degrees Celsius.')
#     if temp < 0:
#         print ("Brr that's freezing! Wear some extra layers today.")
#     elif temp >=0 and temp <=16:
#         print("Quite chilly! Don't forget your coat!")
#     elif temp >=16 and temp <=23:
#         print("It's a nice day to have a drink on your terrace!")
#     elif temp >=24 and temp <=32:
#         print("Perfect day to jump into your pool!")
#     elif temp >=32 and temp <=40:
#         print("It's very hot outside! Drink enough water today!")
#
# main()
#
# # Exercise 1-Part2, including float challenge:
# import random
# import numpy.random
# def get_random_temp(season):
#     if season.lower() == 'summer':
#         temp = random.uniform(30,40)
#     elif season.lower() == 'autumn':
#         temp = random.uniform(20, 30)
#     elif season.lower() == 'winter':
#         temp = random.uniform(10, 10)
#     elif season.lower() == 'spring':
#         temp = random.uniform(10, 20)
#     else:
#         temp = random.uniform(10, 40)
#
#     return temp
#
# def main():
#     t = input("what season is it? ")
#     temp = get_random_temp(t)
#     print(f'The temperature right now is {temp} degrees Celsius.')
#     if temp < 0:
#         print ("Brr that's freezing! Wear some extra layers today.")
#     elif temp >=0 and temp <=16:
#         print("Quite chilly! Don't forget your coat!")
#     elif temp >=16 and temp <=23:
#         print("It's a nice day to have a drink on your terrace!")
#     elif temp >=24 and temp <=32:
#         print("Perfect day to jump into your pool!")
#     elif temp >=32 and temp <=40:
#         print("It's very hot outside! Drink enough water today!")
#
# main()

# EXERCISE 2:
# import random
# def throw_dice():
#     toss=random.randint(1,6)
#     return(toss)
#
# def throw_until_doubles():
#     dict = {}
#     counts = 1
#     while True:
#         toss1 = throw_dice()
#         toss2 = throw_dice()
#         dict[counts] = [toss1,toss2]
#         counts += 1
#         if toss1 == toss2:
            # print("you've reached doubles!")
            # print(dict)
            # print(counts-1)
#             return counts-1
# def main():
#     list = []
#     i = 1
#     while i<101:
#         list.append(throw_until_doubles())
#         i+=1
#         print(list)
#         sum_of_list = sum(list)
#         print(f'the dice was thrown {sum_of_list} times')
#         average = sum_of_list/len(list)
#         print(round(average,2))
# main()
