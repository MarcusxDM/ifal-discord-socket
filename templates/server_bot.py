import socket
import json

CLIENT_PUBLIC_KEY = 'key'

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 10000))
    server_socket.listen(1)

    print("Server started, listening for connections...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")

        data = client_socket.recv(1024).decode()
        request = json.loads(data)
        if request.get("command") == "ping":
            response = {"message": "Pong!"}
            client_socket.send(json.dumps(response).encode())

        client_socket.close()

if __name__ == "__main__":
    main()