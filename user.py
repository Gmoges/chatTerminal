# client_chat.py
import socket
import threading

host = '127.0.0.1'  # Use Kali IP or 127.0.0.1 if on same machine
port = 4444

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
