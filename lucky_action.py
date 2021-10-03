from string import capitalize, lower

from lucky_class import Inventory, Compendium, Place


class Player:

    def __init__(self):
        self.stock = Inventory("ingredient")
        self.dish = Inventory("recipe")
        self.recipe_compendium = Compendium("recipe")
        self.shop_compendium = Compendium("ingredient")
        self.money = 50
        self.here = Place(0)
        pass

    # Travel to {choice} if able.
    def travel_to(self, choice):
        for test in self.here.can_go:
            if lower(choice) == lower(Place(test).name):
                print "You travel to : " + capitalize(Place(test).name + "\n")
                self.here = Place(test)
                return
        print "There is no such place around."

    # Show place description.
    def look_around(self):
        print self.here.description()

    # Do an action if able.
    def do(self, choice):
        if self.here.can_do_this(choice):
            print "You can do that."
        else:
            print "You can't do that here."
