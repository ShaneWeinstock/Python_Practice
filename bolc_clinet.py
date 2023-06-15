import socket
def client():
    s = socket.socket()
    s.connect(("127.0.0.1", 56690))        # connects the client to the server
    msg = bytearray ()                      # this creates a mutable bytearray to recieve from server
    buf = s.recv(4)                         #creates a buffer, s.recv(4) says to receive 4 bytes at a time (RATE)

    while buf:
        print(msg)                          # this allows us to watch the msg grow
        msg.extend(buf)                     # extends the msg based on the buf
        buf = s.recv(4)                     # keeps while True 
    print(msg)

client()