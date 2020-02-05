menu_selection = None
menu_text = 'Welcome to the menu\nPlease select what youd like to do:\na. print hello\nb. say your name\nx.exit:'
while menu_selection != 'x':
    menu_selection = input(menu_text)
    if menu_selection == 'a':
        print('hello')
    elif menu_selection == 'b':
        user_name = input('Tell me your name')
        print(f'Hello {user_name}')

 NINJA=
import sys
import random
from copy import copy
user_string =input('please write something 10 characters long:')
if len(user_string) != 10:
    print("Must be 10 characters long..")
    sys.exit(1)
    print(user_string)

    info = f"First Character: {user_string[0]}, Last Character: {user_string[-1]}"
    print(info)

for i in range(1, len(user_string)+1):
        print(user_string[:i])

        for i in range(len(user_string)):
            print(f"iter {i}: " + user_string[:i+1])

        jumbled = copy(user_string)
        jumbled =random.shuffle(list(jumbled))
        jumbled = ''.join(jumbled)
        print(jumbled)



