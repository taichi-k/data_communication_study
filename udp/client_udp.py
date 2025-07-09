# client_udp.py
import socket
import time

HOST = '127.0.0.1'
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        msg = "Hello"
        s.sendto(msg.encode(), (HOST, PORT))
        print("Sent:", msg)
        time.sleep(1)
