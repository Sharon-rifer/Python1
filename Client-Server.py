from multiprocessing.connection import Client

SERVER(server.py)
import socket
HOST = '127.0.0.1'
PORT = 65432
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}...")
        conn, addr = s.accept()
        with conn:
            print("Connected by {addr}")
            conn.sendall(b"Hello from server!")
            except Exception as e:
            print("Server error:", e)



Client(client.py)
import socket
HOST = '127.0.0.1'
PORT = 65432
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024)
        print("Received from server:", data.decode())
        except Exception a as e:
        print("Client error:", e)




