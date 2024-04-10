import socket
import json
# Endereço do servidor e porta
HOST = 'localhost'  # Ou '127.0.0.1'
PORT = 10000

data_to_send = {'command': 'ping'}

# Converter o JSON em uma string e, em seguida, em bytes
json_data = json.dumps(data_to_send).encode()

# Cria um objeto socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conecta ao servidor
    s.connect((HOST, PORT))

    # Envie dados para o servidor
    s.sendall(json_data)

    # Receba dados do servidor
    data = s.recv(1024)

print('Recebido:', data.decode())