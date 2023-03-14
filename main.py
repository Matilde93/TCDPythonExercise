from socket import *
import threading


def handle_client(connection_socket, address):
    print(address)
    keep_communicating = True

    while keep_communicating:
        sentence = connection_socket.recv(1024).decode()
        sentence_partition = sentence.partition(": ")
        function_name = sentence_partition[0].lower()
        message = sentence_partition[2][:-1].lower()

        if sentence == "close;":
            connection_socket.send('closing'.encode())
            keep_communicating = False

        elif function_name == "reverse":
            connection_socket.send(message[::-1].encode())

        elif function_name.lower() == "lower":
            connection_socket.send(message.lower().encode())

        elif function_name.lower() == "upper":
            connection_socket.send(message.upper().encode())

    connection_socket.close()


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:
    connection_socket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connection_socket, addr)).start()
