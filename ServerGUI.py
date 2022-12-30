#from tkinter import *
import socket
import _thread as th

s = socket.socket((socket.AF_INET),socket.SOCK_STREAM)
host="127.0.0.1"
port=1234
msg = ""
s.bind((host,port))
s.listen(50)
sesson=[]

def recvValue(con,adr, usr):
    while True:
        try:
            msg = con.recv(1024).decode('utf-8')
            #+' '+str(adr[1])
            if msg == 'StopConnection':
                for ses in sesson:
                    if ses == con:
                        sesson.pop(sesson.index(ses))
                        ses.close()
                    else:
                        msg1 = usr + " : Exit From Chat Window"
                        ses.send(msg1.encode('utf-8'))
            else:
                msg = usr + " : " + msg
                for ses in sesson:
                    if ses != con:
                        ses.send(msg.encode('utf-8'))
        except ConnectionResetError as e:
            pass

while True:
    conn, addr = s.accept()
    usr=conn.recv(1024).decode('utf-8')
    msg = usr + " Join in the Group"    # with Port No: "+ str(addr[1])
    sesson.append(conn)
    print(sesson)
    for ses in sesson:
        ses.send(msg.encode('utf-8'))

    th.start_new_thread(recvValue,(conn, addr, usr))






'''def sendMessage():
    svrMsg = "Server: "+sendMsgText.get()
    for c in sesson:
        c.send(svrMsg.encode('utf-8'))
    sendMsgText.delete(0,END)
    sendMsgText.focus() 

def mainThread(s):
    conn, addr = Sokt.accept()
    sesson.append(conn)
    label['text']="New Connection From :"+ str(addr[1])
    th.start_new_thread(recvValue, (conn, addr))

root=Tk()
root.title("Server Chat Window")
root.geometry("400x345")
root['bg']="#00ff40"


label=Label(root,text="", font=("bold",10))
label.place(x=5, y=5,width=390, height=300)

sendMsgText=Entry(root, font=("normal",15))
sendMsgText.place(x=5,y=310,width=300,height=30)

sendBttn=Button(root, text="Send", bg="#ff0000", command=sendMessage)
sendBttn.place(x=310, y=310, width=85, height=30)

th.start_new_thread(mainThread, (Sokt,))
root.mainloop()'''



