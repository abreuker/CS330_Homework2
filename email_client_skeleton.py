from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver =   ("smtp.gmail.com", 465) 

# Create a TCP socket called clientSocket 
#Fill in start  
clientSocket = socket(AF_INET, SOCK_STREAM)
#Fill in end
clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Authentication using base64
# For Gmail, it is recommended to create an "app password" and
# use that value in the password field instead of the regular password.
# username and password values should be enclosed in quotes: 
# Example: username = "sample@gmail.com" 
username = "toadletgames@gmail.com"
password = "xxxxxxxxxxxxxxxx"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())
    
# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <toadletgames@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("mail from command:\r\n " +recv2)
# Fill in end

# Send RCPT TO command and print server response. 
# Fill in start
rcptTo = "RCPT TO:<abreuker@mail.bradley.edu>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("rcpt to command:\r\n " + recv3)
# Fill in end

# Send DATA command and print server response. 
# Fill in start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("data command\r\n " +recv4)
# Fill in end

# Send message data.
# Fill in start
subject = "This is a test email! Hello!\r\n\r\n"
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print("send message data:\r\n " + recv5)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitVar = "QUIT\r\n"
clientSocket.send(quitVar.encode())
recv6 = clientSocket.recv(1024).decode()
print("quit command:\r\n " + recv6)
# Fill in end
