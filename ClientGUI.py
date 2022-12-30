from tkinter import *
from tkinter import messagebox

import socket
import _thread as th
import time

def ConnectWithServer():
    global s
    global host
    global port
    global clientName
    clientName= clientNameTxt.get()
    print(clientName)
    if clientName == "":
        messagebox.showerror("Error", "Enter User Name")
        clientNameTxt.focus()
    else:
        try:
            s = socket.socket((socket.AF_INET),socket.SOCK_STREAM)
            host="127.0.0.1"
            port=1234

            s.connect((host, port))
            s.send(clientName.encode('utf-8'))

            th.start_new_thread(recvValue, (s,))
            time.sleep(1)
            connectBtn['state'] = 'disable'
            stopConnectBtn['state'] = 'normal'
            clientNameTxt['state'] = 'disable'

        except Exception as e:
            messagebox.showerror("Error", e)

def StopConnectionWithServer():
    msg='StopConnection'
    s.send(msg.encode('utf-8'))
    time.sleep(2)
    #print(msg)
    root.quit()

def SendMessage():
    msg = sendMsgText.get()
    s.send(msg.encode('utf-8'))
    msgTxt['state'] = 'normal'
    msgTxt.insert(END, clientName + " : " + msg + '\n')
    msgTxt['state'] = 'disable'
    sendMsgText.delete(0,END)

def recvValue(s):
    while True:

        # msgTxt.configure(anchor=W)
        try:
            msg=s.recv(1024).decode('utf-8')
            #print(msg)
            msgTxt['state'] = 'normal'
            msgTxt.insert(END, msg + '\n')
            msgTxt['state'] = 'disable'
        except Exception as e:
            messagebox.showerror("Error",e)
            root.quit()
        #label['text'] += '\n'+s.recv(1024).decode('utf-8')

root=Tk()
root.title("Client Chat Window")
root.geometry("600x400")
root['bg'] = "#00ff40"

clientNameLbl = Label(root, text="User Name: ", anchor=W, bg="#00ff40", fg="blue", font = ("bold",)).place(x=5, y=5)

clientNameTxt = Entry(root)
clientNameTxt.place(x=100, y=5, width=290, height=30)

connectBtn = Button(root, text="Connect", bg="red", command= ConnectWithServer)
connectBtn.place(x=400, y=5, width=80, height=30)

stopConnectBtn = Button(root, text="Stop", bg="red", state='disable', command= StopConnectionWithServer)
stopConnectBtn.place(x=485, y=5, width=80, height=30)

msgTxt = Text(root)
msgTxt.insert(0.0,"Public Chat Room\n")
msgTxt.configure(state="disable")

msgTxt.place(x=5, y=40, width=390, height=320)


#label=Label(root,text="aaaaa", font=("bold", 10), anchor=NW )
#label.config(state='disable')
#label.configure(state='disable')
#label.place(x=5, y=20, width=390, height=300)

sendMsgText=Entry(root, font=("normal",15))
sendMsgText.place(x=5,y=365, width=300, height=30)

sendBttn=Button(root, text="Send", bg="#ff0000", command=SendMessage)
sendBttn.place(x=310, y=365, width=85, height=30)



root.mainloop()
