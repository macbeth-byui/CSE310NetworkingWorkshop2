"""
CSE310 Networking Workshop - Example 2 - Solution

This example will explore a peer to peer architecture using Python 
sockets.  The example also a client/server component (Directory Server).
"""

import socketserver
import socket
import threading

# This is the current peer directory that we will use to chat with 
# others.  This will be updated by the Directory Server after each
# chat message we send.  The Directory Server uses port 5000 but
# chat messages will use port 6000.
directory = dict()

class Chat_Server(socketserver.BaseRequestHandler):
    """
    Each peer will have its own server to receive messages from
    other peers.
    """
    def handle(self):
        # Just display the messages.
        source_msg = None
        print("\n{}\n".format(source_msg))


def refresh_directory(username, directory_address):
    """
    Send username to directory server and return back the updated 
    directory dictionary.
    """
    pass

def send_chat(src_username, tgt_username, message):
    """
    Send chat message to another user.  The chat message will be prefixed
    with our username.  The IP address is obtained from the directory dictionary.
    """
    pass        
        

# Get information from user to start the chat session
directory_ip = input("Enter IP Address of Directory Server: ")
directory_address = (directory_ip, 5000)

username = input("Enter you unique username: ")

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
server_address = (ip_address, 6000)
print("Starting Chat Server: [{}:{}]".format(server_address[0], server_address[1]))

# Create the chat server in a background thread and then use a while loop to read
# message requests from the user in the main thread
with socketserver.UDPServer(server_address, Chat_Server) as server:
    

    request = None
    while request != "quit":
        # Request an updated directory from the server directory server
        directory = refresh_directory(username, directory_address)
        print("Directory: {}".format(list(directory.keys())))
        # User will need to type username followed by a colon followed by the message
        request = input("(username:msg)> ")
        request_parts = request.split(":")
        if len(request_parts) == 2:  # Ignore if invalid
            send_chat(username, request_parts[0], request_parts[1])

    print("Stopping Chat Server")
    server.shutdown()