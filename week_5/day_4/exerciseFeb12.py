import random
import statistics


class ForceWielder:
    def __init__(self, name):
        self.name = name
        self.power = random.randint(1,15)
        self.wisdom = random.randint(1,15)


    def train(self):
        pass

    def fight(self, other):
        fighter1 = statistics.harmonic_mean([self.power, self.wisdom])
        fighter2 = statistics.harmonic_mean([other.power, other.wisdom])
        print(fighter1)
        print(fighter2)
        if fighter1 > fighter2:
            print(f'winner is, {self.name}')
        else:
            print(f'winner is, {other.name}')

    def is_jedi(self):
        pass

class Jedi(ForceWielder):
    def __init__(self, name):
        super().__init__(name)

        if self.wisdom > self.power:
            self.lightsaber_color = 'Green'
        elif self.power > self.wisdom:
            self.lightsaber_color = 'Blue'
        elif self.power == self.wisdom:
            self.lightsaber_color = 'Violet'
        print(self.lightsaber_color)

        self.wisdom = self.wisdom + 10
        print(self.wisdom)

    def train(self):
        self.wisdom = self.wisdom + random.randint(10,20)
        self.power = self.power + random.randint(5,15)
        print(self.wisdom, self.power)

    def is_jedi(self):
       return True

class Sith(ForceWielder):
    def __init__(self, name):
        super().__init__(name)

        self.name = "Darth" + name
        print(self.name)

        self.lightsaber_color = 'red'
        print(self.lightsaber_color)
        self.power = self.power + 10
        print(self.power)

    def train(self):
        self.wisdom = self.wisdom + random.randint(5, 15)
        self.power = self.power + random.randint(10, 120)
        print(self.wisdom, self.power)

    def is_jedi(self):
        return False

p1 = ForceWielder("Abby")
p2 = ForceWielder("Rachel")
p1.fight(p2)
jedi = Jedi("Anakin")

jedi.train()
print(jedi.is_jedi())

p3 = Sith(" Mitch")
p3.train()
print(p3.is_jedi())




