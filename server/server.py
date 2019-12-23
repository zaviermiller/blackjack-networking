import time, socket, sys, json
from Player import Player
from Blackjack import Blackjack

# class Server:

#     def __init__(self):
#         self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.host = socket.gethostname()
#         self.port = 5555

# if __name__ == "__main__":
#     server = Server()

player_count = int(input("How many players? "))

print("Booting Blackjack Server v1...\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 9999
s.bind((host, port))
print(host, "(", ip, ")\n")

players = []
in_game = False

s.listen()

while in_game is False:
    sys.stdout.write(f"\rWaiting for connections ({len(players)}/{player_count})...")
    conn, addr = s.accept()
    data = conn.recv(1024)
    player = Player(data.decode())
    player.set_connection(conn)
    players.append(player)
    if len(players) == player_count:
        in_game = True
        sys.stdout.write(f"\rWaiting for connections ({len(players)}/{player_count})...\n\n")

game = Blackjack(players)

game.deal()

while in_game is True:
    winner = None

    for player in players:
        # JSON format to send data => {"text": text, "active": True/False}
        try:
            player._connection.sendall(json.dumps({"text": player.show_cards(), "active": player == game.active_player()}).encode())
        except IndexError:
            winner = players[0]
            if winner is None:
                for player in players:
                    if player.get_value() < 21 and player.get_value() > winner.get_value():
                        winner = player
            player._connection.sendall((f'{winner} is the winner!'.encode()))
            in_game = False
    data = game.active_player()._connection.recv(1)
    if data.decode() == '0':
        print(f'Dealt {game.hit(game.active_player())} to {game.active_player()}\n')
        game.active_player().order_cards()
        if game.active_player().get_value() > 21:
            game.next_player()
    else:
        print(f'{player} stayed\n')
        game.next_player()
                    
                
