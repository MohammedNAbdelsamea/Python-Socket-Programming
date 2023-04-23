from socket import *

serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
sentence = ""
while sentence != "Exit":
    sentence = input('Enter message to send or type Exit to disconnect: ')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(f'Received Messsage from Server:  {modifiedSentence.decode()}')

print('Now you are disconnected from the server')
clientSocket.close()
