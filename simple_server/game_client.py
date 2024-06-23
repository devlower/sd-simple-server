import Pyro4
from define_classes import Request


def send_request(action, data):
    Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')
    Pyro4.config.SERIALIZER = 'pickle'

    ns = Pyro4.locateNS()
    uri = ns.lookup('PYRO:Pyro.NameServer@localhost:9090')
    game_server = Pyro4.Proxy(uri)
    request = Request(action, data)
    result = game_server.handle_request(request)
    print(f'Received result: {result.message}')

if __name__ == '__main__':
    send_request('create_game', 'Valorant')
    send_request('create_player', 'joao_marcelo')
    send_request('create_player', 'sizonel')
    send_request('create_player', 'devlower')
    send_request('ban_player', 'devlower')