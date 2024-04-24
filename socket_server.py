import socket

# Endereço e porta do servidor
HOST = '127.0.0.1'
PORT = 10000

# Cria um objeto socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Liga o servidor ao endereço e porta especificados
    server_socket.bind((HOST, PORT))

    # Ouve por conexões recebidas
    server_socket.listen()

    print(f'Servidor socket escutando em {HOST}:{PORT}')

    # Aceita conexões entrantes
    client_socket, addr = server_socket.accept()

    with client_socket:
        print(f'Conexão recebida de {addr}')

        # Recebe dados do cliente
        data = client_socket.recv(1024)
        
        if data.decode() == "!socket":
        # Envia os dados de volta para o cliente
            client_socket.sendall(b'pong')
        client_socket.close()