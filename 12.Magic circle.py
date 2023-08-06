import tkinter as tk 
from tkinter.ttk import * 
import random 
import time 
### Window###
window = tk.Tk() 
window.geometry("800x800") 
window.title("colour circle.....")
###generate colours###
def from_rgb(rgb): 
	return "#%02x%02x%02x" % rgb

###canvas###
canv = tk.Canvas(window, background="White", height=600, width=600) 
canv.pack()
###coordinates###
coord = 10,10,790,790 

###fucntion to draw###
def draw():
    gap=random.randint(1,30) 
    for ind in range(0, 360,gap):
        color=from_rgb((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        arc=canv.create_arc(coord, start=ind,extent=gap,fill=color)
            
###infinite loop to draw ###

while(1):
    draw() 
    time.sleep(0.5) 
    canv.update()

window.mainloop() 

