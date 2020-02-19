from miniproject import *

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












