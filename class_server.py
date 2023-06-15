import socket

def server():
    s=socket.socket()
    s.bind(("", 56690)) #.bind binds the socket to an address
    # in the above you have two arguments, one for the address if you know/want to input something (domain) and then the port numbers
    print("server is binded")
    s.listen()                  # allows the server to listen to the connections // listens to any / open connection
    while True:                 # keeps the server open, creates a service
        conn, addr = s.accept() # creates tuple pair of socket and address
        msg = b'Welcome to BOLC 23-003 Server' # msg is welcome msg
        conn.sendall(msg)       # send the message to the client
        conn.close()            # closes the connection

server()