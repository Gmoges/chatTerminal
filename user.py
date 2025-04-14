# client_chat.py
import socket
import threading

host = input("Enter server IP address: ")  # Example: 10.0.2.15
port = int(input("Enter port number: "))   # Example: 4444


client = socket.socket()
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(f"[SERVER]: {message}")
        except:
            print("[!] Connection closed.")
            break

def send():
    while True:
        msg = input("YOU: ")
        client.send(msg.encode())

# Create threads
threading.Thread(target=receive).start()
threading.Thread(target=send).start()
