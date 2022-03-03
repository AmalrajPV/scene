from tkinter import *

root = Tk()
root.geometry('500x600')
canvas = Canvas(root, width=500, height=600, background="skyblue")
canvas.pack()

n = 0
canvas.create_polygon(n + 0, 400, n + 100, 200, n + 200, 400, fill="grey", outline="grey")
n = 150
canvas.create_polygon(n + 0, 400, n + 100, 200, n + 200, 400, fill="grey", outline="grey")
n = 300
canvas.create_polygon(n + 0, 400, n + 100, 200, n + 200, 400, fill="grey", outline="grey")

canvas.create_rectangle(0, 400, 500, 600, fill="grey", outline="grey")

canvas.create_polygon(0, 500, 60, 350, 120, 500, fill="white", outline="white")
canvas.create_polygon(42, 408, 60, 355, 120, 500, 69, 396, 61, 403, 55, 390, fill="lightblue", outline="white")

canvas.create_polygon(60, 500, 120, 350, 200, 500, fill="white", outline="white")
canvas.create_polygon(101, 403, 121, 362, 172, 458, 137, 402, 127, 408, 118, 398, 117, 415, 107, 403, fill="lightblue",
                      outline="white")

canvas.create_polygon(180, 500, 260, 350, 360, 500, fill="white", outline="white")
canvas.create_polygon(194, 480, 261, 358, 342, 479, 287, 415, 286, 438, 265, 420, 262, 437, 249, 430, 224, 503,
                      fill="lightblue", outline="lightblue")

canvas.create_polygon(340, 500, 420, 380, 500, 500, fill="white", outline="white")
canvas.create_polygon(354, 486, 420, 385, 492, 491, 435, 422, 447, 448, 422, 424, 413, 453, 405, 423, fill="lightblue",
                      outline="lightblue")

canvas.create_rectangle(0, 500, 500, 600, fill="white", outline="white")
canvas.create_polygon(0, 549, 58, 558, 68, 546, 66, 560, 73, 553, 73, 566, 111, 574, 198, 542, 196, 536, 283, 554, 326,
                      540, 339, 542, 341, 534, 354, 537, 372, 533, 372, 526, 378, 536, 385, 528, 387, 537, 406, 530,
                      447, 547, 500, 524, 500, 600, 0, 600, fill="lightblue", outline="lightblue")
canvas.create_polygon(0, 550, 58, 558, 68, 546, 66, 560, 73, 553, 73, 566, 93, 571, 0, 600, fill="skyblue",
                      outline="skyblue")
canvas.create_oval(160, 100, 230, 170, fill="lightyellow", outline="white")

canvas.create_oval(30, 180, 70, 160, fill="white", outline="white")
canvas.create_oval(80, 180, 120, 160, fill="white", outline="white")
canvas.create_oval(50, 150, 100, 185, fill="white", outline="white")

canvas.create_oval(230, 210, 280, 190, fill="white", outline="white")
canvas.create_oval(290, 210, 340, 190, fill="white", outline="white")
canvas.create_oval(260, 180, 310, 215, fill="white", outline="white")

canvas.create_oval(330, 110, 380, 90, fill="white", outline="white")
canvas.create_oval(390, 110, 440, 90, fill="white", outline="white")
canvas.create_oval(360, 80, 410, 115, fill="white", outline="white")

canvas.create_line(382, 486, 382, 600, fill="brown", width=15)
canvas.create_polygon(334, 521, 434, 521, 384, 439, fill="green", outline="green")
canvas.create_polygon(334, 500, 434, 500, 384, 418, fill="green", outline="green")
canvas.create_polygon(334, 480, 434, 480, 384, 398, fill="green", outline="green")
canvas.create_polygon(334, 460, 434, 460, 384, 378, fill="green", outline="green")


def pos(e):
    print(e.x, e.y)

root.bind('<Button-1>', pos)

root.mainloop()
