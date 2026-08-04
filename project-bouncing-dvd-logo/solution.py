import tkinter as tk
import random

W, H, SIZE, SPEED = 400, 300, 60, 4
COLORS = ["red", "green", "blue", "yellow", "cyan"]

root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H, bg="black")
canvas.pack()
logo = canvas.create_rectangle(0, 0, SIZE, SIZE / 2, fill="white")
vx, vy = SPEED, SPEED

def tick():
    global vx, vy
    x1, y1, x2, y2 = canvas.coords(logo)
    if x1 <= 0 or x2 >= W:
        vx = -vx
        canvas.itemconfig(logo, fill=random.choice(COLORS))
    if y1 <= 0 or y2 >= H:
        vy = -vy
        canvas.itemconfig(logo, fill=random.choice(COLORS))
    canvas.move(logo, vx, vy)
    root.after(16, tick)

tick()
root.mainloop()
