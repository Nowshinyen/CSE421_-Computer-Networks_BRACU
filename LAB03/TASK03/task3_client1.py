import socket
port = 5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

format = "utf-8"
server_socket_address = (host_ip, port)
disconnected = "End"

buffer= 16
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)

def msg_to_send(msg):
    message = msg.encode(format)
    msg_lenght = len(message)
    msg_lenght = str(msg_lenght).encode(format)
    msg_lenght += b" "*(buffer - len(msg_lenght))
    client.send(msg_lenght)
    client.send(message)
    print(client.recv(2048). decode(format))


while True:
    prompt = input("please give a word:")

    if prompt == disconnected :
        msg_to_send(disconnected)
        break

    else:
        msg_to_send(prompt)

client.close()
        
        