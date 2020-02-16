# class Pet:
#     def __init__(self, species, name, color):
#         self.species = species
#         self.name = name
#         self.col0r = color
#
#     def eat(self):
#         print("eat mice")
#     def sleep (self):
#             print("18hr/day")
#     def talk(self):
#         print(f"meow!My name is {self.name}")
#
#
# class House:
#     def __init__(self, city, num_rooms, landlord):
#         self.city = city
#         self.num_rooms = num_rooms
#         self.landlord = landlord
#
#         self.rent = 1000 * self.num_rooms
#         if city == "TA":
#             self.rent *= 2
#
#     def sign_contract(self, name, date):
#         if self.landlord == "Moti":
#             self.rent *= 2
#             print(f"Rental agreement between {name} and {self.landlord} for NIS{self.rent}")
#
#     def complain_about_broken_window(self):
#             print(f"{self.landlord} says Sorry about that I cant help")

# my house = House("TA", 2, "Moti")
#             type(myhouse)
# myhouse.sign_contract("jon","today")

# yourhouse = ("jerusalem", 4, "shlomo")
# all_houses = [myhouse, yourhouse]
# myhouse == yourhouse
# False

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#         self.winner = False
#         # (we dont know yet whos the winner so set to False)
#
#     def talk(self):
#         print("woof")
#
#     def jump(self):
#         self.height *= 2
#         print(self.height)
#
#     def fight(self, another_dog):
#         if self.height > another_dog.height:
#             return self
#         else:
#             return another_dog
#
#
# davids_dog = Dog("Rex", 50)
# print(davids_dog.name)
#
# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name)
#
#
# if davids_dog.height > sarahs_dog.height:
#     davids_dog.winner = True
# else:
#     sarahs_dog.winner = True
#
# print(davids_dog.winner)
# print(sarahs_dog.winner)
#
# # def fight(dog1, dog2):
# #     if dog1.height > dog2.height:
# #         return dog1
#
# davids_dog = Dog("Rex", 50)
# print(davids_dog.name)
#
# sarahs_dog = Dog("Teacup", 20)
# # davids_dog is self here, sarahs_dog is another_dog here
# # variable and calling a function
# winner = davids_dog.fight(sarahs_dog)
# print(f'The winners name is {winner.name}')

# class Str:
#     def __init__(self, text):
#         self.text = text
#
#         def upper(self):
#             upper_text =self.text made into upper case
#             return upper_text

class Zoo:
    def __init__(self, my_zoo):
        self.animals = []
        self.my_zoo = my_zoo
        self.pen = {}

    def addAnimal(self, newAnimal):
        if newAnimal not in self.animals:
            self.animals.append(newAnimal)

    def getAnimals(self):
        print(self.animals)

    def sellAnimal(self, animal_to_sell):
        self.animals.remove(animal_to_sell)
        print(f'Goodbye {animal_to_sell}')

    def sortAnimals(self, animals):
        animals_sorted = self.animals.sort()
        pen = {}
        temp = 0
        for x, y in zip(animals[::], animals[1::]):
            if x[0] == y[0]:
                pen[temp] = [x,y]
            else:
                temp += 1
                pen[temp] = x
                pen[temp] = y
        print(pen)



my_zoo = Zoo('Tel Aviv Zoo')
my_zoo.addAnimal("zebra")
my_zoo.addAnimal("hippopotamus")
my_zoo.addAnimal("gorilla")
my_zoo.addAnimal("lion")
my_zoo.addAnimal("flamingo")
my_zoo.addAnimal("bear")
my_zoo.addAnimal("leopard")
my_zoo.addAnimal("monkey")
my_zoo.getAnimals()

my_zoo.sellAnimal("zebra")
my_zoo.getAnimals()

my_zoo.sortAnimals(my_zoo.animals)
my_zoo.getAnimals()
