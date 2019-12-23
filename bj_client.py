import socket, json, time, sys

HOST = socket.gethostname()
PORT = 9999

name = input("Name: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(name.encode())
    while True:
        data = s.recv(2048)
        try:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            data = json.loads(data.decode().replace('\r\n', '\\r\\n'))
            print(data.get("text"))
            if data.get("active") == True:
                move = (input("Hit (0) or Stay (1)?: "))
                s.sendall(move.encode())
            else:
                print("Waiting for players...")
        except Exception as e:
            print(data.decode())
            break