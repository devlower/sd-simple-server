import Pyro4

@Pyro4.expose
class Game:
    def __init__(self, title):
        self.title = title

@Pyro4.expose
class Player:
    def __init__(self, username):
        self.username = username
        self.banned = False

    def ban(self):
        self.banned = True

@Pyro4.expose
class Result:
    def __init__(self, message):
        self.message = message

@Pyro4.expose
class Request:
    def __init__(self, action, data):
        self.action = action
        self.data = data

    def execute(self, server):
        if self.action == 'create_game':
            return server.create_game(self.data)
        elif self.action == 'create_player':
            return server.create_player(self.data)
        elif self.action == 'ban_player':
            return server.ban_player(self.data)
        else:
            return Result('Invalid action')