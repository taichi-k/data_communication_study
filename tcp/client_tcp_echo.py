import socket
import threading

HOST = '127.0.0.1'
PORT = 8081

def recv_loop(sock):
    """サーバからのメッセージを常時待ち受けて表示"""
    while True:
        data = sock.recv(1024)
        if not data:
            print("[Client] Connection closed by server")
            break
        print(f"[Client] Received echo: {data.decode()!r}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # 別スレッドで受信ループを開始
    threading.Thread(target=recv_loop, args=(s,), daemon=True).start()

    print("[Client] Connected. Enterキーで送信します。Ctrl+Cで終了。")
    try:
        while True:
            msg = input() or "Hello"
            s.sendall(msg.encode())
            print(f"[Client] Sent: {msg!r}")
    except KeyboardInterrupt:
        print("\n[Client] Exiting.")
