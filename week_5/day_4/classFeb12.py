class Book:
​
    def __init__(self, title, author, text):
        self.title = title
        self.author = author
        self.text = text
        self.sentences = self.text.split('. ')
​
    def __repr__(self):
        return f'Book: {self.title} by {self.author}'
​
    def __add__(self, other):
        return Book(title=self.title + ' & ' + other.title,
                    author=self.author + ' & ' + other.author,
                    text=self.text + '\n' + other.text)
​
    def __len__(self):
        return len(self.text)
​
    def __mul__(self, other):
        if type(other) == int:
            return [self] * other
        elif isinstance(other, Book):
            return [self] * len(other)
        else:
            raise TypeError('Unsupported operation')
​
    def __gt__(self, other):
        if isinstance(other, Book):
            return len(self) > len(other)
        else:
            raise TypeError('Unsupported operation')
​
    def __lt__(self, other):
        if isinstance(other, Book):
            return len(self) < len(other)
        else:
            raise TypeError('Unsupported operation')
​
    def __getitem__(self, item):
        return self.sentences[item]
​
    # def __iter__(self):
    #     self.i = 0
    #     return self
    #
    # def __next__(self):
    #     if self.i >= len(self.sentences):
    #         raise StopIteration
    #     else:
    #         out = self.sentences[self.i]
    #         self.i += 1
    #         return out
​
​
if __name__ == '__main__':
    zohar = Book(title='The Zohar', author='Rabbi Shimon bar Yohai', text="hbckhjzdc. zhjcbkjdbchz. sjkzcbhzjkhbcd. ")
    lotr = Book(title='Lord of the Rings',
                author='JR Tolkien', text='......')
​
    print(zohar)
    print(zohar + lotr)
    zohar.__add__(lotr)
    print(zohar * 3)
    print(type(zohar))
    print(zohar * lotr)
​
    print(zohar > lotr)
    print(zohar < lotr)
​
    for something in zohar:
        print(something)
​
    print(zohar[0])
​
    with open("the_stranger.txt", "r") as file:
        text = file.read()
​
    with open("my_book.txt", "w") as file:
        file.write(text)
​
# with statement is a temporary variable

# USED TO OPEN RANDOM FILES IN YOUR COMP
    stranger = Book(title='the stranger', author='Albert Camus', text=text)
​
    print(stranger)
    for sentence in stranger:
        print(sentence)
​
    print(len(stranger))

#
# with statement is a temporary variable

# USED TO OPEN RANDOM FILES IN YOUR COMP
# with open("the_stranger.txt", 'w') as file:
#     text = file.read()
#
# # with open("the_stranger.txt", 'w') as file:
# #     text = file.readline()
#
# with open("the_stranger.txt", 'w') as file:
#     text = file.write('jkokhkb')

print(text)



FAMILY EXERCISE IN CLASS:
#
# class Family:
#     def __init__(self, members, last_name):
#         def __init__(self, last_name):
#             self.members = members
#             self.last_name = last_name
#
#         def born(self, **kwargs):
#             self.members[kwargs["name"]] = kwargs
#             # self.add_member_details(name=, age=0, sex=, is_child=True, **kwargs)
#             print(f'Mazel Tov on the birth of your new child {kwargs["name"]}!')
#
#         def is_18(self,name):
#             if self.members.get(name):
#                 member = self.members.get(name)
#                 return member['age'] >=18
#             else:
#                 raise KeyError(f'{name} was not found in the family')
#
#     if __name__ == '__main__':
#         fam_dic ={"Michael":{"name": "michael", "age": 35, "Gender":'Male', "is_child": False},
#                 "Sarah":{"name": "Sarah", "age": 32, "Gender":'Female', "is_child": False},
#                 "Kevin":{"name": "Kevin", "age": 16, "Gender": 'Male', "is_child": True}
#                  }
#
# family = Family(fam_dic, "Cohen")
# print(fam_dic.get("Lea"))
# print(family.members)
#
# Moses = {'name': "Moses","age" = 0,'sex' = "Male",'is_child' = True, 'prophet' = True}
# family.born(**Moses)
# print(family.members)
# print(family.is_18, 'Michael')

# class Incredibles(Family):
#
#     def use_power(self, name):
#         member = self.members.get(name)
#         if member:
#             power = member.get('power')
#             if self.is_18(name):
#                 print(f'{member['incredible_name']} uses {power}!')
#             else:
#                 raise Exception(print("you are not old enough to do this, go to your room"))
#
#         else:
#             raise KeyError(f'{name} was not found in the family')
#
# a_dic ={"Michael":{"name": "michael", "age": 35, "Gender":'Male', "is_child": False, "incredible_name": "Super Michael"},
#                  "Sarah":{"name": "Sarah", "age": 32, "Gender":'Female', "is_child": False, "incredible_name": "Super Sarah"},
#                  "Kevin":{"name": "Kevin", "age": 16, "Gender": 'Male', "is_child": True, "incredible_name": "Super Kevin"}
#                   }
#
# inc = Incredibles(fam_dic, last_name ="smith")
#
# inc.born(name= "Jack", age= 0, gender='male', is_child =False, incredible_name= "Super Jack"}
# print(inc.members)