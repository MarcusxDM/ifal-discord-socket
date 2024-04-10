import discord
import socket

# Token do bot do Discord
TOKEN = 'MTIyNzYwNDAwMjM1OTc0MjUyNA.GV_5Md.LduTg_BMUl8hJfFqovbRdV8KVYG3Qcu_seo5-4'

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.members = True

# Criar um cliente do Discord
client = discord.Client(intents=intents)

async def enviar_para_discord(message, content):
    # Verifica se a mensagem foi enviada em um canal de guilda (servidor)
    if message.guild:
        # Obtém o canal onde a mensagem foi recebida
        canal = message.channel
        await canal.send(content)
    else:
        print("Mensagem recebida fora de um canal de servidor.")


async def enviar_para_socket(message):
    # Endereço e porta do servidor socket
    HOST = '127.0.0.1'
    PORT = 10000

    # Cria um objeto socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Conecta ao servidor
        client_socket.connect((HOST, PORT))

        # Envia a mensagem para o servidor
        client_socket.sendall(message.content.encode())

        # Recebe a resposta do servidor
        resposta = client_socket.recv(1024)
        print('Resposta do servidor:', resposta.decode())
        await enviar_para_discord(message, resposta.decode()) 

async def enviar_para_socket2(message):
    # Envia a mensagem para o servidor
    CLIENT_SOCKET.sendall(message.content.encode())

    # Recebe a resposta do servidor
    resposta = CLIENT_SOCKET.recv(1024)
    print('Resposta do servidor:', resposta.decode())
    await enviar_para_discord(message, resposta.decode()) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!ping'):
        # await message.channel.send('Pong!')
        await enviar_para_socket2(message)
    elif message.content.startswith('!socket'):
        await enviar_para_socket(message)



HOST = '127.0.0.1'
PORT = 10000

# Cria um objeto socket
CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT_SOCKET.connect((HOST, PORT))

# Iniciar o bot
client.run(TOKEN)
