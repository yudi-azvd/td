from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))

print("The server is ready to receive")

while True:
  message, client_addr = server_socket.recvfrom(2048)
  # print(client_addr)
  modified_msg = message.decode().upper()
  print('client sent:', message.decode())
  server_socket.sendto(modified_msg.encode(), client_addr)
