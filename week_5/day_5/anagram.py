from miniproject import *

<<<<<<< HEAD
anagram_word = AnagramChecker()

while True:
    user_input = input("Please Choose a Word to Start the Game \n or Enter X to Exit the Game ").upper()
    if user_input == 'X':
        print("Sorry to see you go!")
        break
    else:
        if len(user_input.split()) > 1:
            print("Only single words allowed :(.")
        else:
            for char in user_input:
                if char.isdigit() or not char.isalpha():
                    print('Only letters allowed :(.')
                    break

            else:
                user_input = user_input.strip()
                if anagram_word.is_valid_word(user_input):
                    print("You've chosen a valid Word!")
                    print(anagram_word.get_anagrams(user_input))
                else:
                    print("This is not a valid word :(.")



=======
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
>>>>>>> 9abcdba50c603f2471068b249086de997d50f2a2









