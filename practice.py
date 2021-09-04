import tkinter as tk
from tkinter.constants import COMMAND, END, HORIZONTAL
from PIL import ImageTk,Image
import random
height = 1050
width = 1680
root = tk.Tk()
root.title('Dreamyy')

class EmptyArray(Exception):
    def __init__(self, msg):
        self.msg = msg


class ArrayQueue():
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        try:
            if len(self.items) == 0:
                raise EmptyArray("Array is empty!")

            return self.items.pop(0)
        except EmptyArray as err:
            print(err)
    
    def update(self, value, update):
        self.items[value - 1] = update

    def first(self):
        try:
            if len(self.items) == 0:
                raise EmptyArray("Array is empty!")

            return self.items[0]
        except EmptyArray as err:
            print(err)

    def allElements(self):
        return self.items



instantiate = ArrayQueue()

def listy(entryy):
    instantiate.enqueue(entryy)
    entry.delete(0, END)

def bobo(numbery):

    if int(numbery) < 200:
        mdehgui = instantiate.first()
        instantiate.dequeue()
        label4 = tk.Label(toppy, text=f"I have no doubt that you are feeling blue. I'll make you happy a little bit.", font=25)
        label4.place(rely=0, relx=0.08)
        label5 = tk.Label(toppy, text=f"Gongrats! You accomplished {mdehgui}", font=25)
        label5.place(rely=0.05, relx=0.3)
    else:
        label4 = tk.Label(toppy, text=f"It's great that you're doing well! I grant you Pony", font=25)
        label4.place(rely=0, relx=0.2)
    
def blessing():
    global myimg1
    global toppy
    toppy = tk.Toplevel()
    toppy.title("Blessing")
    myimg1 = ImageTk.PhotoImage(Image.open("./fgui/images/blessing.png"))
    my_labell = tk.Label(toppy, image=myimg1).pack()
    horizontal = tk.Scale(toppy, from_=0, to=1000, orient=HORIZONTAL)
    horizontal.place(rely=0.43)

    haha = tk.Label(toppy, text="Are you happy?")
    haha.place(rely=0.4)

    love = tk.Button(toppy, text="Bless me", command=lambda: bobo(horizontal.get()))
    love.place(relx=0.13, rely=0.45)

    my_labell = tk.Label(toppy, text=horizontal.get())
    my_labell.place(relx=1, rely=0.3)

def openShow():
    global my_img
    top = tk.Toplevel()
    top.title("Show items")
    my_img = ImageTk.PhotoImage(Image.open("./fgui/images/bucket-list.png"))
    my_label = tk.Label(top, image=my_img).pack()
    lablel = tk.Label(top, text=f"Items on Bucket List: {instantiate.allElements()}")
    lablel.place(relx=0.1, rely=0.1)

def updatey(entry1, entry2):
    instantiate.update(int(entry1), entry2)
    index.delete(0, END)
    value.delete(0, END)


def openUpdate():
    global my_img1
    global index
    global value
    top = tk.Toplevel()
    top.title("Update")
    my_img1 = ImageTk.PhotoImage(Image.open("./fgui/images/bucket.png"))
    my_label = tk.Label(top, image=my_img1)
    my_label.pack()
    lablel = tk.Label(top, text=f"Items on Bucket List: {instantiate.allElements()}")
    lablel.place(relx=0, rely=0.02)

    index_label = tk.Label(top, text="Index", font=25)
    index_label.place(rely=0.1)

    index = tk.Entry(top, font=25)
    index.place(rely=0.1, relx=0.06)

    value_label = tk.Label(top, text="value", font=25)
    value_label.place(rely=0.15)

    value = tk.Entry(top, font=25)
    value.place(rely=0.15, relx=0.06)

    updateButton = tk.Button(top, text="Update", font=120, command=lambda: [updatey(index.get(), value.get()), top.destroy()])
    updateButton.place(rely=0.1, relx=0.3, relheight=0.09)


canva = tk.Canvas(root, height=height, width=width)
canva.pack()

background_image = tk.PhotoImage(file='./fgui/images/picture.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.05, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Enter an item", font=25, command=lambda: listy(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

update = tk.Button(root, text="Update an item", font=15, command= openUpdate)
update.place(relx=0, relheight=0.05, relwidth=0.09)

show = tk.Button(root, text="Show items", font=15, command= openShow)
show.place(relx=0.91, relheight=0.05, relwidth=0.09)

pray = tk.Button(root, text=" ", font=1, command=blessing)
pray.place(rely=0.86, relx=0.489, relheight=0.01, relwidth=0.005)



root.mainloop()