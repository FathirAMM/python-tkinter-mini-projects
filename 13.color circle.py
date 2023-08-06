import tkinter as tk 
from tkinter.ttk import *
import random 
import time 
### Window###
window = tk.Tk() 
window.geometry("800x800") 
window.title("colour circle.....")
###canvas###
canv = tk.Canvas(window, background="White", height=800, width=800) 
canv.pack() 

### drawing the circles ###

def draw(i):
    coordl = 200+i,0+i,600+i,400+i 
    coord2 = 400-i,200+i,800-i,600+i 
    coord3 = 200-i,400-i,600+i,800-i 
    coord4 = 0+i,200-i,400+i,600-i 
    canv.create_oval(coordl, outline="red") 
    canv.create_oval(coord2, outline="blue") 
    canv.create_oval(coord3, outline="yellow") 
    canv.create_oval(coord4, outline="green") 
### loop for drawing ####
for i in range(0,200,2):
     draw(i) 
     time.sleep(0.1) 
     canv.update() 
window.mainloop() 


