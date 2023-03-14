from socket import *

serverName = "10.200.130.23"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
keep_communicating = True
clientSocket.connect((serverName, serverPort))

while keep_communicating:
    sentence = input('Input sentence: ')
    if sentence == "close;":
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode())
        keep_communicating = False
    else:
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode())
clientSocket.close()
