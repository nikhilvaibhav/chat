import socket
from tkinter import *



def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0,END )
    client.send(bytes(message, 'utf-8'))
    receive(listbox)

def receive(listbox):
    message_from_client = client.recv(200)
    listbox.insert('end',"client", message_from_client.decode('utf-8'))

root = Tk()
root.title("SERVER")
entry = Entry()
entry.pack()

button = Button(root,text = "Send",bg = "cyan", command = lambda : send(listbox, entry))
button.pack(side = BOTTOM)

rbutton = Button(root, text = "Receive", bg = "cyan", command = lambda  : receive(listbox))
rbutton.pack(side = BOTTOM)

listbox = Listbox(root)
listbox.pack()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()

PORT = 12345

s.bind((HOST_NAME,PORT))

s.listen(4)

client, address = s.accept()

root.mainloop()