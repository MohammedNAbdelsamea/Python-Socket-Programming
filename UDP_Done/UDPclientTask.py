from socket import *

serverIP = '127.0.0.1'
serverPort = 12000


clientPort = int(input("Enter your port number"))
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('',clientPort))

message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverIP, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())

clientSocket.close()
