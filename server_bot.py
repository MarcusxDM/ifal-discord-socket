import socket
import json

CLIENT_PUBLIC_KEY = 'f325fcdd88cbb70c7e48af11f4f372e54b9b249f6c4e8eaf480907b40db90c4a'

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