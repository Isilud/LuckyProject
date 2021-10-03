import json

##########################################
# Import json object, used by other class
##########################################
from string import capitalize


class DataFileMixin:

    @staticmethod
    def _get_by_index(key, category):
        with open('{list}list.json'.format(list=category), "r") as open_file:
            # with open(renpy.loader.transfn('data/{list}list.json'.format(list=category)), "r") as open_file:
            data = json.load(open_file)
            return data[str(key)]


#############################
# Set and manage inventories
#############################

class Inventory(DataFileMixin):
    MAX_NUMBER = 99

    def __init__(self, category):
        self.key = []
        self.quantity = []
        self.category = category

    # Find where the key is. -1 if not present.
    def find(self, key):
        if key in self.key:
            return self.key.index(key)
        else:
            return -1

    # Sort inventory by key value.
    def sort(self):
        key = self.key
        quantity = self.quantity
        zipped = zip(key, quantity)
        zipped.sort(key=lambda index: index[0])
        sorted_key = []
        sorted_quantity = []
        for line in zipped:
            sorted_key.append(line[0])
            sorted_quantity.append(line[1])
        self.key = sorted_key
        self.quantity = sorted_quantity

    # Add to inventory.
    def add(self, key, number=1):
        where = self.find(key)
        if number > self.MAX_NUMBER:
            number = self.MAX_NUMBER
        if where < 0 and number > 0:
            self.key.append(key)
            self.quantity.append(number)
        else:
            self.quantity[where] += number
            if self.quantity[where] > self.MAX_NUMBER:
                self.quantity[where] = self.MAX_NUMBER

    # Remove from inventory.
    def remove(self, key, number=1):
        where = self.find(key)
        if where < 0:
            print "You have no " + self._get_by_index(key, self.category)["name"] + "."
            return False
        else:
            if self.quantity[where] < number:
                print "You don't have enough " + self._get_by_index(key, self.category)["name"] + "."
                return False
            else:
                self.add(key, -number)
                if self.quantity[where] == 0:
                    self.key.pop(where)
                    self.quantity.pop(where)
                return True

    def __str__(self):
        zipped = zip(self.key, self.quantity)
        result = ""
        for line in zipped:
            result += "\n{0} : {1}".format(self._get_by_index(line[0], self.category)["name"], line[1])
        return result


# Compendium tracking discovered ingredients and dishes.
class Compendium(DataFileMixin):

    def __init__(self, category):
        self.category = category
        self.key = []
        self.status = []
        with open('{list}list.json'.format(list=category), "r") as open_file:
            data = json.load(open_file)
            for key in data:
                self.key.append(key)
                self.status.append(False)

    def __str__(self):
        result = "\n"
        line = zip(self.key, self.status)
        if self.category == "ingredient":
            for index in line:
                if index[1]:
                    ingredient = self._get_by_index(index[0], "ingredient")
                    result += capitalize("{0} : {1} g\n".format(ingredient["name"], ingredient["price"]))
        elif self.category == "recipe":
            for index in line:
                if index[1]:
                    recipe = self._get_by_index(index[0], "recipe")
                    result += capitalize("{0}\n".format(recipe["name"]))
                    for ingredient in zip(recipe["ingredient_which"], recipe["ingredient_many"]):
                        result += "   - " + capitalize("{0} : {1}".format(
                            self._get_by_index(ingredient[0], "ingredient")["name"], ingredient[1]))
        return result

    # Unlock a recipe if it exist
    def unlock(self, key):
        if key in self.key:
            self.status[self.index(key)] = True
        else:
            print ("No recipe with the ID {0}".format(key))
