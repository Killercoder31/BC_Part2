import socket 
s=socket.socket()

port=12345
s.bind(('',port))
s.listen(5)
c,addr=s.accept()
count = 1

while True:
    tran=c.recv(1024).decode()
    if("Jupiter" in tran):
        c.send('Verified'.encode())
    else:
        c.send('Malicious'.encode())
    print("Total transaction verified today: ",count)
    count+=1