from tkinter import *
import random
import time
from tkinter.ttk import *

#this is the main window
root=Tk()
#this is ro set the size and width of the main window
root.geometry("1000x1000")
#This is to set the title of the main window
root.title("Sample form")
#This is to resize the window
root.resizable("True","True")

def generate_colours(rgb):
    return "#%02x%02x%02x" % rgb

cn=Canvas(root,background="black",width=1000,height=1000)
cn.pack()

for j in range(100):
    for i in range(1,250,10):
        random_clr=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        coordinates=250+i,100+i,750-i,600-i
        cn.create_rectangle(coordinates,fill=generate_colours(random_clr))
    cn.update()
    time.sleep(0.001)


root.mainloop()
