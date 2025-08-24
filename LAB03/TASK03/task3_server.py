import socket
import threading
port = 5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

buffer = 16
server_socket_address = (host_ip, port)

format = "utf-8"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)
disconnected = "End"

server.listen()
print("server is listening to you.....")

def handle_clients(conn, addr):
    print("Connect to: ", addr)
    connected = True
    while connected:
        message_lenght = conn.recv(buffer).decode(format)
        print("Lenght of the given message:" , message_lenght)
        
        if message_lenght:
            message_lenght = int(message_lenght)
            msg = conn.recv(message_lenght).decode(format) 
            if msg == disconnected:
                conn.send("Bye,see you soon". encode(format))
                print("Terminating connection with: ", addr)
                connected= False
            
            else:
                vowels = "aeiouAEIOU"
                count = 0
                
                for i in msg:
                    if i in vowels :
                        count+=1
                if count == 0 :
                    conn.send("Not enough vowels" .encode(format))
                
                elif   count <= 2 :
                    conn.send ("Enough vowels I guess". encode(format))
                else:
                    conn.send ("Too many vowels". encode(format))
                    
                        
    conn.close()
                
                
while True:
    conn, addr = server.accept()
    
    thread = threading.Thread(target=handle_clients, args=(conn,addr))
    thread.start()        
        
        
    

