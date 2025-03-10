from socket import *
import threading

def start_server():
    s = socket()
    host = input("Ange serverns IP-adress, t.ex. localhost eller 10.32.42.137: ")
    port = 12345
    s.bind((host, port))
    s.listen()
    print("Servern startad, väntar på klienter...")
    return s

clients = []

def broadcast(data, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(data)
            except:
                clients.remove(client)

def threaded_client(connection):
    clients.append(connection)
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break
            broadcast(data, connection)
        except:
            break

    clients.remove(connection)
    connection.close()

def main():
    server_socket = start_server()
    while True:
        conn, address = server_socket.accept()
        print(f"En ny klient anslöt: {address[0]}:{address[1]}")
        threading.Thread(target=threaded_client, args=(conn,)).start()

if __name__ == "__main__":
    main()