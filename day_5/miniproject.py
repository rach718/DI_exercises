import itertools

class AnagramChecker:
    def __init__(self):
        self.list = open("sowpods.txt", "r").read().split("\n")


    def is_valid_word(self, word):
        if word in self.list:
            return True
        else:
            return False


    def get_anagrams(self, word):
        anagrams = []
        perms = [''.join(perm) for perm in itertools.permutations(word)]
        for words in perms:
            if words in self.list:
                anagrams.append(words)
        return anagrams


    def is_anagram(self, word1, word2):
        if word1 in self.get_anagrams(word2):
            return True
        else:
            return False

my_checker = AnagramChecker()

# print(my_checker.list)

my_other_checker = AnagramChecker()

is_anagram = my_checker.is_anagram("MEAT", "MATE")

# print(is_anagram)



# my_checker.is_valid_word("HELLO")
#
# my_checker.get_anagrams("DOG")
#
# print(my_checker.is_anagram("DOG", "GOD"))