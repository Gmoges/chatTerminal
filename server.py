# server_chat.py
import socket
import threading

host = '0.0.0.0'
port = 4444

server = socket.socket()
server.bind((host, port))
server.listen(1)

print("[+] Waiting for a connection...")
client, addr = server.accept()
print(f"[+] Connected with {addr}")

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(f"[CLIENT]: {message}")
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
