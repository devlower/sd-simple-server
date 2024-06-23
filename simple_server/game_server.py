import Pyro4
from define_classes import Game, Player, Result, Request

@Pyro4.expose
class GameServer:
    def __init__(self):
        self.games = {}
        self.players = {}

    def create_game(self, title):
        if title in self.games:
            return Result(f'Game {title} already exists.')
        game = Game(title)
        self.games[title] = game
        return Result(f'Game {title} created successfully.')

    def create_player(self, username):
        if username in self.players:
            return Result(f'Player {username} already exists.')
        player = Player(username)
        self.players[username] = player
        return Result(f'Player {username} created successfully.')
    
    def ban_player(self, username):
        if username not in self.players:
            return Result(f'Player {username} does not exists.')
        self.players[username].ban()
        return Result(f'Player {username} has been banned.')
    
    def handle_request(self, request):
        if isinstance(request, Request):
            result = request.execute(self)
            return result
        else:
            raise TypeError('Invalid request type')
        
        
        
def start_server():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(GameServer)
    ns.register('test.gameServer', uri)
    print('Server is running')
    daemon.requestLoop()

if __name__ == '__main__':
    start_server()
    
