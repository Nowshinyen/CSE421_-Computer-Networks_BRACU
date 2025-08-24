import socket
port = 5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

buffer = 16
server_socket_address = (host_ip, port)
format= "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)
disconnected = "End"
server.listen()
print("Server is listening to you.....")


while True:
    conn, addr = server.accept()
    
    print("Connect to: ", addr)
    connected = True
    
    while connected :
        message_lenght = conn.recv(buffer).decode(format)
        print("Lenght of the given message: " , message_lenght)
        if message_lenght :
            message_lenght= int(message_lenght)
            msg = conn.recv(message_lenght).decode(format)
            
            if msg == disconnected :
                conn.send("Bye,see you soon". encode(format))
                
                print("Terminating connection with: ", addr)
                connected = False
            
            else:
                hour = int(msg)
                
                if hour <= 40:
                    salary=hour*200
                
                else:
                    salary = 8000
                    extra_hour = hour-40
                    salary += extra_hour*300
            conn.send(("Salary: " + str(salary)).encode(format))
                    
                        
    conn.close()
                
            
        
        
    

