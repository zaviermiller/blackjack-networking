import time, socket, sys, json, select
from threading import Thread
from Player import Player
from Blackjack import Blackjack

class Server:

    def __init__(self):
        print("Booting Blackjack Server v1...\n")
        time.sleep(1)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.host = socket.gethostname()
        self.port = 5555
        self.s.bind((self.host, self.port))
        print(f'[*] Blackjack Server v1 booted at {socket.gethostbyname(self.host)}:{self.port}\n')
        self.players = []
        self.in_game = False
    
    def broadcast(self,message):
        print(message)
        for player in self.players:
            player._connection.sendall(message.encode())
            
def client_thread(player):
    while True: 
            try: 
                message = player._connection.recv(2048) 
                if message:
                    broadcast(f'[{player}] {message}')
  
                else: 
                    pass  
            except: 
                continue       

if __name__ == "__main__":
    player_count = int(input("How many players?: "))

    server = Server()

    server.s.listen()
    print(f"[*] Waiting for connections...")

    while server.in_game is False:
        conn, addr = server.s.accept()
        if conn not in [player._connection for player in server.players]:
            data = conn.recv(1024)
            player = Player(data.decode())
            player.set_connection(conn)
            server.players.append(player)
            server.broadcast(f'[*] {player} has joined the game')
            # Thread(target=client_thread, args=(player,)).start()
            if len(server.players) == player_count:
                server.in_game = True
                print('[*] Game start')

    game = Blackjack(server.players)

    game.deal()

    while server.in_game is True:

        for player in server.players:
            # JSON format to send data => {"text": text, "active": True/False}
            try:
                player._connection.sendall(json.dumps({"text": player.show_cards(), "active": player == game.active_player()}).encode())
            except IndexError:
                if game.winner is None:
                    game.winner = server.players[0]
                    for player in server.players:
                        if player.get_value() < 21 and player.get_value() > game.winner.get_value():
                            game.winner = player
                player._connection.sendall((f'{game.winner} is the winner!'.encode()))
        data = game.active_player()._connection.recv(1)
        if data.decode() == '0':
            print(f'[*] Dealt {game.hit(game.active_player())} to {game.active_player()}\n')
            game.active_player().order_cards()
            if game.active_player().get_value() > 21:
                game.next_player()
        else:
            print(f'[*] {player} stayed\n')
            game.next_player()
                
