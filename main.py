import json
from string import lower
from lucky_class import Inventory, Compendium
from place import Place


class Game:

    def __init__(self):
        stock = Inventory("ingredient")
        dish = Inventory("recipe")
        recipe_compendium = Compendium("recipe")
        with open('recipelist.json', "r") as open_file:
            data = json.load(open_file)
            for key in data:
                recipe_compendium.unlock(key)
        print recipe_compendium
        shop_compendium = Compendium("ingredient")
        with open('ingredientlist.json', "r") as open_file:
            data = json.load(open_file)
            for key in data:
                shop_compendium.unlock(key)
        print shop_compendium
        money = 50
        here = Place(0)
        user_input = ""
        while user_input != "leave":
            here.description()
            user_input = lower(raw_input("What do you want to do or where do you want to go ? ('leave' to exit)\n"))
            if user_input == "leave":
                break
            there = here.go_to(user_input)
            here = there
        pass


Game()
