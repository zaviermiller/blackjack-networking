import socket, json, time, sys

try:
    HOST = sys.argv[1]
except IndexError:
    print('ERROR: Please use the command: python bj_client.py [SERVER IP]')
    exit()
PORT = 5555

name = input("Name: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(name.encode())
    while True:
        data = s.recv(2048)
        try:
            data = json.loads(data.decode().replace('\r\n', '\\r\\n'))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(data.get("text"))
            if data.get("active") == True:
                move = (input("Hit (0) or Stay (1)?: "))
                s.sendall(move.encode())
            else:
                print("Waiting for players...")
        except json.JSONDecodeError:
            print(data.decode())