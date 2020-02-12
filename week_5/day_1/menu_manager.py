class MenuManager:
    def __init__(self):
        self.menu = {}

    def add_item(self, name, price, spice, gluten):
        items = {
            "name": name,
            'price': price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu[name] = items

    def print_menu(self):
        print(self.menu)

    def update_item(self, name, price, spice, gluten):
            if name in self.menu:
                self.menu[name]['price'] = price
                self.menu[name]['spice'] = spice
                self.menu[name]['gluten'] = gluten
            else:
                print(f"{name} is not on menu")

    def remove_item(self, name):
        if name in self.menu:
            del self.menu[name]
            print(self.menu)
        else:
            print(f"{name} is not on menu")


new_dish = MenuManager()
new_dish.add_item("Steak", 60, "B", True)
new_dish.add_item("Penne Vodka", 45, "A", True)
new_dish.add_item("Greek Salad", 40, "A", True)
new_dish.print_menu()


new_dish.update_item("Sushi", 45, 'A', False)
new_dish.print_menu()

new_dish.update_item("Greek Salad", 45, 'B', True)
new_dish.print_menu()

new_dish.remove_item("Steak")





# PLEASE IGNORE THE BELOW. THANKS!

# To add spice:
#
#
# def add_item(self, name, price, spice, gluten):
#     item = {}
#     item["name"] = name
#     item["price"] = price
#     if spice == "A":
#         item["spice"] = "not spicy"
#     elif spice == "B":
#         item["spice"] = "a little spicy"
#     elif spice == "C":
#         item["spice"] = "very spicy"
#     item["gluten"] = gluten
#     self.menuItems.append(item)

# class MenuManager:
#     def __init__(self):
#         self.menu = []
#
#     # def actual_menu(self):
#     #     {  "Salad":{
#     #             "name" : "Greek Salad",
#     #             "price": 40,
#     #             "spice": "a",
#     #             "gluten": True
#     #         },
#     #         "Pasta":{
#     #             "name": "Penne Vodka",
#     #             "price": 40,
#     #             "spice": "a",
#     #             "gluten": False
#     #     }
#     #     }
#
#     def add_item(self, name, price, spice, gluten):
#         menu_item = {
#             "name": name,
#             'price': price,
#             "spice": spice,
#             "gluten": gluten
#         }
#         self.menu.append(menu_item)
#
#     def print_menu(self):
#         print(self.menu)
#
#     def update_item(self, name, price, spice, gluten):
#             for item in self.menu:
#                 if item['name'] == name:
#                     item['price'] = price
#                     item['spice'] = spice
#                     item['gluten'] = gluten
#
#                     return item
#
#             temp_list = []
#             for item in self.menu:
#                 temp_list.append(item['name'])
#
#             if name not in temp_list:
#                 print(f"{name} is not on menu")
#
#
#     def remove_item(self, name):
#         temp_list = []
#         for item in self.menu:
#             temp_list.append(item['name'])
#
#         if name not in temp_list:
#             print(f"{name} is not on menu")
#             return self.menu
#
#         for count,item in enumerate(self.menu):
#             # print(count,item)
#             if item['name'] == name:
#                 index_of_dict = count
#                 # print(index_of_burgers_dict)
#         self.menu.pop(index_of_dict)
#         print(self.menu)
#         return self.menu
#
#
#
#             # temp_list = []
#             # for item in self.menu:
#             #     temp_list.append(item['name'])
#             #
#             # if name not in temp_list:
#             #     print(f"{name} is not on menu")
#
# new_dish = MenuManager()
# new_dish.add_item("burger", 50, "c", True)
# # new_dish.print_menu()
# new_dish.add_item("salad", 50, "c", True)
# # new_dish.print_menu()
#
#
# new_dish.update_item("cracker", 45, 'b', False)
# # new_dish.print_menu()
#
# new_dish.remove_item("burger")
# new_dish.remove_item("burger")
# # print(new_dish.print_menu())