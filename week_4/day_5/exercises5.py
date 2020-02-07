# Exercise 1:
# x = 5
# y = 4
# if x > y:
#     print(f'x is great than y')
# else:
#     print(f'y is greater than x')

# # Exercise 1 with function:
# def greater_num(num1,num2):
#     if num1 > num2:
#         print(f'num1 is great than num2')
#     else:
#         print(f'num1 is greater than num2')
# greater_num(4,6)

# Exercise 2:
# win_letter = "r"
# while letter != win_letter:
#     letter = input("Guess the computers letter? ")
#
# print(f"You won! The letter was {win_letter}!")

# # Exercise 2 with function:

# letter = "d"
# def check_guess(guess, letter):
#     if letter == guess:
#         return True
#     else:
#         return False
#
# def letter_guess():
#     guess = input("Guess a letter: ")
#     result = check_guess(guess, letter)
#     if result:
#         print("Hooray! You guessed right!")
#         return True
#     else:
#         print("Sorry, try again")
#         return False
#
# answer = letter_guess()
# if answer:
#     print("You did it!")
# else:
#     print("The winning letter was",letter)


# Exercise 3:

# letters = ['a', 'b', 'c', 'd']
# for letter in letters:
#     print(letter.upper())

# Exercise 3 in a function:

# def to_uppercase(oldList):
#     newList = []
#     for letter in oldList:
#         newList.append(letter.upper())
#         return newList

# string_to_change =['a', 'b','c','d']
# changed_string = to_uppercase(string_to_change)
# print(string_to_change)

# # Another way:
# letters = ['a', 'b', 'c', 'd']
# letters2 = list(map(str.upper, letters))
# print(letters2)

# Exercise 4:
# def contains_letter(letters_list, letter_to_check):
#     is_letter_found = False
#     for letter in letters_list:
#         if letter == letter_to_check:
#             is_letter_found = True
#
#     return is_letter_found
#
#
# result = contains_letter(["a","b","c"], "b")
# if result:
#     print("We found the letter")
# else:
#     print("We did not find the letter")

# Exercise 6:
# def add(num1, num2):
#     return num1 + num2
#
# answer = add(4,6)
#
# if answer>12:
#     print("great")
# else:
#     print(f'{answer} is less than 12')

# Exercise 7:
# Exercise 1:
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
#
# filled = "*"
# space = " "
# def show_tree():
#     for row in picture:
#      for star in row:
#          if (star):
#             print(filled, end =" ")
#          else:
#             print(space, end =" ")
#      print('')
#
# show_tree()
# show_tree()
# show_tree()

# Exercises for practice:

# def say_hello(name='bob', emoji=':)'):
#     print(f'hello {name} {emoji}')
# say_hello('andrei', ':)')
# say_hello('sam', ':)')
#
# say_hello()

# def sum(num1, num2):
#     return num1 + num2
#
# total = sum(10,5)
# print(sum(10,total))
#
# def sum(num1, num2):
#     def another_func(n1, n2):
#         return n1 + n2
#     return another_func(num1, num2)
#
# total= sum(10,20)
# print(total)
