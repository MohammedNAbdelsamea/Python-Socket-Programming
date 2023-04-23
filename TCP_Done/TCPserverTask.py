from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print(f'Listening at {serverSocket.getsockname()}')
    connectionSocket, addr = serverSocket.accept()
    print(f'The server now in connected to:  {addr}')
    print(f'Socket connects between  {serverSocket.getsockname()} and {addr}')
    while True:
        sentence = connectionSocket.recv(1024).decode()
        print(f'Received Message from Client:  {sentence}')
        if sentence!="Exit":
            numberOfBytes = str(len(sentence))
            capitalizedSentence = (f'Your data was {numberOfBytes} bytes')
            connectionSocket.send(capitalizedSentence.encode())
        else :
            disconnectMessage = "Disconnect"
            connectionSocket.send(disconnectMessage.encode())
            break
    print('Reply sent, Server socket closed')
    connectionSocket.close()

