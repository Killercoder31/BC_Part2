import socket
class Node():
    def __init__(self,password):
        self.s=socket.socket()
        self.password=password
    
    def connect_to_node(self,host,port):
        self.s.connect((host,port))

    def close_conn(self):
        self.s.close()
    
    def get_verified(self,new_tran):
        unver_tran=str(new_tran)+self.password
        self.s.send(unver_tran.encode())
        return self.s.recv(1024).decode()


