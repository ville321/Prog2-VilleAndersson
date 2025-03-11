from socket import *
from tkinter import *
import threading

def connect_to_server():
    s = socket()
    host = input("Ange serverns IP-adress:")
    port = 12345
    s.connect((host, port))
    return s

def receive_drawing_data(conn):
    while True:
        data = conn.recv(1024)
        if data:
            x1, y1, x2, y2 = map(int, data.decode("utf-8").split(","))
            canv.create_line(x1, y1, x2, y2, fill="black", width=2)

def draw(event):
    x, y = event.x, event.y
    if hasattr(draw, 'last_x'):
        if 0 <= x <= canv.winfo_width() and 0 <= y <= canv.winfo_height():
            canv.create_line(draw.last_x, draw.last_y, x, y, fill="black", width=2)
            data = f"{draw.last_x},{draw.last_y},{x},{y}"
            conn.send(data.encode("utf-8"))
    draw.last_x, draw.last_y = x, y

def reset_last_position(event):
    if hasattr(draw, 'last_x'):
        del draw.last_x
        del draw.last_y

conn = connect_to_server()

root = Tk()
canv = Canvas(root, height=250, width=300, bg="blue")
canv.pack()

canv.bind("<B1-Motion>", draw)
canv.bind("<ButtonRelease-1>", reset_last_position)

threading.Thread(target=receive_drawing_data, args=(conn,), daemon=True).start()

root.mainloop()