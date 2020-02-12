class Family:
    def __init__(self, last_name):
        self.members = {}
        self.last_name = last_name

    def add_member_details(self, name, age, sex, is_child):
        member = {
            "name": name,
            'age': age,
            "sex": sex,
            "is_child": is_child
        }
        self.members[name] = member

    def print_members(self):
        print(self.members)

# class Children(Family):
#     def __init__(self, last_name):
#         super().__init__(self, last_name)

    def born(self,**kwargs):
        self.members[kwargs["name"]] = kwargs
        # self.add_member_details(name=, age=0, sex=, is_child=True, **kwargs)
        print(f'Mazel Tov on the birth of your new child {kwargs["name"]}!')

    def is_18(self, name):
        for child in self.members:
            if self.members[name]['age'] > 18:
                return True
                # print(f'{name} is older than 18')
            else:
                # print(f'{name} is younger than 18') how to stop it from printing 4 times.
                return False

    def Smith_Family(self):
        paragraph = f"The Smith family has {len(self.members)} members, and their names are: "
        for k, v in self.members.items():
            paragraph += ", " + v["name"]
            # for child, children in v.items():
            #     paragraph += f" {child} : {children}; "
            # paragraph += "\n"
        print(paragraph)

family1 = Family("Smith")
member1 = family1.add_member_details("Michael", 35, 'Male', False)
member2= family1.add_member_details("Sarah", 32, 'Female', False)
member3 = family1.add_member_details("Kevin", 16, 'Male', True)
family1.print_members()

family1.born(name="Moses", age=0,sex="Male",is_child=True,prophet=True)
print(family1.last_name)
family1.print_members()

print(family1.is_18("Kevin"))
family1.Smith_Family()

