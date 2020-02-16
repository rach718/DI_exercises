import time

# # class Person:
# #     def __init__(self, name, last_name, age, tz):
#
#         # p1 = Person(Yair, Hochner, 28, teuda)
#         # p2 = Person(Eli, Gabay, 19, teuda)
#         # self is how the instance will behave, it refers to P1 and P2.
#         # P1 and P2 are instances of the class Person.
#         # p2.talk()-method
#
#         # p2.name will get me the name of p2. P2 is now self.
# #
# # STATIC METHOD-dont need the info of the instance-allows you to put in other parameters instead of self.
# # class Circle:
# #
# #         def __init__(self, radius):
# #                 self.radius =radius
# #
# #         def area(self):
# #                 return math.pi * self.radius**2
# #
# #         @staticmethod
# #         def compute_area(r):
# #                 return math.pi * r ** 2
# #
# # if __name__="__main__":
# #         c = Circle(radius=2)
# #         print(c.area())
# #         print(c.compute_area(r=5))
# #
# #         compute_area(self, r=5)
# #
# #         staticmethod(compute_area(r=5))
#
#
#
# class Writer:
#         def __init__(self, name, n_books, genre):
#                 self.name = name
#                 self.n_books = n_books
#                 self.genre = genre
#
#         def write(self):
#                 self.n_books +=1
#                 print(f'{self.name} wrote a book')
#
#         @staticmethod
#         def say_hi():
#                 print("Hi!")
#
#
# class Philosopher(Writer):
#         # (all attributes including the staticmethod are inherited from the parent class, in this case the writer)
#         def __init__(self, name, n_books, genre, domain):
#                 super().__init__(name, n_books, genre)
#                 self.domain = domain
#
#         def write_nonsense(self):
#                 self.n_books +=1
#                 print(f"{self.name}: What is this nonsense")
#
#
# class French:
#         def __init__(self,name):
#                 self.name = name
#         def talk_nonsense(self):
#                 print(f"{self.name}: Blah blah...nonsense...blah blah")
#
#
# class FrenchPhilosopher(French, Philosopher):
#         def conference(self):
#                 print(f"{self.name}: ..post modern nonsense..")
#
#
#
# if __name__ == '__main__':
#         albert = Writer(name="Albert Camus", n_books=25, genre=["philosophy", "roman"])
#         print(albert.name)
#
#         albert.write()
#         print(albert.n_books)
#         print(albert.genre)
#
#         albert.write()
#         print(albert.n_books)
#         albert.say_hi()
#
#         fred =Philosopher(name="Freidrich", n_books=30, genre=["amoralism","uberstuff"])
#         print(fred.n_books)
#         fred.write()
#         print()
#
#
#         derrida =FrenchPhilopsher(name=j"jacques Derrida", n_books=100)
#
#         derrida.confernece() #from frenchphilosopher
#         derrida.talk_nonsense() #from French
#         derrida.write() #writer
#         derrida.write_nonsense() #from Philosopher


# DECORATOR:

def decorator(func):
        def wrapper():
                print(f'running {func}')
                func()
                print('done')
        return wrapper

@decorator
def talk():
        print('some talk')

def timeit(func):
        def wrapper(*args, **kwargs):
                start = time.perf_counter()
                func(*args, **kwargs)
                stop = time.perf_counter() - start
                print(f'function took: {end}')
                return output
        return wrapper

@timeit
def compute(power):
        return 2**5

@timeit
def talk():
        print('some talk')

if __name__ == '__main__':
        talk()
