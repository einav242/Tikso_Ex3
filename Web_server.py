# import socket module
from socket import *
import sys  # In order to terminate the program


def web_server():
    serverPort = 6789
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a sever socket
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open("hello_world.html", "r")
            outputdata = f.read()
            print(outputdata)
            #  Send one HTTP header line into socket
            # Fill in start
            connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode('utf-8'))
            # Fill in end
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()

        except IOError:
            connectionSocket.send('\nHTTP/1.1 404 Not Found\n'.encode())
            connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())

    # Send response message for file not found
    # Fill in start
    # Fill in end
    # Close client socket
    # Fill in start
    # Fill in end
            serverSocket.close()
    # sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == '__main__':
    web_server()
