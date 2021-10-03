from string import capitalize


class Place:

    PLACE_DESCRIPTION = {
        0: {
            "name": "main road",
            "can_go": [1, 2, 3],
            "look_desc": ["on the"]
        },
        1: {
            "name": "cafe",
            "can_go": [0, 3, 4],
            "look_desc": ["in the"]
        },
        2: {
            "name": "shop",
            "can_go": [0],
            "look_desc": ["in the"]
        },
        3: {
            "name": "room",
            "can_go": [1, 4],
            "look_desc": ["in your"]
        },
        4: {
            "name": "kitchen",
            "can_go": [1, 3],
            "look_desc": ["in the"]
        }
    }

    def __init__(self, key):
        self.key = key
        for attr in self.PLACE_DESCRIPTION[key]:
            setattr(self, attr, self.PLACE_DESCRIPTION[key][attr])

    def description(self):
        print "You are " + self.look_desc[0] + " " + self.name + "."
        if self.name == "kitchen":
            print "Here you can 'cook' things.\n"
        if self.name == "shop":
            print "Here you can 'buy' or 'sell' ingredients.\n"
        if self.name == "cafe":
            print "Here you can 'sell' dishes.\n"
        print "You can go to those places :"
        for test in self.can_go:
            print capitalize(Place(test).name + ".")
        print ""

    def go_to(self, choice):
        for test in self.can_go:
            if choice == Place(test).name:
                print "You go to : " + Place(test).name + "\n"
                return Place(test)
        print "There is no such place around."
        return Place(self.key)
