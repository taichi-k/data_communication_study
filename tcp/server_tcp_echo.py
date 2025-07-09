import socket

HOST = '127.0.0.1'
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[Server] Listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"[Server] Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("[Server] Connection closed by client")
                break
            text = data.decode()
            print(f"[Server] Received: {text!r}")
            # 受け取ったメッセージをそのまま返す
            text += "ってなんやねん"
            conn.sendall(text.encode())
            print(f"[Server] Sent back: {text!r}")
