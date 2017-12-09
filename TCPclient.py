#!/usr/bin/env python
import socket
serverName = '127.0.0.1'
serverPort = 12009
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server:', modifiedSentence.decode())
clientSocket.close()
