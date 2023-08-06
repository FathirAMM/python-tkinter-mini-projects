from tkinter import *
import random
import time

#this is the main window
root=Tk()
#this is ro set the size and width of the main window
root.geometry("1000x1000")
#This is to set the title of the main window
root.title("Sample form")
#This is to resize the window
root.resizable("True","True")





cn=Canvas(root,background="black",width=1000,height=1000)
cn.pack()

def generate_colours(rgb):
    return "#%02x%02x%02x" % rgb


def make_tree(initial_coordinates_x,initial_coordinates_y):
    if(initial_coordinates_y<0):
        return
    else:
        num_1=int(initial_coordinates_x+160)
        num_2=int(initial_coordinates_y-160)
        next_x_coordinate=random.randint(initial_coordinates_x,num_1)
        next_y_coordinate=random.randint(num_2,initial_coordinates_y)
        clr=generate_colours((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        cn.create_line(initial_coordinates_x,initial_coordinates_y,next_x_coordinate,next_y_coordinate,fill=clr,width=3)
        make_tree(next_x_coordinate,next_y_coordinate)
        make_tree(next_x_coordinate,next_y_coordinate)
    cn.update()
make_tree(0,780)

root.mainloop()