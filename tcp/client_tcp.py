# client_tcp.py
import socket
import time

HOST = '127.0.0.1'
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = "Hello"
        s.sendall(msg.encode())
        print("Sent:", msg)
        time.sleep(1)
