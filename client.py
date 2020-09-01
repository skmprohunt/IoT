import socket               
s = socket.socket()         
host = socket.gethostname() 
port = 12345                
s.connect((host, port))
print(s.recv(1024))
s.send(b"78781F100F0C1D0B0F34C6027AC74C0C4658100014D401CC00287D001F71002623090D0A")
s.close()                     
