#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
import sys

#Prepare a sever socket
#Fill in start
serverPort = 678
serverSocket.bind(("", serverPort))
#Fill in end

serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept() #Fill in start              #Fill in end          
    try:
        message =  connectionSocket.recv(1024).decode() #Fill in start          #Fill in end               
        filename = message.split()[1]                 
        f = open(filename[1:])                        
        outputdata = f.read()#Fill in start       #Fill in end                   
        
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in end                
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start        
        connectionSocket.send("HTTP/1.1 404 Not found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found </h1></body></html>\r\n".encode())
        #Fill in end
        
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end            
serverSocket.close()
sys.exit()
