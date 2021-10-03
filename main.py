from string import lower

from lucky_action import Player


class Game:

    def __init__(self):
        player = Player()
        user_input = ""

        print "To travel : 'go' + place."
        print "To do something : 'do' + action.\n"
        while user_input != "leave":
            player.look_around()
            user_input = lower(raw_input("What do you want to do ?\n"))
            if len(user_input.split()) > 1:
                action = user_input.split()[0]
                choice = user_input.split()[1]
                if action == "go":
                    player.travel_to(choice)
                if action == "do":
                    player.do(choice)
        pass


Game()
