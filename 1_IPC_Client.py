import socket
import threading

# Function to handle client connections
def handle_client(client_socket):
    # Receive data from the client
    request = client_socket.recv(1024)
    print(f"Received: {request.decode()}")

    # Echo back the received data
    client_socket.send(request)
    client_socket.close()

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen(5)  # Listen for connections with a backlog of 5

print("Server listening on port 8888")

# Accept incoming connections
while True:
    client, addr = server.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")

    # Handle client connections in separate threads
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
