#import libraries and there elements 
from tkinter import *
from tkinter.ttk import *
from time import strftime
#create the main window of our code 
root = Tk()
root.title("clock")
#define function in which we have to declare the time format and other things
def time():
    string = strftime("%H:%M:%S%p")
    label.config(text=string)
    label.after(1000,time)

#define  appearance of clock
label = Label(root, font =("ds-digital",80),background="black",foreground="magenta")
label.pack(anchor='center')
# callout the function 
time()
#use this to tell tkinter to run event loop (refresh rate )
mainloop()