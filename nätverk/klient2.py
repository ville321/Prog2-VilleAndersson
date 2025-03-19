from socket import *
def connect_to_server():    # samma som i tidigare exempel
    s = socket()
    host = input("Ange serverns IP-adress:")
    port = 12345
    s.connect((host, port))
    return s
conn = connect_to_server()
b = conn.recv(1024)
msg = b.decode('utf-16')
print(msg)
from tkinter import *   # konstruera det grafiska gränssnittet
root = Tk()
canv = Canvas(root, height=250, width=300, bg="blue")
canv.pack()
id1 = canv.create_oval(0, 100, 50, 150, fill="yellow")
id2 = canv.create_oval(0, 100, 50, 150, fill="red")
color = ""
while color not in ["g", "r"]:      # kontrollera korrekt input
    color = input("Ange färg (g/r):")   # g för gul, r för röd
def send_msg(e):                   # skicka meddelanden till servern
    key = e.keysym
    if key in ["Up", "Down", "Left", "Right"]:
        msg = color + e.keysym      # t.ex. "gUp" eller "rLeft"
        b = msg.encode("utf-16")
        conn.send(b)
canv.bind_all("<Key>", send_msg)
def receiver_thread():      # ta emot meddelanden från servern
    while True:
        b = conn.recv(1024)
        msg = b.decode("utf-16")
        msg = msg.replace("Servern tog emot följande meddelande: ", "")
        if msg[0] == "g":   # flytta gul cirkel
            id = id1
        else:               # flytta röd cirkel
            id = id2
        if msg[1] == "L" and canv.coords(id)[0] > 0:  # "Left"
            canv.move(id, -50, 0)
        if msg[1] == "R" and canv.coords(id)[0] < 250:  # "Right"
            canv.move(id, 50, 0)
        if msg[1] == "U" and canv.coords(id)[3] > 50:  # "Up"
            canv.move(id, 0, -50)
        if msg[1] == "D" and canv.coords(id)[3] < 250:  # "Down"
            canv.move(id, 0, 50)
from _thread import *
start_new_thread(receiver_thread, ())
root.mainloop()
