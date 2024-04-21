import socket

# Set up the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

# Send data to the server
client.send(b"Hello, abcdddddd!")

# Receive data from the server
response = client.recv(1024)
print(f"Received from server: {response.decode()}")

# Close the connection
client.close()
