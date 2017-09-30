0#############################################################################
# Program:
#    Lab PythonWebServerT2, Computer Communication and Networking
#    Brother Jones, CS 460
# Author:
#    Paul Bowman
# Summary:
#    This program is a simple http server in python
#
#############################################################################
#############################################################################
# No changes made for resubmission
#############################################################################
#!/usr/bin/env python
import sys
import socket


DEFAULT_VALUE = 6789
CRLF = "\r\n"

port = int(sys.argv[1]) if len(sys.argv) == 2 else DEFAULT_VALUE
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(1)
print "Server listening for response\n"

try:
    while 1:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(2048)
        sentenceDeco = sentence.decode()
        
        req = sentenceDeco.split(' ')[1]
        fileExists = True
        try:
           content = open(req[1:])
        except IOError:
            fileExists = False
        if fileExists == True:
            statusLine = "HTTP/1.0 200"
            if req.endswith(".html") or req.endswith(".htm"):
                contentType = "text/html"
            if req.endswith(".jpeg"):
                contentType = "text/jpeg"
            if req.endswith(".gif"):
                contentType = "text/gif"
            if req.endswith(".txt"):
                contentType = "text/plain"
            else:
                contentType = "application/octet-stream"
            contentTypeLine = "Content-type: " + contentType + CRLF
            message = statusLine + contentTypeLine + CRLF + content.read()
        else:
            statusLine = "HTTP/1.0 404"
            contentTypeLine = "Content-Type: text/html" + CRLF
            content = "<HTML><HEAD><TITLE>Not Found</TITLE><BODY>Not Found</BODY></HTML>"
            message = statusLine + contentTypeLine + CRLF + content
        connectionSocket.send(message)
        connectionSocket.close()
    
except KeyboardInterrupt:
    print "\nClosing Server"
    serverSocket.close()
