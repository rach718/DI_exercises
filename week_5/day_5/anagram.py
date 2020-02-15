from miniproject import *

user_input = input("Please Choose a Word to Start the Game \n or Enter X to Exit the Game ").upper()
user1 = is_valid_word()

while True:

    # for word in user_input:
    if user_input == 'X':
        print("Sorry to see you go")
        break
    elif len(user_input.split()) > 1:
        print("Input must be a single world only, no numbers, no characters")

    elif user_input == user1(is_valid_word):
        print(True)



user_input2 = AnagramChecker.is_valid_word()
user_input2 = user_input.strip()



# def show_menu(self):
#     if user_input2 == "":
#         print(user_input)
#     else:
#         return False









