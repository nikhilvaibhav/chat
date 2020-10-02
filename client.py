import socket
from tkinter import *



def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0,END)
    s.send(bytes(message, 'utf-8'))
    receive(listbox)

def receive(listbox):
    message = s.recv(200)
    listbox.insert('end',"Server: ",message.decode('utf-8'))

root = Tk()
root.title("CLIENT")
entry = Entry()
entry.pack(side = BOTTOM)

button = Button(root,text = "Send",bg = "magenta", command = lambda : send(listbox, entry))
button.pack(side = BOTTOM)

rbutton = Button(root, text = "Receive", bg = "magenta", command = lambda  : receive(listbox))
rbutton.pack(side = BOTTOM)

listbox = Listbox(root)
listbox.pack()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME,PORT))

root.mainloop()